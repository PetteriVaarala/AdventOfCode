#!/usr/bin/env python3
import collections


def main():
    increased = 0
    q = collections.deque(3 * [0], 3)
    q_prev = collections.deque(3 * [9999], 3)
    with open('input') as f:
        for line in f:
            depth = int(line.strip())
            q.append(depth)
            if sum(q) > sum(q_prev):
                increased += 1
                print(f'{sum(q)} (increased)')
            else:
                print(f'{sum(q)}')
            q_prev.append(depth)

    print(f'Answer: {increased}')


if __name__ == "__main__":
    main()
