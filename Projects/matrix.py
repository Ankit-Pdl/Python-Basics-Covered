"""
Matrix Operations in Python
Supports: addition, subtraction, multiplication, transpose,
          determinant, inverse, scalar operations, and more.
"""


def create_matrix(rows, cols, fill=0):
    """Create a matrix filled with a default value."""
    return [[fill] * cols for _ in range(rows)]


def display(matrix, label="Matrix"):
    """Pretty-print a matrix."""
    print(f"\n{label}:")
    for row in matrix:
        print("  [" + "  ".join(f"{val:8.3f}" for val in row) + " ]")


def shape(matrix):
    """Return (rows, cols) of a matrix."""
    return len(matrix), len(matrix[0])


def add(A, B):
    """Element-wise addition of two matrices."""
    r, c = shape(A)
    assert shape(A) == shape(B), "Matrices must have the same shape for addition."
    return [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]


def subtract(A, B):
    """Element-wise subtraction of two matrices."""
    r, c = shape(A)
    assert shape(A) == shape(B), "Matrices must have the same shape for subtraction."
    return [[A[i][j] - B[i][j] for j in range(c)] for i in range(r)]


def scalar_multiply(A, k):
    """Multiply every element of a matrix by a scalar."""
    return [[A[i][j] * k for j in range(len(A[0]))] for i in range(len(A))]


def multiply(A, B):
    """Standard matrix multiplication (dot product)."""
    rA, cA = shape(A)
    rB, cB = shape(B)
    assert cA == rB, f"Cannot multiply: shapes {rA}×{cA} and {rB}×{cB} are incompatible."
    result = create_matrix(rA, cB)
    for i in range(rA):
        for j in range(cB):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(cA))
    return result


def transpose(A):
    """Transpose a matrix (flip rows and columns)."""
    r, c = shape(A)
    return [[A[i][j] for i in range(r)] for j in range(c)]


def identity(n):
    """Return an n×n identity matrix."""
    mat = create_matrix(n, n)
    for i in range(n):
        mat[i][i] = 1
    return mat


def determinant(A):
    """Compute the determinant of a square matrix using cofactor expansion."""
    n, m = shape(A)
    assert n == m, "Determinant is only defined for square matrices."
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0
    for col in range(n):
        minor = [[A[i][j] for j in range(n) if j != col] for i in range(1, n)]
        det += ((-1) ** col) * A[0][col] * determinant(minor)
    return det


def get_minor(A, row, col):
    """Return the minor matrix by removing a specific row and column."""
    return [[A[i][j] for j in range(len(A[0])) if j != col]
            for i in range(len(A)) if i != row]


def inverse(A):
    """Compute the inverse of a square matrix using the adjugate method."""
    n, _ = shape(A)
    assert n == _, "Inverse is only defined for square matrices."
    det = determinant(A)
    assert det != 0, "Matrix is singular (determinant = 0); inverse does not exist."

    if n == 1:
        return [[1 / A[0][0]]]

    # Build cofactor matrix
    cofactors = [[
        ((-1) ** (i + j)) * determinant(get_minor(A, i, j))
        for j in range(n)
    ] for i in range(n)]

    
    adj = transpose(cofactors)

    return [[adj[i][j] / det for j in range(n)] for i in range(n)]


def hadamard(A, B):
    """Element-wise (Hadamard) product of two matrices."""
    r, c = shape(A)
    assert shape(A) == shape(B), "Matrices must have the same shape for Hadamard product."
    return [[A[i][j] * B[i][j] for j in range(c)] for i in range(r)]


def trace(A):
    """Sum of elements on the main diagonal."""
    n, m = shape(A)
    assert n == m, "Trace is only defined for square matrices."
    return sum(A[i][i] for i in range(n))


def frobenius_norm(A):
    """Frobenius norm: sqrt of sum of squares of all elements."""
    return sum(A[i][j] ** 2 for i in range(len(A)) for j in range(len(A[0]))) ** 0.5



if __name__ == "__main__":
    print("=" * 55)
    print("         MATRIX OPERATIONS DEMO")
    print("=" * 55)

    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    C = [[2, -1, 0],
         [1,  3, 2],
         [0,  1, 4]]

    display(A, "Matrix A")
    display(B, "Matrix B")
    display(C, "Matrix C (invertible)")

    display(add(A, B),           "A + B")
    display(subtract(A, B),      "A - B")
    display(scalar_multiply(A, 3),"A × 3 (scalar)")
    display(multiply(A, B),      "A × B (dot product)")
    display(transpose(A),        "Transpose of A")
    display(hadamard(A, B),      "A ⊙ B (Hadamard product)")
    display(identity(3),         "3×3 Identity Matrix")

    print(f"\nTrace of A          : {trace(A):.3f}")
    print(f"Determinant of A    : {determinant(A):.3f}")
    print(f"Frobenius norm of A : {frobenius_norm(A):.3f}")

    det_C = determinant(C)
    print(f"\nDeterminant of C    : {det_C:.3f}")
    if det_C != 0:
        inv_C = inverse(C)
        display(inv_C, "Inverse of C")
        display(multiply(C, inv_C), "C × C⁻¹ (should be Identity)")