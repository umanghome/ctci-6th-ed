def compress (s):
    if len(s) < 2:
        return s
    c = s[0]
    prev = s[0]
    counter = 1
    for i in s[1:]:
        if i == prev:
            counter = counter + 1
        else:
            c = c + str(counter) + i
            counter = 1
            prev = i
    c = c + str(counter)
    if len(c) < len(s):
        return c
    else:
        return s

def main ():
    s = raw_input('String: ')
    print compress(s)

if __name__ == '__main__':
    main()