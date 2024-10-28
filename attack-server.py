from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the server address and port
server_address = ('', 9090)

# Create the HTTP server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Server started on http://localhost:9090")
# Start listening for HTTP requests
httpd.serve_forever()