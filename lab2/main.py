
def booleans():
    def example1():
        print(10 > 9)
        print(10 == 9)
        print(10 < 9) 

    def example2():
        a = 200
        b = 33

        if b > a:
            print("b is greater than a")
        else:
            print("b is not greater than a")

    def example3():
        print(bool("Hello"))
        print(bool(15))
    
    def example4():
        x = "Hello"
        y = 15

        print(bool(x))
        print(bool(y))
    
    def example5():
        bool("abc")
        bool(123)
        bool(["apple", "cherry", "banana"])

    def example6():
        class myclass():
            def __len__(self):
                return 0

        myobj = myclass()
        print(bool(myobj))
    
    def example7():
        def myFunction():
          return True
        print(myFunction())

    def example8():
        def myFunction():
            return True

        if myFunction():
            print("YES!")
        else:
            print("NO!")
    
    all = [ example1, example2, example3, example4, example5, example6, example7, example8 ]
    for f in all:
        print("-----------")
        f()
        print("-----------")


# == 	Equal 	x == y 	
# != 	Not equal 	x != y 	
# > 	Greater than 	x > y 	
# < 	Less than 	x < y 	
# >= 	Greater than or equal to 	x >= y 	
# <= 	Less than or equal to 	x <= y

# and  	Returns True if both statements are true 	x < 5 and  x < 10 	
# or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
# not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)

# is  	Returns True if both variables are the same object 	x is y 	
# is not 	Returns True if both variables are not the same object 	x is not y

# in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
# not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y

# &  	AND 	Sets each bit to 1 if both bits are 1 	x & y 	
# | 	OR 	Sets each bit to 1 if one of two bits is 1 	x | y 	
# ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1 	x ^ y 	
# ~ 	NOT 	Inverts all the bits 	~x 	
# << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off 	x << 2 	
# >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2

def ops():
    print((6 + 3) - (6 + 3)) 
    print(100 + 5 * 3) 

def lists():
    thisList = [ "apple", "banana", "cherry" ]
    def length():
        print(len(thisList))
    def exampleDataTypes():
        list1 = ["apple", "banana", "cherry"]
        list2 = [1, 5, 7, 9, 3]
        list3 = [True, False, False]
        list1 = ["abc", 34, True, 40, "male"]
    def listFunction():
        thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
        print(thislist)
    all = [ length, exampleDataTypes, listFunction ]
    for f in all:
        f()

# Immutable
def tuples():
    mytuple = ("apple", "banana", "cherry")
    print(mytuple)

def sets():
    myset = {"apple", "banana", "cherry"} # Cannot contain duplicates.
    print(myset)

# Key-Value pairs
def dicts():
    thisdict =	{ 
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)

def ifelsestatement():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")


def whileLoop():
    i = 0
    while i < 6: # run the code until conditions met.
        i += 1
        if i == 5:
            break # stop the loop completly.
        if i == 3:
            continue # skip iteration.
        print(i)


def forLoop():
    fruits = ["apple", "banana", "cherry"] # iterator
    for x in fruits: # Run the code until iterator ends.
        print(x)

if __name__ == "__main__":
    booleans()
    ops()
    lists()
    tuples()
    sets()
    dicts()
    ifelsestatement()
    whileLoop()
    forLoop()
