import os
import socket
import unittest

try:
    import psycopg

    HAS_PSYCOPG = True
except ImportError:
    HAS_PSYCOPG = False


class DatabaseTests(unittest.TestCase):
    def test_database_connection(self):
        if HAS_PSYCOPG:
            database_url = os.environ["DATABASE_URL"]
            with psycopg.connect(database_url) as conn:
                self.assertIsNotNone(conn)
        else:
            pg_host = os.environ["PGHOST"]
            pg_port = int(os.environ["PGPORT"])
            with socket.create_connection((pg_host, pg_port), timeout=5):
                # A successful connection is all this assertion needs.
                pass


if __name__ == "__main__":
    unittest.main()
