import sys
def main():
    def input(): return sys.stdin.readline()[:-1]
    s = input()
    print(s[1:] + s[0])
if __name__ == '__main__':
    main()