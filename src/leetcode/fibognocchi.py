

def fibonocio(num: int, memo=None) -> int:

    if memo is None:
        memo = {}
    if num in memo: return memo[num]
    if num == 0: return 0
    if num == 1: return 1

    memo[num] = fibonocio(num - 1, memo) + fibonocio(num - 2, memo)
    return memo[num]

if __name__ == '__main__':
    print(fibonocio(8))


