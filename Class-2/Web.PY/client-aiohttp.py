###
# Python aiohttp client test example.
# 
# License - MIT.
###

import os
import asyncio

# pip install aiohttp.
import aiohttp


# aiohttp_post - aiohttp post test.
async def aiohttp_post(url_path, post_data):
# {
    async with aiohttp.ClientSession() as session:
        async with session.post(url_path, data = post_data) as resp:
            datas = await resp.text()

            print(resp.status)
            print(datas)
# }


# aiohttp_get - aiohttp get test.
async def aiohttp_get(url_path):
# {
    async with aiohttp.ClientSession() as session:
        async with session.get(url_path) as resp:
            datas = await resp.text()

            print(resp.status)
            print(datas)
            # with open('event.html', 'wb') as fd:
            #     fd.write(datas)
# }


# aiohttp_test - aiohttp test function.
async def aiohttp_test():
# {
    get_url     = 'https://www.kernel.org/'
    post_url    = 'http://httpbin.org/post'
    post_data   = b'data'

    # http get.
    await aiohttp_get(get_url)

    # http post.
    await aiohttp_post(post_url, post_data)
# }


# Main function.
def main():
# {
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aiohttp_test())
# }


# Program entry.
if '__main__' == __name__:
    main()
