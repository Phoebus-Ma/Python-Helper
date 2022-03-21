###
# Python flask test.
# 
# License - MIT
###

import os
from urllib import request


# Main function.
def main():
# {
    url = 'https://kaifa.baidu.com/'
    
    f = open('TestPage.html', 'wb')

    req = request.Request(url)

    with request.urlopen(req) as fd_url:
        data = fd_url.read()

        f.write(data)

    f.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
