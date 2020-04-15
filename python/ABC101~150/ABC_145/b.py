def main():
    n = int(input())
    x = input()
    if x[:(n//2)] == x[(n//2):]:
        print("Yes")
        exit(0)
    print("No")


if __name__ == "__main__":
    main()