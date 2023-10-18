<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zadanie - Wyniki</title>
</head>
<body>
    <h1>Wyniki Ankiety</h1>
    <hr>
    <?php
        if(isset($_POST['imie'])) {
            $imie = $_POST['imie'];
            $nazwisko = $_POST['nazw'];
            $plec = $_POST['plec'];
            $sport = isset($_POST['sport']) ? 'Tak' : 'Nie';
            $film = isset($_POST['film']) ? 'Tak' : 'Nie';
            $elektronika = isset($_POST['elektronika']) ? 'Tak' : 'Nie';
            $informatyka = isset($_POST['informatyka']) ? 'Tak' : 'Nie';
            $szkola = $_POST['szkola'];
            $o_sobie = $_POST['o_sobie'];

            echo "<p>Imię: $imie</p>";
            echo "<p>Nazwisko: $nazwisko</p>";
            echo "<p>Płeć: $plec</p>";
            echo "<p>Zainteresowania:</p>";
            echo "<ul>";
            echo "<li>Sport: $sport</li>";
            echo "<li>Film: $film</li>";
            echo "<li>Elektronika: $elektronika</li>";
            echo "<li>Informatyka: $informatyka</li>";
            echo "</ul>";
            echo "<p>Szkoła: $szkola</p>";
            echo "<p>Krótko o sobie:</p>";
            echo "<p>$o_sobie</p>";
        } else {
            echo "<p>Brak danych do wyświetlenia.</p>";
        }
    ?>
</body>
</html>
        