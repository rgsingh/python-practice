"""Given a string s, find the length of the longest substring without duplicate characters."""

def length_longest2(s: str)-> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def length_longest(s: str) -> int:
    left_idx = 0
    max_sub = 0
    char_index = {}
    for right_idx, char in enumerate(s):
        if char in char_index and char_index[char] >= left_idx:
            left_idx = char_index[char] + 1
        char_index[char] = right_idx
        max_sub = max(max_sub, right_idx - left_idx + 1)
    return max_sub


def length_longest3(s: str) -> int:
    left_idx = 0
    char_index = {}
    max_len = 0

    for right_idx, c in enumerate(s):
        if c in char_index and char_index[c] >= left_idx:
            left_idx = char_index[c] + 1
        char_index[c] = right_idx
        max_len = max(max_len, right_idx - left_idx + 1)
    return max_len

if __name__ == '__main__':
    print(length_longest3("abcabcbbc"))
    print(length_longest3("bbbbb"))
    print(length_longest3("pwwkew"))
