from re import compile, findall, sub
if __name__ == "__main__":
    a = input()    
    print(sub(compile('_.'), lambda anystr: anystr.group().upper(), a).replace('_', ''))