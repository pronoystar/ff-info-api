from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        uid = query.get("uid", [None])[0]

        if not uid:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps({
                "success": False,
                "error": "UID is required",
                "example": "/api/info?uid=123456789"
            }).encode())
            return

        response = {
            "success": True,
            "uid": uid,
            "nickname": "Unknown",
            "level": None,
            "region": None,
            "likes": None,
            "rank": None,
            "message": "FF data source not connected yet"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())
