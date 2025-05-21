

def reverse_array(A: list) -> list:
    N = len(A)

    for i in range(N // 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]

    return A



if __name__ == '__main__':
    print(reverse_array([1,2,5,7,4,6]))