#! /usr/bin/env python3

import argparse
from pathlib import Path

def is_password_valid(password_tuple, part):
    policy, password = password_tuple
    policy_amount, policy_char = policy.strip().split()
    lower, upper = (int(el) for el in policy_amount.split('-'))

    if part == 1:
        amount = password.count(policy_char)
        return amount >= lower and amount <= upper
    else:
        return (password[lower - 1] == policy_char) ^ (password[upper - 1] == policy_char)

def check_passwords(passwords, part):
    amount_valid = 0
    for password in passwords:
        if is_password_valid(password, part):
            amount_valid += 1

    return amount_valid

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()

    input_text = Path(args.input).read_text().strip()
    passwords = [tuple(line.split(': ')) for line in input_text.split('\n')]

    result = check_passwords(passwords, part=1)
    print(f"There are {result} valid passwords Part1")

    result = check_passwords(passwords, part=2)
    print(f"There are {result} valid passwords Part2")
