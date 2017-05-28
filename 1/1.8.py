def print_matrix (matrix):
    for i in matrix:
        print i

def zeroes (matrix):
    n = len(matrix)
    m = len(matrix[0])

    _matrix = []
    for i in range(n):
        _matrix.append([None for i in range(m)])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(m):
                    _matrix[i][k] = 0
                for k in range(n):
                    _matrix[k][j] = 0

    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] is None:
                _matrix[i][j] = matrix[i][j]

    return _matrix

def main ():
    matrix = [[1, 2, 0, 4, 3], [5, 6, 7, 8, 6], [1, 0, 3, 4, 6], [5, 6, 7, 8, 9]]
    print 'Before zero-ization:'
    print_matrix(matrix)
    zero = zeroes(matrix)
    print 'After zero-ization:'
    print_matrix(zero)

if __name__ == '__main__':
    main()