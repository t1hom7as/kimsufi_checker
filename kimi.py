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


class Colours:
    red = '\033[0;31;40m'
    yellow = '\033[0;33;40m'
    green = '\033[0;32;40m'
    reset = '\033[0m'


class Checker:

    def __init__(self):
        self.server = False
        self.server_choice = False

        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('ks', help='Available options:\nks1\nks2\nks3\nks4\n'
            'ks5\nks6\nks7\nks8\nks9\nks10\nks11\nks12\n')
        args = parser.parse_args()
        self.selection = args.ks

        if self.selection not in SERVER_DICT.keys():
            sys.exit(f'{Colours.yellow}Invalid option{Colours.reset}')
    
    def main(self):
        for k, v in SERVER_DICT.items():
            if k == self.selection:
                self.server_choice = v

        if not self.server_choice:
            sys.exit(f'{Colours.yellow}Invalid option{Colours.reset}')

        while True:
            try:
                r = requests.get(URL)
                if r.status_code == 200:
                    data = r.json()
                    output = data['answer']['availability']
            except requests.RequestException:
                sys.exit(f'{Colours.yellow}Unable to connect to OVH{Colours.reset}')
            for x in output:
                if self.server_choice == x['reference']:
                    for y in x['zones']:
                        zone = y['zone']
                        if y['availability'] != 'unavailable':
                                self.server = True
                                print(f'{Colours.green}Server available in: {zone}{Colours.reset}')
                                print(f'https://www.kimsufi.com/uk/order/kimsufi.xml?reference={self.server_choice}\n')
            if not self.server:
                print(f'{Colours.red}No servers available{Colours.reset}')
                time.sleep(5)
            else:
                break

if __name__ == "__main__":
    Checker().main()
