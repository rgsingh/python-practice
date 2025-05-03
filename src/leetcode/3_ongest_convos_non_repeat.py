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


if __name__ == '__main__':
    print(longest_convo_sequence([
        "bro, you should try the punch.",
        "have you seen my cat?",
        "bro, you should try the punch.",
        "my dog is really a cat inside.",
        "have you seen my cat?",
        "man, i can't stand all of these people."
    ]))