"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""
def steps(n: int) -> int:
    if n <= 1:
        print(f"1 >= {n}")
        return 1
    print(f"1 < {n}")
    return steps(n-1) + steps(n-2)


"""
Generalized and memoized for any number of steps allowed at a time

steps(4)
├── steps(3)
│   ├── steps(2)
│   │   ├── steps(1)
│   │   │   ├── steps(0) → 1      (base case)
│   │   │   └── steps(-1) → 0     (base case)
│   │   │   → return 1
│   │   │   → memo[1] = 1
│   │   └── steps(0) → 1          (base case)
│   │   → return 2
│   │   → memo[2] = 2
│   └── steps(1) → memo[1] HIT → 1
│   → return 3
│   → memo[3] = 3
└── steps(2) → memo[2] HIT → 2

→ return 5
→ memo[4] = 5

Memo Key	    When It's Set
memo[1] = 1	    After evaluating steps(0) and steps(-1) under steps(1)
memo[2] = 2	    After computing steps(1) and steps(0) under steps(2)
memo[3] = 3	    After computing steps(2) and steps(1) under steps(3)
memo[4] = 5	    After using memo[3] and memo[2] in steps(4)
"""
def steps(n: int, step_options: list[int], memo: dict=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        print(f"RETURN memo[{n}] = {memo[n]}")
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        return 1
    print(f"Computing steps({n})")
    memo[n] = sum(steps(n - step, step_options, memo) for step in step_options)
    print(f"SET memo[{n}] = {memo[n]}")
    return memo[n]


if __name__ == '__main__':
    print(steps(4, [1,2]))