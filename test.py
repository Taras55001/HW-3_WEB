from multiprocessing import Pool, cpu_count, freeze_support
from time import time

def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(n, *number):
    pool = Pool(processes=n)
    results = pool.map(factorize_number, number)
    pool.close()
    pool.join()
    return results

if __name__ == '__main__':
    freeze_support()
    n = cpu_count()
    
    for i in range(1,n):
        start_time = time()
        a, b, c, d = factorize(i, 128, 255, 99999, 10651060)
        end_time = time()

        execution_time = end_time - start_time
        print("Parallel execution time:", execution_time)


    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
