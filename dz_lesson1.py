
import ipaddress
import subprocess

from tabulate import tabulate


def host_ping(addr):
    return (
        subprocess.call(['ping', str(addr)],  stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        ==0
        )

def host_range_ping(addresses):
    res = {}
    for addr in addresses:
        res[addr] = host_ping(addr)
    return res

def host_range_ping_tab(ping_res):
    colums = ['HOST', 'STATUS']
    return tabulate(ping_res.items(), headers=colums, tablefmt="github")

if __name__ == '__main__':
    res = host_ping(addr = ipaddress.ip_address('127.0.0.1'))
    print('Первое задание', res)

    addresses = ('127.0.0.1', 'yandex.ru')
    res = host_range_ping(addresses)
    print('Второе задание',res)


    # res = host_range_ping(['127.0.0.1', 'yandex.ru'])
    table = host_range_ping_tab(res)

    print('Третье задание\n', table)