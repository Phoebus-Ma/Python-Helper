###
# Python wsgi test.
# 
# License - MIT
###

import os
from wsgiref.simple_server import make_server


# Server handler.
def server_handler(environ, start_response):
# {
    resp_status = '200 OK'
    http_header = [('Content-Type', 'text/html')]
    http_body   = [b'<h1>Hello, World!</h1>']

    # Respond to client requests.
    start_response(resp_status, http_header)

    # return http body data.
    return http_body
# }


# Main function.
def main():
# {
    web_port = 65531

    # Create web server.
    httpd = make_server('', web_port, server_handler)

    print('Web server start!')
    print('Enter this URL in your browser: 127.0.0.1:%d.' % web_port)
    print('Ctrl+C to stop the server.')

    # Listening for HTTP requests.
    httpd.serve_forever()
# }


# Program entry.
if '__main__' == __name__:
    main()
