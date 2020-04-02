import numpy as np


def solution(key, lock):
    answer = True

    def spin_key(key):
        M = len(key)
        new_key = [[0 for i in range(0, M)] for i in range(0, M)]

        for i in range(0, M):
            for j in range(0, M):
                new_key[j][M - i - 1] = key[i][j]

        return (new_key)

    def expand_array(lock, M, N):
        new_lock = [[0 for i in range(0, (M - 1) * 2 + N)] for i in range(0, (M - 1) * 2 + N)]

        for i in range(0, len(new_lock)):
            for j in range(0, len(new_lock)):
                if i >= M - 1 and i < len(new_lock) - (M - 1) and j >= M - 1 and j < len(new_lock) - (M - 1):
                    new_lock[i][j] = lock[i - (M - 1)][j - (M - 1)]

        return new_lock

    M = len(key)
    N = len(lock)

    new_lock = expand_array(lock, M, N)
    new_lock = np.array(new_lock)

    ones = np.ones((N, N))
    zeros = np.zeros((N, N))
    new_key = key.copy()
    for spin in range(0, 4):
        new_key = spin_key(new_key)
        for i in range(0, len(new_lock) - M + 1):
            for j in range(0, len(new_lock) - M + 1):
                new_lock2 = new_lock.copy()
                new_lock2[i:i + M, j:j + M] += new_key
                a = new_lock2[M - 1:M + N - 1, M - 1:M + N - 1] - ones
                if a.any() == zeros.any():
                    return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
