def urlify (s):
    s = s.strip()
    s_list = s.split(' ')
    return '%20'.join(s_list)

def main ():
    s = raw_input('String: ')
    print urlify(s)

if __name__ == '__main__':
    main()