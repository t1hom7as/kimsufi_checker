import argparse
import sys
import time

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

URL = 'https://www.ovh.com/engine/api/dedicated/server/availabilities?country=eu'
TIME = 8


class KimiException(Exception):
    pass


class Colours:
    red = '\033[0;31;40m'
    yellow = '\033[0;33;40m'
    green = '\033[0;32;40m'
    reset = '\033[0m'


class Checker:
    def __init__(self, selection):
        self.server = False
        self.server_choice = False
        self.selection = selection

    def grab_data(self):
        try:
            r = requests.get(URL)
            if r.status_code == 200:
                data = r.json()
                return data
        except requests.RequestException:
            raise KimiException(f'{Colours.yellow}Unable to connect to OVH{Colours.reset}')
        except (ValueError, KeyError):
            raise KimiException(f'{Colours.yellow}Invalid response from OVH{Colours.reset}')

    def mas_data(self, data):
        for x in data:
            if self.server_choice in x['hardware']:
                for y in x['datacenters']:
                    if y['datacenter'] == 'default':
                        continue
                    if y['availability'] != 'unavailable':
                        self.server = True
                        print(f'{Colours.green}Server available in: {y["datacenter"]}{Colours.reset}')
                        print(f'https://www.kimsufi.com/uk/order/kimsufi.xml?reference={self.server_choice}\n')  # noqa: E501¬

    def loop(self):    # noqa: C901
        print(f'\nProbing every {TIME} seconds...\n')
        try:
            self.server_choice = SERVER_DICT[self.selection]
        except KeyError:
            raise KimiException('Invalid selection')

        while True:
            data = self.grab_data()
            self.mas_data(data)

            if not self.server:
                print(f'{Colours.red}No servers available{Colours.reset} {time.ctime()}')
                time.sleep(TIME)
            else:
                break


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('ks', help='Available options:\nks1\nks2\nks3\nks4\n'
                        'ks5\nks6\nks7\nks8\nks9\nks10\nks11\nks12\n')
    args = parser.parse_args()
    selection = args.ks

    if selection not in SERVER_DICT.keys():
        sys.exit(f'{Colours.yellow}Invalid option{Colours.reset}')

    checker = Checker(selection)

    try:
        checker.loop()
    except KimiException as ex:
        sys.exit(ex.args[0])
    except KeyboardInterrupt:
        sys.exit('\rBye...')
