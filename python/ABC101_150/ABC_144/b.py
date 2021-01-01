def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes")
                exit(0)
    print("No")

if __name__ == "__main__":
    main()