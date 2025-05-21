def longest_palindrome(s: str) -> str:
    result = ""

    for i in range(len(s)):
        # Odd-length palindromes (centered on a single char)
        odd = expand_from_center(s, i, i)
        if len(odd) > len(result):
            result = odd

        # Even-length palindromes (centered on a pair)
        even = expand_from_center(s, i, i + 1)
        if len(even) > len(result):
            result = even

    return result


def expand_from_center(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


if __name__ == '__main__':
    print(longest_palindrome("aabbacdc"))
