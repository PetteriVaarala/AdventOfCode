#!/usr/bin/env python3

def main():
    with open('input') as f:
        foo = f.read().split('\n')

    x = 0
    while x != len(foo):
        y = x + 1
        while y != len(foo):
            z = y + 1
            while z != len(foo):
                # print(f'{foo[x]}+{foo[y]}+{foo[z]}={int(foo[x])+int(foo[y])+int(foo[z])}, {x}:{y}:{z}')
                if int(foo[x]) + int(foo[y]) + int(foo[z]) == 2020:
                    print(f'{foo[x]}+{foo[y]}+{foo[z]}={int(foo[x]) + int(foo[y]) + int(foo[z])}')
                    print(f'{foo[x]}*{foo[y]}*{foo[z]}={int(foo[x]) * int(foo[y]) * int(foo[z])}')
                    exit()
                z += 1
            y += 1
        x += 1


if __name__ == "__main__":
    main()
