#! /usr/bin/env python3

import argparse
from pathlib import Path

def two_numbers_sum_to_target(target, numbers):
    ''' search in numbers for two numbers that sum up to target and return their product '''
    complementary = set()
    for x in numbers:
        if x in complementary:
            print(f"Found to complementary number: {x} {target - x}")
            return x * (target - x)
        complementary.add(target - x)

    print(f"No two numbers sum up to {target}")
    return None


def three_numbers_sum_to_target(target, numbers):
    ''' search in numbers for 3 numbers that sum up to target and return their product '''
    for it, x in enumerate(numbers):
        two_numbers_product = two_numbers_sum_to_target(target - x, numbers[it + 1:])
        if two_numbers_product is not None:
            print(f"Complementary product to {x} is {two_numbers_product}")
            return two_numbers_product * x

    print(f"No three numbers sum up to {target}")
    return None






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()


    numbers = [int(x) for x in Path(args.input).read_text().split('\n')[:-1]]
    result = two_numbers_sum_to_target(2020, numbers)
    print(f"product of two numbers is  {result}")

    result = three_numbers_sum_to_target(2020, numbers)
    print(f"product of three numbers is {result}")
