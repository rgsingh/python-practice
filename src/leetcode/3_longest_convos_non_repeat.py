"""Given a sequence of people you meet in a room from when you enter to the last person you meet,
find the number of the conversations initiated by each person in a sequence of people where there are no repeats"""


def longest_convo_sequence(convos: list[str]) -> int:
    max_len = 0
    l_convo_idx = 0
    convo_index = {}

    for r_convo_idx, convo in enumerate(convos):
        if convo in convo_index and convo_index[convo] >= l_convo_idx:
            l_convo_idx = convo_index[convo] + 1  # shrink the window
        convo_index[convo] = r_convo_idx
        max_len = max(max_len, r_convo_idx - l_convo_idx + 1)

    return max_len

def longest_convo_sequence2(convos: list[str]) -> int:
    left_idx = 0
    convo_idx = {}
    max_len = 0

    for right_idx, convo in enumerate(convos):
        if convo in convo_idx and convo_idx[convo] >= left_idx:
            left_idx = convo_idx[convo] + 1
        convo_idx[convo] = right_idx
        max_len = max(max_len, right_idx - left_idx + 1)

    return max_len

def longest_convo_sequence3(convos: list[str]) -> str:
    left = 0
    seen = set()
    max_len = 0

    for right in range(len(convos)):
        while convos[right] in seen:
            left += 1
            seen.remove(convos[left])
        seen.add(convos[right])
        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == '__main__':
    print(longest_convo_sequence([
        "bro, you should try the punch.",
        "have you seen my cat?",
        "bro, you should try the punch.",
        "my dog is really a cat inside.",
        "have you seen my cat?",
        "man, i can't stand all of these people."
    ]))

    print(longest_convo_sequence([
        "mommy?",
        "mommy?",
        "bruh, sup?",
        "hey, my man!",
        "bruh, sup?",
    ]))


    print(longest_convo_sequence3([
        "bro, you should try the punch.",
        "have you seen my cat?",
        "bro, you should try the punch.",
        "my dog is really a cat inside.",
        "have you seen my cat?",
        "man, i can't stand all of these people."
    ]))

    print(longest_convo_sequence3([
        "mommy?",
        "mommy?",
        "bruh, sup?",
        "hey, my man!",
        "bruh, sup?",
    ]))

