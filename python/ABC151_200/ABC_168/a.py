def main():
    n = int(input())

    n = n % 10
    if n in [2, 4, 5, 7, 9]:
        print("hon")
    elif n == 3:
        print("bon")
    else:
        print("pon")
if __name__ == "__main__":
    main()