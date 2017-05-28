def print_matrix (matrix):
    for i in matrix:
        print i

def rotate (matrix):
    _matrix = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        _matrix[i] = list(matrix[i])
    n = len(matrix)
    for i in range(n / 2):
        top = _matrix[i]
        bottom = _matrix[n - 1 - i]
        for j in (range(i, n - i)[::-1]):
            # left to bottom
            matrix[n - 1 - i][j] = _matrix[j][i]
            # top to left
            matrix[j][i] = top[n - 1 - j]
        for j in (range(i, n - i)):
            # right to top
            matrix[i][j] = _matrix[j][n - 1 - i]
            # bottom to right
            matrix[j][n - 1 - i] = bottom[n - 1 - j]
    return matrix


def main ():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
    print 'Before rotation:'
    print_matrix(matrix)
    rotated = rotate(matrix)
    print 'After rotation:'
    print_matrix(rotated)

if __name__ == '__main__':
    main()