import requests


class Ip:
    def __init__(self):
        self.info = {
            'email': '1983782527@qq.com'
        }
        self.ver = self.version = 1.0
        self.author = "Rare"
        self.info['ver'] = self.info['version'] = self.ver
        self.info['author'] = self.author

    def get_my_ip(self, format='json'):
        """A function for get ourselves ip, thr key parameter is format which is defaulted as txt.
        There are two choice for this parameter, txt and json."""
        if format == 'txt':
            try:
                resp = requests.get(url='https://ifconfig.me/ip')
                return resp.text
            except Exception:
                raise ConnectionError
        if format == 'json':
            try:
                resp = requests.get(url='https://httpbin.org/ip')
                return resp.text
            except Exception:
                raise ConnectionError


if __name__ == '__main__':
    item = Ip()
    ip = item.get_my_ip('txt')
    print(ip)

