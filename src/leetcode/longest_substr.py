"""Given a string s, find the length of the longest substring without duplicate characters."""


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


if __name__ == '__main__':
    print(length_longest("abcabcbbc"))
    print(length_longest("bbbbb"))
    print(length_longest("pwwkew"))
