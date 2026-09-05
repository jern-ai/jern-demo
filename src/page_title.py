"""Extract the title from an HTML document."""

import html
import re


TITLE_RE = re.compile(r'<title[^>]*>(.*?)</title>', re.IGNORECASE | re.DOTALL)


def extract_title(html_text):
    """Return the text of the first <title> tag in *html_text*, or None."""
    match = TITLE_RE.search(html_text)
    if not match:
        return None
    return html.unescape(match.group(1).strip())
