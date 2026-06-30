import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print(f"Dummy server running on port {port}")
    server.serve_forever()

def start():
    threading.Thread(target=run_server, daemon=True).start()
