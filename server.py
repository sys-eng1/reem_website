from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the port on which you want to run the server
PORT = 8000

# Set up a simple HTTP request handler
handler = SimpleHTTPRequestHandler

# Create an HTTP server
httpd = HTTPServer(('localhost', PORT), handler)

print(f"Serving on port {PORT}")
httpd.serve_forever()
