#!/usr/bin/env python3
import collections


def main():
    increased = -1
    q = collections.deque(3 * [0], 3)
    q_prev = collections.deque(3 * [0], 3)
    with open('input') as f:
        for line in f:
            depth = int(line.strip())
            q.append(depth)
            if q.count(0) > 0:
                pass
            else:
                if sum(q) > sum(q_prev):
                    increased = increased + 1
                    print(f'{sum(q)} (increased)')
                else:
                    print(f'{sum(q)}')
            q_prev = q.copy()

    print(f'Total: {increased}')


if __name__ == "__main__":
    main()
