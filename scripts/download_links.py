"""Release 下载地址：GitHub 原链与用户可选的公共加速入口。"""

from html import escape

REPO = 'yuluoos/TVBox-tvs'
MIRRORS = (
    ('GHFast', 'https://ghfast.top/'),
    ('GH-Proxy', 'https://gh-proxy.org/'),
)
NOTICE = 'GitHub 下载慢时可尝试第三方加速；速度因地区和运营商而异，失败可切换线路。下载后请核对 SHA-256。'


def download_url(version, filename):
    return f'https://github.com/{REPO}/releases/download/v{version}/{filename}'


def markdown_links(version, filename, label='GitHub 原链'):
    url = download_url(version, filename)
    links = [(label, url)]
    links.extend((f'{name}（第三方加速）', prefix + url) for name, prefix in MIRRORS)
    return ' · '.join(f'[{name}]({href})' for name, href in links)


def html_mirrors(version, item):
    url = download_url(version, item['name'])
    links = ' · '.join(
        f'<a href="{escape(prefix + url, quote=True)}">{name}（第三方加速）</a>'
        for name, prefix in MIRRORS
    )
    return (
        f'<div class="alts">{links}</div>'
        '<details><summary>SHA-256 校验值</summary>'
        f'<code style="overflow-wrap:anywhere">{escape(item["sha256"])}</code></details>'
    )
