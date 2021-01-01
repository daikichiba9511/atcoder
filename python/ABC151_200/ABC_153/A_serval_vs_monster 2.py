
def main():
    H, A = map(int, input().split())
    count = 0
    while True:
        H -= A
        count += 1
        if H <= 0:
            break

    print(count)





if __name__ == "__main__":
    main()