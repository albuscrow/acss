from json import dumps


class SSConfigure:
    def __init__(self):
        self.datas = []

    def add_user(self, port, pwd):
        self.datas.append((port, pwd))

    def to_json(self):
        return dumps(
            {'server': '0.0.0.0',
             'auth': True,
             'fast_open': True,
             'method': 'chacha20',
             'timeout': 60,
             'mode': 'tcp_and_udp',
             'ipv6_first': True,
             'port_password': {port: pwd for port, pwd in self.datas}})
