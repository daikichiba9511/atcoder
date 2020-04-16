def main():
    s = input()
    l = ["Sunny", "Cloudy", "Rainy"]
    idx = l.index(s)
    if idx == 2:
        print("Sunny")
        exit(0)
    print(l[idx+1])

if __name__ == "__main__":
    main()