def main():
    k = int(input())
    s : str = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k]+"...")
if __name__ == "__main__":
    main()