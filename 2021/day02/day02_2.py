#!/usr/bin/env python3

def main():
    x = 0
    depth = 0
    aim = 0
    with open('input') as f:
        for line in f:
            command = line.strip().split(" ")
            if command[0] == "forward":
                x += int(command[1])
                depth += aim * int(command[1])
            elif command[0] == "down":
                aim += int(command[1])
            elif command[0] == "up":
                aim -= int(command[1])
            print(f'{command=} {x=} {depth=} {aim=}')

    print(f'Answer: {x*depth}')


if __name__ == "__main__":
    main()
