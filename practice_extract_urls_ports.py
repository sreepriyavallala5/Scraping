import re
from urllib.parse import urlparse

URL_RE = re.compile(r'(https?://[^\s,<>()"\']+)', re.IGNORECASE)
PORT_RE = re.compile(rf':(\d{1,5})\b')

def extract_urls(text):
    return URL_RE.findall(text or "")

def extract_ports(text):
    ports = {int(m.group(1)) for m in PORT_RE.finditer(text or "") if 0 < int(m.group(1)) <= 65535}
    return sorted(ports)

if __name__ == "__main__":
    md = """
    Offboard: https://payments.example.com/notify
    Callback: legacy.partner.net:8080/callback
    Another: http://api.example.org:443/path
    """
    print("URLs:", extract_urls(md))
    print("Ports:", extract_ports(md))