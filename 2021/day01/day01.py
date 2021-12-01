#!/usr/bin/env python3

def main():
    increased = 0
    depth_prev = 9999
    with open('input') as f:
        for line in f:
            depth = int(line.strip())
            if depth > depth_prev:
                increased += 1
                print(f'{depth} (increased)')
            else:
                print(f'{depth}')
            depth_prev = depth
        print(f'Answer: {increased}')


if __name__ == "__main__":
    main()
