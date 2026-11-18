from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
        <div style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1>Halo dari Jenkins CI/CD (Python)! 🐍🚀</h1>
            <h2>Tes dekku</h2>
            <p>Versi Aplikasi: <b>v1.0</b></p>
        </div>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), SimpleHandler)
    print("Server Python berjalan di port 5000...")
    server.serve_forever()
