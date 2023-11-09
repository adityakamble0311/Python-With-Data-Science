def get_matrix_input(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

rows1 = int(input("Enter the number of rows for the first matrix: "))
columns1 = int(input("Enter the number of columns for the first matrix: "))
print("Enter elements for the first matrix:")
matrix1 = get_matrix_input(rows1, columns1)

rows2 = int(input("Enter the number of rows for the second matrix: "))
columns2 = int(input("Enter the number of columns for the second matrix: "))

print("Enter elements for the second matrix:")
matrix2 = get_matrix_input(rows2, columns2)

while True:
    print("\nMatrix Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Transpose First Matrix")
    print("6. Transpose Second Matrix")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        if rows1 == rows2 and columns1 == columns2:
            result = []
            for i in range(rows1):
                row = []
                for j in range(columns1):
                    row.append(matrix1[i][j] + matrix2[i][j])
                result.append(row)
            print("Result of Addition:")
            print_matrix(result)
        else:
            print("Matrices must have the same dimensions for addition.")
    elif choice == '2':
        if rows1 == rows2 and columns1 == columns2:
            result = []
            for i in range(rows1):
                row = []
                for j in range(columns1):
                    row.append(matrix1[i][j] - matrix2[i][j])
                result.append(row)
            print("Result of Subtraction:")
            print_matrix(result)
        else:
            print("Matrices must have the same dimensions for subtraction.")
    elif choice == '3':
        print("Matrix multiplication is not supported without NumPy.")
    elif choice == '4':
        scalar = float(input("Enter a scalar value for division: "))
        result = []
        for i in range(rows1):
            row = []
            for j in range(columns1):
                row.append(matrix1[i][j] / scalar)
            result.append(row)
        print("Result of Division:")
        print_matrix(result)
    elif choice == '5':
        matrix1 = [[matrix1[j][i] for j in range(rows1)] for i in range(columns1)]  # Transpose the first matrix
        print("Transposed First Matrix:")
        print_matrix(matrix1)
    elif choice == '6':
        matrix2 = [[matrix2[j][i] for j in range(rows2)] for i in range(columns2)]  
        print("Transposed Second Matrix:")
        print_matrix(matrix2)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7).")
