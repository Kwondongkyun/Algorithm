def print_pyramid(n: int):
    # TODO: implement this function
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end='')
        for k in range(1, 2*i):
            print('*', end='')
        print()


def print_inverted_pyramid(n: int):
    # TODO: implement this function
    for i in range(1,n):
        print(" "*(i) + "*"*(2*(n-i)-1))


if __name__ == "__main__":
    N = int(input())
    print_pyramid(N)
    print_inverted_pyramid(N)