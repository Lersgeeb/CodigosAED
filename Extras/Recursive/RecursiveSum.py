def recSumFirstN(n):
    if n == 0:
        return 0
    else:
        return recSumFirstN(n-1) + n
def main():
    x = int(input("Please enter a non-negative integer: "))
    s = recSumFirstN(x)

    print("The sum of the first", x, "integers is", str(s)+".")

if __name__ == "__main__":
    main()