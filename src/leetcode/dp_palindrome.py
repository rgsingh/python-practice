def longest_palindrome_dp(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Substrings of length 3 or more
    for length in range(3, n + 1):  # substring lengths
        for i in range(n - length + 1):
            j = i + length - 1  # end index
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length

    return s[start:start + max_len]


if __name__ == '__main__':
    print(longest_palindrome_dp("babad"))