# user str
# class str
# function: palindrome
# min 3

class PalindromeChecker():
    def __init__(self, string):
        self.string = string
    def isPalindrome(self) -> bool:
        return True





if __name__ == "__main__":
    
    user = input('Enter: ')
    
    instance = PalindromeChecker(user)

    print( instance.isPalindrome() )


