#!/usr/bin/env python3
"""
Universe Android Netboot - Minimal Host Server
Simple HTTP + placeholder for TFTP/NBD.
Goal: Serve boot files and a basic rootfs to a netbooting Pixel 3a.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import argparse

class NetbootHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[NETBOOT] {self.address_string()} - {format % args}")

def main():
    parser = argparse.ArgumentParser(description="Minimal Universe Netboot Host")
    parser.add_argument("--port", type=int, default=8080, help="HTTP port")
    parser.add_argument("--dir", default="./bootfiles", help="Directory to serve")
    args = parser.parse_args()

    os.makedirs(args.dir, exist_ok=True)
    os.chdir(args.dir)

    print("=" * 60)
    print("Universe Android Netboot Host – Simplified")
    print(f"Serving files from: {os.getcwd()}")
    print(f"HTTP listening on port {args.port}")
    print("Place kernel, initramfs, and rootfs images in the bootfiles directory.")
    print("Pixel 3a will pull from here once network is up.")
    print("=" * 60)

    server = HTTPServer(("0.0.0.0", args.port), NetbootHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down cleanly.")
        server.shutdown()

if __name__ == "__main__":
    main()
