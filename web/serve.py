"""Starts the converter page's static server on 127.0.0.1:8080 in the
background and returns once it answers, so one command serves the page."""
import subprocess
import sys
import time
import urllib.request

log = open("/tmp/web-server.log", "ab")
server = subprocess.Popen(
    [sys.executable, "-m", "http.server", "8080", "--bind", "127.0.0.1", "--directory", "web"],
    stdout=log,
    stderr=subprocess.STDOUT,
    stdin=subprocess.DEVNULL,
)
for _ in range(50):
    try:
        urllib.request.urlopen("http://127.0.0.1:8080/", timeout=1)
        print("serving web/ at http://127.0.0.1:8080/ (pid %d)" % server.pid)
        sys.exit(0)
    except Exception:
        time.sleep(0.2)
print("the server did not start; see /tmp/web-server.log")
sys.exit(1)
