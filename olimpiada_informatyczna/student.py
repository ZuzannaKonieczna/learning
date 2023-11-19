n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[1])
max_lectures = 0
end_time = 0

selected_lectures = []  
for lecture in l:
    if lecture[0] > end_time:
        max_lectures += 1
        end_time = lecture[1]
        selected_lectures.append(lecture)

print( max_lectures)
print("Wykłady na które można się wybrać:")
for lecture in selected_lectures:
    print(l.index(lecture))

