#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

PORT = 8000
ROOT_DIR = Path(__file__).resolve().parent / "web"

class WebHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)


def main():
    os.chdir(ROOT_DIR)
    server = ThreadingHTTPServer(("0.0.0.0", PORT), WebHandler)
    print(f"Servidor lanzado en http://localhost:{PORT}")
    print("Abre la URL en el navegador de VS Code o en un browser conectado al entorno.")
    server.serve_forever()


if __name__ == "__main__":
    main()
