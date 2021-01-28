#! /usr/bin/env python3

import argparse
from math import inf
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()

    text = Path(args.input).read_text().strip()


    max_ID, min_ID, ID_sum = 0, inf, 0
    for line in text.split('\n'):
        binary = (line.replace('B', '1').replace('F', '0')
                      .replace('R', '1').replace('L', '0'))
        row = int(binary[:7], 2)
        column = int(binary[7:], 2)
        seat_ID = row * 8 + column
        max_ID = seat_ID if seat_ID > max_ID else max_ID
        min_ID = seat_ID if seat_ID < min_ID else min_ID
        ID_sum += seat_ID

    missing_ID = sum(x for x in range(min_ID, max_ID + 1)) - ID_sum
    print(f'max_ID = {max_ID}')
    print(f'missing_ID= {missing_ID}')
