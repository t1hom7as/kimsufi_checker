from pprint import pprint
import sys
import time
import argparse
import requests


SERVER_DICT = {
    'ks1': '1801sk12',
    'ks2': '1801sk13',
    'ks3': '1801sk14',
    'ks4': '1801sk15',
    'ks5': '1801sk16',
    'ks6': '1801sk17',
    'ks7': '1801sk18',
    'ks8': '1801sk19',
    'ks9': '1801sk20',
    'ks10': '1801sk21',
    'ks11': '1801sk22',
    'ks12': '1801sk23'
}


URL = 'http://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2'


class Colours():
    red = '\033[0;31;40m'
    yellow = '\033[0;33;40m'
    green = '\033[0;32;40m'
    reset = '\033[0m'


class Checker():
    server = False
    server_choice = False

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('ks',
            help='Available options:\n'
            'ks1\nks2\nks3\nks4\n'
            'ks5\nks6\nks7\nks8\n'
            'ks9\nks10\nks11\nks12\n')
    args = parser.parse_args()
    selection = args.ks

    for k, v in SERVER_DICT.items():
        if k == selection:
            server_choice = v

    while True:
        try:
            r = requests.get(URL)
            if r.status_code == 200:
                data = r.json()
                output = data['answer']['availability']
        except requests.RequestException:
            sys.exit(f'{Colours.yellow}Unable to connect to OVH{Colours.reset}')

        print(server_choice)
        if server_choice:
            for x in output:
                pprint(x)
                if server_choice in x['reference']:
                    print(x['reference'])
                    for y in x['zones']:
                        zone = y['zone']
                        print(zone)
                        if y['availability'] != 'unavailable':
                            server = True
                            print(f'{Colours.green}Server available in: {zone}{Colours.reset}')
                            print(f'https://www.kimsufi.com/uk/order/kimsufi.xml?reference={server_choice}')
                            break
                if not server:
                    print(f'{Colours.red}No servers available{Colours.reset}')
                time.sleep(5)
        else:
            raise IndexError(f'{Colours.yellow}Invalid option{Colours.reset}')

