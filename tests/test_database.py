import os
import socket
import struct
import sys
import unittest


class PostgresSSLRequestTests(unittest.TestCase):
    def test_ssl_request_response(self):
        host = os.environ.get("PGHOST", "127.0.0.1")
        port = int(os.environ.get("PGPORT", "5432"))

        with socket.create_connection((host, port)) as sock:
            sock.sendall(struct.pack(">II", 8, 80877103))
            response = sock.recv(1)

        self.assertEqual(len(response), 1)
        self.assertIn(response, (b"S", b"N"))


if __name__ == "__main__":
    unittest.main()
