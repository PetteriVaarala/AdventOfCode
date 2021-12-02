#!/usr/bin/env python3

def main():
    x = 0
    depth = 0
    with open('input') as f:
        for line in f:
            command = line.strip().split(" ")
            if command[0] == "forward":
                x += int(command[1])
            elif command[0] == "down":
                depth += int(command[1])
            elif command[0] == "up":
                depth -= int(command[1])
            print(f'{command=} {x=} {depth=}')

    print(f'Answer: {x*depth}')


if __name__ == "__main__":
    main()
