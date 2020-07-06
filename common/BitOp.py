import math
import time

def fls_1(v):
    return int(math.log2(v))


t = [  0,  9,  1, 10, 13, 21,  2, 29, \
      11, 14, 16, 18, 22, 25,  3, 30, \
       8, 12, 20, 28, 15, 17, 24,  7, \
      19, 27, 23,  6, 26,  5,  4, 31]

def fls(v):
    global t
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    return t[((v * 0x07C4ACDD) & 0xffffffff) >> 27]


v = 1000
r0 = fls_1(v)
r1 = fls(v)
print('%d %d' %(r0, r1))


def run():
    start_time = time.time()
    for i in range(1, 20000):
        fls_1(i)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for i in range(1, 20000):
        fls(i)
    print("--- %s seconds ---" % (time.time() - start_time))

run()
