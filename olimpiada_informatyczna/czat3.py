from collections import defaultdict

def extended_word(n, k, a, b, s):
    s_prime = s
    occurrences = defaultdict(list)

    for i in range(n - k):
        r = s_prime[i:i + k]
        next_letter = s_prime[i + k]
        occurrences[r].append(next_letter)

    for _ in range(b - n + 1):
        r = s_prime[-k:]
        next_letter_options = occurrences[r][-1]
        s_prime += min(next_letter_options)

    return s_prime[a - 1:b]


n, k, a, b = map(int, input().split())
s = input()

result = extended_word(n, k, a, b, s)
print(result)
