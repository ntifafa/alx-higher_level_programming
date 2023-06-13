def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in range(len(matrix)):
            for element in range(len(matrix[row])):
                if element == len(matrix[row]) - 1:
                    print('{:d}'.format(matrix[row][element]))
                else:
                    print('{:d} '.format(matrix[row][element]), end='')
