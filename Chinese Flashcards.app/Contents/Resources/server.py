#!/usr/bin/env python3
"""
Chinese Flashcards — local server.

Serves the app at http://localhost:8080 and persists all data to:
  ~/Library/Application Support/Chinese Flashcards/data.json

Works in Safari, Chrome, Firefox, and Edge.

Usage:
    python3 server.py
"""

import json
import os
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

# ── Data file path ─────────────────────────────────────────────────────────────
# Store user data in Application Support, not inside the .app bundle.
# Writing inside a .app at runtime is bad macOS practice and can be blocked
# by Gatekeeper.
DATA_DIR  = os.path.expanduser('~/Library/Application Support/Chinese Flashcards')
DATA_FILE = os.path.join(DATA_DIR, 'data.json')


def _init_data_dir():
    """
    Ensure the data directory exists, then migrate legacy data if needed.

    Migration: if data.json doesn't exist in Application Support yet but an
    old data.json sits next to the .app bundle (three levels up from this
    file: Resources → Contents → .app → parent folder), copy it across once.
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        # Walk up: server.py → Resources → Contents → .app → parent folder
        bundle_parent = os.path.dirname(  # parent of .app
            os.path.dirname(              # .app
                os.path.dirname(          # Contents
                    os.path.dirname(      # Resources
                        os.path.abspath(__file__)
                    )
                )
            )
        )
        legacy = os.path.join(bundle_parent, 'data.json')
        if os.path.exists(legacy):
            shutil.copy2(legacy, DATA_FILE)
            print(f'Migrated existing data from {legacy}')


class Handler(SimpleHTTPRequestHandler):

    # ── API routes ────────────────────────────────────────────────────────────

    def do_GET(self):
        if self.path == '/data':
            self._serve_data()
        else:
            # Fall through to SimpleHTTPRequestHandler for static files
            # (index.html, dictionary.js, etc.)
            super().do_GET()

    def do_POST(self):
        if self.path == '/data':
            self._save_data()
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        # Pre-flight CORS — not strictly needed for same-origin requests
        # but included for completeness.
        self.send_response(204)
        self._add_cors_headers()
        self.end_headers()

    # ── Handlers ──────────────────────────────────────────────────────────────

    def _serve_data(self):
        """Return data.json, or an empty object if it doesn't exist yet."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                body = f.read().encode('utf-8')
        else:
            body = b'{}'

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self._add_cors_headers()
        self.end_headers()
        self.wfile.write(body)

    def _save_data(self):
        """Write the POST body to data.json after validating it is valid JSON."""
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)

        try:
            json.loads(body)  # Validate before writing — reject malformed payloads
        except json.JSONDecodeError as e:
            self.send_error(400, f'Invalid JSON: {e}')
            return

        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(body.decode('utf-8'))
        except IOError as e:
            self.send_error(500, f'Could not write data.json: {e}')
            return

        self.send_response(200)
        self._add_cors_headers()
        self.end_headers()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _add_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def log_message(self, format, *args):
        # Suppress per-request logs to keep the terminal clean.
        # Remove this override if you want to see request logs.
        pass


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    _init_data_dir()
    server = HTTPServer(('localhost', PORT), Handler)
    print(f'Serving Chinese Flashcards at http://localhost:{PORT}')
    print(f'Data file: {DATA_FILE}')
    print('Press Ctrl+C to stop.\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
