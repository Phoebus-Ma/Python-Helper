###
# Python http post example.
# 
# License - MIT.
###

import os

# pip install requests.
import requests

# pip install lxml
# pip install beautifulsoup4
from bs4 import BeautifulSoup


# login github class.
class login_github():
# {
    # Initialization function.
    def __init__(self):
    # {
        # Chromium core browser user agent.
        self._headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
        }

        self._login_page    = 'https://github.com/login'
        self._session_page  = 'https://github.com/session'

        self._session       = requests.Session()
    # }


    # Get html data.
    def datas(self, url_path):
    # {
        datas = self._session.get(url = url_path, headers = self._headers)

        return datas
    # }


    # Http Get.
    def get(self):
    # {
        html    = requests.get(url = self._login_page, headers = self._headers)
        soup    = BeautifulSoup(html.text, 'lxml')
        tokens  = soup.find_all('input', type="hidden")[1]
        attrs   = tokens.attrs['value']

        return attrs
    # }


    # Http Post.
    def post(self, Username, Password):
    # {
        data = {
            'commit'            : 'Sign in',
            'utf8'              : ' ✓',
            'authenticity_token': self.get(),
            'login'             : Username,
            'password'          : Password,
            'webauthn-support': ' supported'
        }

        # Post.
        res = self._session.post(
            url     = self._session_page,
            data    = data,
            headers = self._headers
        )
    # }
# }


# Main function.
def main():
# {
    test_page = 'https://github.com/torvalds/linux'

    print('Login Github !')
    Username = input('Username or email address: ')
    Password = input('Password: ')

    login = login_github()

    # login.
    login.post(Username, Password)

    # get data.
    datas = login.datas(test_page)

    with open('test.html', 'wb') as fd:
        fd.write(datas.content)
# }


# Program entry.
if '__main__' == __name__:
    main()
