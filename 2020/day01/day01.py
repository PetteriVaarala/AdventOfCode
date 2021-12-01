#!/usr/bin/env python3

def main():
    with open('input') as f:
        foo = f.read().split('\n')

    x = 0
    while x != len(foo):
        y = x + 1
        while y != len(foo):
            # print(f'{foo[x]}+{foo[y]}={int(foo[x])+int(foo[y])}, {x}:{y}')
            if int(foo[x]) + int(foo[y]) == 2020:
                print(f'{foo[x]}+{foo[y]}={int(foo[x]) + int(foo[y])}')
                print(f'{foo[x]}*{foo[y]}={int(foo[x]) * int(foo[y])}')
                exit()
            y += 1
        x += 1


if __name__ == "__main__":
    main()
