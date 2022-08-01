###
# Python aiohttp server test example.
# 
# License - MIT.
###

import os

# pip install aiohttp.
from aiohttp import web


# aiohttp_hanlde - aiohttp test handler function.
async def aiohttp_hanlde(request):
# {
    name = request.match_info.get('name', 'Anonymous')

    text = 'Hello, ' + name

    return web.Response(text = text)
# }


# Main function.
def main():
# {
    app = web.Application()

    app.add_routes(
        [
            web.get('/', aiohttp_hanlde),
            web.get('/{name}', aiohttp_hanlde)
        ]
    )

    web.run_app(app)

    print('Press CTRL+C to quit.')

    # http://localhost:8080
    # http://localhost:8080/linus
    # http://127.0.01:8080
    print('Type http://localhost:8080 in your browser')
# }


# Program entry.
if '__main__' == __name__:
    main()
