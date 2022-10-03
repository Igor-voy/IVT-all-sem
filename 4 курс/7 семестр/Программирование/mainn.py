import main
import timeit
import math
import concurrent.futures as ftres
from functools import partial


def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):
    executor = ftres.ThreadPoolExecutor(max_workers = n_jobs)

    step = (b - a) / n_jobs
    fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    spawn_lst = []

    for i in fs:
        spawn = partial(executor.submit, main.integrate, f, i[0], i[1])
        spawn_lst.append(spawn)

    res = []
    for f in spawn_lst:
        res.append(f())

    s = [r.result() for r in ftres.as_completed(res)]

    return sum(s)


if __name__ == '__main__':
    print("Интеграл для 10**3")
    print(main.integrate(main.func, 0.8, 1.8, n_iter = 10**3))
    print("Время выполнения")
    print(timeit.timeit(stmt="integrate(func, 0.8, 1.8, n_iter = 1000)", setup="from main import integrate; from main import func", number = 10))
    print("")
    print("Интеграл для 10**4")
    print(main.integrate(main.func, 0.8, 1.8, n_iter = 10**4))
    print("Время выполнения")
    print(timeit.timeit(stmt="integrate(func, 0.8, 1.8, n_iter = 10000)", setup="from main import integrate; from main import func", number = 10))
    print("")
    print("Интеграл для 10**5")
    print(main.integrate(main.func, 0.8, 1.8, n_iter = 10**5))
    print("Время выполнения")
    print(timeit.timeit(stmt="integrate(func, 0.8, 1.8, n_iter = 100000)", setup="from main import integrate; from main import func", number = 10))
    print("") 
    print("*"*50)
    print("")
    print(main.integrate(main.func, 0.8, 1.8, n_iter = 10**5))
    print(timeit.timeit(stmt="integrate(func, 0.8, 1.8, n_iter = 100000)", setup="from main import integrate; from main import func", number = 10))

    print(integrate_async(main.func, 0.8, 1.8, n_iter = 10**5))
    print(timeit.timeit(stmt="integrate_async(func, 0.8, 1.8, n_iter = 100000)", setup="from mainn import integrate_async; from main import func", number = 10))