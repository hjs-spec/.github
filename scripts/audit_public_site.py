"""Small read-only audit; no secrets, JS execution, crawling or scheduled hosting."""
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

HOSTS = {'humanjudgment.org', 'www.humanjudgment.org'}
ROUTES = ['/', '/protocol', '/developers', '/architecture', '/governance', '/alignment', '/primitives', '/robots.txt', '/sitemap.xml']
MARKERS = ['draft-06', 'nonce', 'validation levels', 'zero pii', 'sovereign witness', '1.5ms', '100k', 'jep-core 0.7', 'event identity']


class Redirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urlsplit(newurl)
        if parsed.scheme != 'https' or parsed.hostname not in HOSTS:
            raise ValueError('Unexpected redirect target; no request sent: ' + newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.text = []
        self.metadata = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'script' and attr.get('src'):
            self.scripts.append(attr['src'])
        if tag == 'meta' and attr.get('name') in ('description', 'robots', 'generator'):
            self.metadata.append(attr)
        if tag == 'link' and attr.get('rel') == 'canonical':
            self.metadata.append(attr)
    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.hidden:
            self.hidden -= 1
    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.text.append(data.strip())


def main():
    root = Path('public-site-audit')
    root.mkdir(exist_ok=True)
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'observations': [],
              'scope': 'Fresh public HTTP, not source/deployment access or search-index verification.'}
    opener = build_opener(Redirects())
    targets = [('www.humanjudgment.org', route) for route in ROUTES] + [('humanjudgment.org', '/'), ('humanjudgment.org', '/developers')]
    for index, (host, route) in enumerate(targets):
        url = 'https://' + host + route
        item = {'requested_url': url}
        try:
            try:
                response = opener.open(Request(url, headers={'User-Agent': 'JEP-public-entry-audit/1.0', 'Cache-Control': 'no-cache'}), timeout=20)
            except HTTPError as exc:
                response = exc
            with response:
                data = response.read(2 * 1024 * 1024 + 1)
                if len(data) > 2 * 1024 * 1024:
                    raise ValueError('Response exceeds audit size limit')
                item.update(status=response.status, final_url=response.url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                            headers={name: response.headers[name] for name in ['date', 'server', 'cache-control', 'age', 'etag', 'content-type', 'x-vercel-id', 'x-vercel-cache', 'cf-cache-status', 'location'] if name in response.headers})
                text = data.decode('utf-8', errors='replace')
            (root / (str(index) + '.body.txt')).write_text(text, encoding='utf-8')
            page = Page()
            page.feed(text)
            visible = '\n'.join(page.text)
            (root / (str(index) + '.visible.txt')).write_text(visible, encoding='utf-8')
            item.update(metadata=page.metadata, scripts=page.scripts[:12], visible_characters=len(visible),
                        indicators=[marker for marker in MARKERS if marker in visible.lower()],
                        rendering='client-rendered-or-sparse' if len(visible) < 200 and page.scripts else 'HTTP text captured')
        except Exception as exc:
            item['error'] = type(exc).__name__ + ': ' + str(exc)
        report['observations'].append(item)
    (root / 'report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))
    if not any(item.get('status') == 200 for item in report['observations']):
        raise SystemExit('No successful response; audit is incomplete')


if __name__ == '__main__':
    main()
