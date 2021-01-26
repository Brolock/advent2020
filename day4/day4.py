#! /usr/bin/env python3

import argparse
from pathlib import Path
import re
from time import perf_counter

def valid_fields(entries):
    # All entries except years aren't yet normalized so [^\s]+ is the best match
    pattern = re.compile(r'(?=.*byr:\d{4})'
                         r'(?=.*iyr:\d{4})'
                         r'(?=.*eyr:\d{4})'
                         r'(?=.*hgt:[^\s]+)'
                         r'(?=.*hcl:[^\s]+)'
                         r'(?=.*ecl:[^\s]+)'
                         r'(?=.*pid:[^\s]+)')

    valid_entries = 0
    for entry in entries:
        if re.match(pattern, entry):
            valid_entries += 1
    print(valid_entries)

def valid_data(entries):
    # Lookahead to ignore order of entries, \b to ensure not to have trailing chars
    pattern = re.compile(r'(?=.*byr:(\d{4})\b)'
                         r'(?=.*iyr:(\d{4})\b)'
                         r'(?=.*eyr:(\d{4})\b)'
                         r'(?=.*hgt:(\d+(?:in|cm))\b)'
                         r'(?=.*hcl:#[0-9a-f]{6}\b)'
                         r'(?=.*ecl:(?:amb|blu|brn|gry|grn|hzl|oth)\b)'
                         r'(?=.*pid:\d{9}\b)')
    valid_entries = 0
    for entry in entries:
        m = re.match(pattern, entry)
        if m:
            # Check validity of the data
            byr, iyr, eyr, hgt = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
            if (byr not in range(1920, 2003) or
                iyr not in range(2010, 2021) or
                eyr not in range(2020, 2031)):
                continue

            hgt, hgt_unit = int(hgt[:-2]), hgt[-2:]
            if (hgt_unit == "cm" and hgt not in range(150, 194) or
                hgt_unit == "in" and hgt not in range(59, 77)):
                continue

            valid_entries += 1

    print(valid_entries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()

    text = Path(args.input).read_text()
    # Pack each entry on a line
    text = re.sub(r'\n(?!\n)', r' ', text)
    entries = text.strip().split('\n ')

    # Part One
    valid_fields(entries)

    # Part Two
    valid_data(entries)
