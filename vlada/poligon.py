from typing import List


def f(a: int) -> List[int]:
    b = [i for i in range(a)]
    return b


b = f(5)
print(b)
