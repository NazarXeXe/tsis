
if __name__ == "__main__":
    print("hello world")
    # Comment
    """
    Multi-line comment
    """
    var = 0
    print(var)
    var = "hi"
    print(var)


    types = [
        type(1),
        type(1.5),
        type("hi"),
        type( () ),
        type( range(0, 5) ),
        type( [] ),
        type( frozenset((1,2,3)) ),
        type( True ),
        type( None ),
        type( bytearray(1) ),
        type(memoryview( bytes(5) ))
    ]
    for t in types:
        print(t)

    # Casting
    print(int(1.5))
    print(float(1))
    print(int("10000"))

    # strings

    simple = 'Hi'
    formatted = f"{var} | hi"
    binary = b'Hi'
    multiline = '''
Hi
Hello
    '''
    multilineFormatted = f"""
{simple} {formatted}
    """
    print(
        simple,
        formatted,
        binary,
        multiline,
        multilineFormatted,
        sep='\n'
    )