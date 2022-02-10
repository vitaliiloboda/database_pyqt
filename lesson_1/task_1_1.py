"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»).
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

import platform
from subprocess import Popen, PIPE
from ipaddress import ip_address


def host_ping(list_ip, print_res=True):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # result = []
    rich = []
    unrich = []

    for item in list_ip:
        try:
            ip = ip_address(item)
        except ValueError:
            ip = item

        args = ['ping', param, '1', str(ip)]
        command = Popen(args, stdout=PIPE, stderr=PIPE)
        code = command.wait()

        if code == 0:
            if print_res:
                print(f'{ip}: Узел доступен')
            else:
                rich.append(ip)

        else:
            if print_res:
                print(f'{ip}: Узел недоступен')
            else:
                unrich.append(ip)

    return {'reachable': rich, 'unreachable': unrich}


if __name__ == '__main__':
    ip_list = ['yandex.ru', '5.5.5.5', 'mail.ru', 'youdo.com', '190.17.15.1',
               'youtube.com', 'rabota.ru', 'fffff.com', 'wwwwwww']

    host_ping(ip_list)
