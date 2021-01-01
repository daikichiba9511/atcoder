def main():
    a, b = input().split()
    if a < b:
        print(a * int(b))
    else:print(b * int(a))

if __name__ == "__main__":
    main()