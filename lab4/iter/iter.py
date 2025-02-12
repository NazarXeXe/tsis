

class MyNumbersInfinite:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

class MyNumbersFinite:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

def generator():
    for i in range(4):
        yield i

def iterFunction():

    simple = iter( (0,1,2,3) )

    for i in simple:
        print(i)

def classBasedIterator():

    o = iter(MyNumbersInfinite())
    o1 = MyNumbersFinite()


    for i in range(4):
        print(next(o))

    for i in iter(o1):
        print(i)

def utils():

    simple = generator()

    print(sum(simple))
    print(
        list(filter(lambda x: x % 2 == 0, generator()))
    )

if __name__ == "__main__":
    fs = (
        iterFunction, utils, classBasedIterator
    )

    for f in fs:
        f()