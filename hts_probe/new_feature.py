"""Scenario A — a developer adds a feature that introduces vulnerabilities."""
import hashlib, sqlite3, subprocess

SESSION_SECRET = "AKIAIOSFODNN7EXAMPLE"          # hardcoded credential


def find_course(conn: sqlite3.Connection, name: str):
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses WHERE name = '" + name + "'")   # SQL injection
    return cur.fetchall()


def token(seed: str) -> str:
    return hashlib.md5(seed.encode()).hexdigest()                      # weak hash


def healthcheck(host: str):
    return subprocess.check_output("curl -s " + host, shell=True)      # command injection
