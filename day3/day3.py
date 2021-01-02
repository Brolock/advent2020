#! /usr/bin/env python3

import argparse
from pathlib import Path

def get_nb_trees(forest, slopes):
    # Trees encountered on each slope
    trees = [0] * len(slopes)

    for row_id, row in enumerate(forest):
        for slope_id, slope in enumerate(slopes):
            x_slope, y_slope = slope

            if row_id % y_slope == 0 and row[x_slope * row_id % len(row)] == '#':
                trees[slope_id] += 1

    return trees

def reduce_mul(l):
    result = 1
    for x in l:
        result *= x
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()

    forest = (Path(args.input).read_text().strip().split('\n'))
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]
    trees = get_nb_trees(forest, slopes)
    for i, slope in enumerate(slopes):
        print(f"Found {trees[i]} trees on slope {slope}")


    result = reduce_mul(trees)
    print(f"Final result = {result}")
    print(result == 2431272960)
