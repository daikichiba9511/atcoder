import sys

def main():
    def input(): return sys.stdin.readline()[:-1]
    a, b = tuple(map(int, input().split()))
    print(((a - b) / a) * 100)

if __name__ == '__main__':
    main()