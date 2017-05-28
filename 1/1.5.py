def one_removal_away (a, b):
    if len(a) == len(b):
        return False
    a = list(a)
    b = list(b)
    if len(a) > len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a

    for i in shorter:
        try:
            longer.remove(i)
        except:
            pass
    return len(longer) == 1

def one_update_away (a, b):
    if len(a) != len(b):
        return False
    a = set(a)
    b = set(b)
    return len(a.difference(b)) == 1

def one_edit_away (a, b):
    return one_removal_away(a, b) or one_update_away(a, b)

def main ():
    a = raw_input('String: ')
    b = raw_input('String: ')
    print str(one_edit_away(a, b))

if __name__ == '__main__':
    main()