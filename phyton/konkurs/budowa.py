def can_place_runways(n, m, airport, k):
    for i in range(n):
        for j in range(n - k + 1):
            if all(airport[i][j + x] == '.' for x in range(k)):
                if m == 2:
                    if i + 1 < n and all(airport[i + 1][j + x] == '.' for x in range(k)):
                        return True
                else:
                    return True
    return False

def find_max_runway_length(n, m, airport):
    left, right = 1, n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_runways(n, m, airport, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


n, m = map(int, input().split())
airport = [input().strip() for _ in range(n)]


result = find_max_runway_length(n, m, airport)
print(result)
