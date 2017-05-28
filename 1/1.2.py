def is_permutation (a, b):
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    return a == b

def main ():
    a = raw_input('String: ')
    b = raw_input('String: ')
    print str(is_permutation(a, b))

if __name__ == '__main__':
    main()