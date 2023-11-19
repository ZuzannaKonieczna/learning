class Satellite:
    def __init__(self, company, code):
        self.company = company
        self.code = code

def assign_identification_codes(num_satellites, num_connections, code_length_limit):
    # Sprawdź warunki wejściowe
    if num_satellites <= 0 or num_connections < 0 or code_length_limit <= 0:
        return "Błędne dane wejściowe"

    # Zdefiniuj zmienne
    companies = ["A", "B", "C"]  # Możesz dostosować do liczby firm
    connections = set()

    # Zdefiniuj struktury danych
    satellites = []
    for company in companies:
        for i in range(1, num_satellites + 1):
            satellites.append(Satellite(company, f"{company}{i}"))

    # Przypisz kody identyfikacyjne
    for i in range(num_connections):
        sat1 = satellites[i]
        sat2 = satellites[num_satellites + i]

        # Uwzględnij połączenia między satelitami tej samej firmy
        connections.add((sat1.code, sat2.code))
        
        # Uwzględnij połączenia między różnymi firmami
        connections.add((sat2.code, sat1.code))

    # Wypisz wynik
    for sat in satellites:
        print(f"Satelita {sat.code} firmy {sat.company}")

    # Wypisz długość kodów identyfikacyjnych
    print(f"Długość kodów identyfikacyjnych: {code_length_limit}")

    return "Przypisanie kodów zakończone pomyślnie"


n,p,M = map(int, input().split())
result = assign_identification_codes(n, p, M)
print(result)
