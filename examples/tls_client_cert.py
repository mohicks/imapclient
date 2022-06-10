# Establish a secure connection to a server that requires clients ro
# provide a certificate.

import ssl
import os.path as path

from imapclient import IMAPClient

HOST = "imap.host.com"
USERNAME = "someuser"
PASSWORD = "secret"
CERT = path.expanduser("~/path/to/cert.crt")
KEY = path.expanduser("~/path/to/privkey.key")

ssl_context = ssl.create_default_context()

ssl_context.load_cert_chain(CERT, KEY)

with IMAPClient(HOST, ssl_context=ssl_context) as server:
    server.login(USERNAME, PASSWORD)
    # ...do something...
