from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        uid = query.get("uid", [None])[0]

        if not uid:
            self.send_json({
                "success": False,
                "error": "UID is required",
                "example": "/api/info?uid=123456789"
            }, 400)
            return

        # Temporary response
        # Real Free Fire data source will be connected later.
        data = {
            "success": True,
            "uid": uid,
            "nickname": "Unknown",
            "level": None,
            "region": None,
            "likes": None,
            "rank": None,
            "message": "Free Fire data source not connected yet"
        }

        self.send_json(data, 200)

    def send_json(self, data, status):
        body = json.dumps(data, ensure_ascii=False)

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(body.encode("utf-8"))
