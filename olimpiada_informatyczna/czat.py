from collections import defaultdict

def solve(n, k, a, b, S):
    S_prime = list(S)
    
    for i in range(n, b):
        R = S_prime[i - k:i]
        occurrences = defaultdict(int)
        
        for j in range(i - k, i):
            if S_prime[j:j + k] == R:
                next_char = S_prime[j + k]
                occurrences[next_char] += 1
        
        if occurrences:
            most_common_char = max(occurrences, key=occurrences.get)
        else:
            most_common_char = 'a'  # If R does not occur anywhere else, we assume c = a
        
        S_prime.append(most_common_char)

    result = ''.join(S_prime[a:b + 1])
    return result

# Input
n, k, a, b = map(int, input().split())
S = input()

# Solution
result = solve(n, k, a, b, S)

# Output
print(result)
