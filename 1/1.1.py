def is_unique (s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True
    

def main ():
    s = raw_input('String: ')
    print str(is_unique(s))

if __name__ == '__main__':
    main()