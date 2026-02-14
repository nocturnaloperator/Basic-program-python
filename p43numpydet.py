A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B)            # Matrix multiplication
print(np.transpose(A)) # Transpose
print(np.linalg.det(A))