def isSubstring (string, pattern):
    try:
        index = string.index(pattern)
        return True
    except:
        return False

def isRotation (string, rotation):
    string = string + string
    return isSubstring(string, rotation)

def main ():
    a = raw_input('Is string 1: ')
    b = raw_input('a rotation of: ')
    print str(isRotation(b, a))

if __name__ == '__main__':
    main()