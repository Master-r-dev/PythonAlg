import numpy as np
from numpy import linalg as LA
def penrose_moore(X, eps=1e-10):
    # Метод Мура-Пенроуза
    m, n = X.shape
    err = np.inf
    ds = 1
    prev = X.T
    while err > eps:
        # @ - это матричное умножение
        current = np.linalg.lstsq((X.T @ X + ds * np.eye(n)), X.T, rcond=None)[0]
        err = np.linalg.norm(current - prev)
        prev = current
        ds = ds / 2
    return current

a = np.random.randint(0, 10, size = (3, 3))
print(a)
a_pinv = LA.pinv(a)
print(a_pinv) #функция вычисления библиотеки numpy.linalg
print(penrose_moore(a)) # моя функция
#  Проверим выполнение 1-го условия:
print(np.allclose(np.dot(a, np.dot(a_pinv, a)), a))
#  Проверим выполнение 2-го условия:
print(np.allclose(np.dot(a_pinv, np.dot(a, a_pinv)), a_pinv))
#  Проверим выполнение 3-го условия:
print(np.allclose(np.dot(a, a_pinv).T, np.dot(a, a_pinv)))
#  Проверим выполнение 4-го условия:
print(np.allclose(np.dot(a_pinv, a).T, np.dot(a_pinv, a)))