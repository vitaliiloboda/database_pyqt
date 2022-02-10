"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from task_1_1 import host_ping
from ipaddress import ip_address


def host_range_ping(print_res=True):
    # first_ip = '5.5.5.1'
    # last_octet = 3
    first_ip = input('Введите начальный ip-адрес: ')
    first_ip_last_octet = int(first_ip.split('.')[3])
    start = ip_address(first_ip)

    while True:
        last_octet = int(input('Введите последнее значение последнего октета, которое нужно проверить в этом адресе: '))
        if last_octet >= first_ip_last_octet:
            break
        else:
            print('Введите число равное или больше значению последнего октета')

    number = int(last_octet) - first_ip_last_octet

    ip_list = [start]
    for i in range(1, number + 1):
        ip_list.append(start + i)

    # print(ip_list)
    result = host_ping(ip_list, print_res)
    return result


if __name__ == '__main__':
    host_range_ping()
