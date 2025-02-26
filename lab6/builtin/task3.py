def isPalindrome(s: str):
    length = len(s)
    for i, e in enumerate(s):
        if i == length-(i+1):
            return True
        if e != s[length-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    print(isPalindrome(input()))