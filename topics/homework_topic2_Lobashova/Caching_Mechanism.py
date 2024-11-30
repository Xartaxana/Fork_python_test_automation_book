
from functools import lru_cache
import time

@lru_cache (maxsize=10)
def square(n):
    # Simulate an expensive computation
    time.sleep(2)
    return n**2

print(square(2))
print(square(3))
print(square(2))

#cache with dictionary:
cache = {}
def square2(n):
    if n not in cache:
        # Simulate an expensive computation
        time.sleep(2)
        cache[n] = n**2
    return cache[n]

print(square2(2))
print(square2(3))
print(square2(2))
print(cache)