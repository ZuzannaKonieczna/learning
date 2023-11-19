class Lecture:
    def __init__(self, start, end, index):
        self.start = start
        self.end = end
        self.index = index

def choose_lectures(n, lectures):
    lectures.sort(key=lambda x: x.end)  # Sortujemy wykłady po czasie zakończenia
    chosen_lectures = []

    for i in range(n - 1):
        chosen_lectures.append(lectures[i])
        last_end_time = lectures[i].end
        j = i + 1

        # Szukamy kolejnych niekolidujących wykładów
        while j < n and lectures[j].start < last_end_time:
            j += 1

        if j < n:
            last_end_time = lectures[j].end

    # Dodaj ostatni wykład (o najpóźniejszym zakończeniu)
    chosen_lectures.append(lectures[-1])

    return chosen_lectures

def main():
    n = int(input())
    lectures = []

    for i in range(n):
        start, end = map(int, input().split())
        lectures.append(Lecture(start, end, i + 1))

    result = choose_lectures(n, lectures)

    # Wypisujemy wynik
    print(len(result))
    for lecture in result:
        print(lecture.index, end=' ')
        # Wybieramy dowolny niekolidujący wykład jako wykład zapasowy
        backup_lecture = next((x for x in lectures if x.index != lecture.index and (x.start >= lecture.end or x.end <= lecture.start)), None)
        if backup_lecture:
            print(backup_lecture.index)
        else:
            print(lecture.index)  # Jeśli nie znaleziono wykładu zapasowego, używamy tego samego wykładu

if __name__ == "__main__":
    main()
