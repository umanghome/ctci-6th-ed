def palindromable (s):
    s = s.lower()
    d = dict()
    for i in s:
        if not d.has_key(i):
            d[i] = 1
        else:
            d[i] = d[i] + 1
    odd = 0
    for (key, value) in d.items():
        if value % 2 == 1:
            odd = odd + 1
            if odd > 1:
                return False
    return True

def main ():
    s = raw_input('String: ')
    print str(palindromable(s))

if __name__ == '__main__':
    main()