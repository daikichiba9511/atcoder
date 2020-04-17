
def main():
    a, b = map(int, input().split())
    if (a - b) % 2 == 1:
        print("IMPOSSIBLE")
    else: print(int((a + b)/ 2))
if __name__ == "__main__":
    main()