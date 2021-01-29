#! /usr/bin/env python3

import argparse
from pathlib import Path
from collections import Counter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()

    text = Path(args.input).read_text().strip()

    # Part One, Count each elements that appears once in each entry
    gathered_answers = ''
    for entry in [e.replace('\n', '') for e in text.split('\n\n')]:
        gathered_answers += ''.join(set(entry))

    total_yes = sum(Counter(gathered_answers).values())
    print(f'Number of answers with atleast one yes: {total_yes}')


    # Part Two, Count each elements that appears for every user of each entry
    gathered_answers = 0
    for entry in [e + '\n' for e in text.split('\n\n')]:
        c = Counter(entry).most_common()
        all_yes_count = c[0][1]
        for yes_tuple in c:
            yes_answer, yes_count = yes_tuple[0], yes_tuple[1]
            if yes_count == all_yes_count and yes_answer != '\n':
                gathered_answers += 1

    print(f'Number of answers where everyone said yes: {gathered_answers}')
