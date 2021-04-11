# -*- coding: utf-8 -*-

import argparse
from pynyin.pynyin import Pynyin


def main():
    parser = argparse.ArgumentParser(description='Perform simple actions on pinyin strings')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--tone', action='store_true', help='get the (next) tone')
    group.add_argument('-r', '--remove', action='store_true', help='remove tones (preserves other non-ASCII)')
    group.add_argument('-a', '--ascii', action='store_true', help='convert to ASCII')

    parser.add_argument('pinyin', type=str, help='the pinyin string')

    args = parser.parse_args()

    pynyin = Pynyin()

    if args.tone:
        print(pynyin.get_tone(args.pinyin))
    elif args.remove:
        print(pynyin.remove_tones(args.pinyin))
    elif args.ascii:
        print(pynyin.to_ascii(args.pinyin))


if __name__ == '__main__':
    main()
