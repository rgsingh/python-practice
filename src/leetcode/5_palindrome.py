# incomplete and broken
def palindromes(raw_input: str) -> list[str]:
    matches = []
    depth = 0

    for right_idx, curr_char in enumerate(raw_input):
        look_left = raw_input[right_idx - 1] if right_idx > 0 else None
        look_right = raw_input[right_idx + 1] if right_idx < len(raw_input) - 1 else None
        if look_left == look_right:
            depth += 1
            match = raw_input[right_idx - 1:right_idx + 1]
            matches.append(match)
            print(depth)

    return matches


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
