def main():
    n = int(input())
    nums = [i for i in range(1, n+1)]
    print( ((len(nums) + 1) // 2) / len(nums) )

if __name__ == "__main__":
    main()