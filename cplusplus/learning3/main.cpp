#include <iostream>

using namespace std;

string login, haslo;

int main()
{
    cout << "Podaj login: ";
    cin >> login;
    cout << "Podaj haslo: ";
    cin >> haslo;

    if ((login == "zuz") && (haslo == "mom"))
    {
        cout << "Dane sa poprawne";
    }

    else
    {
        cout << "Zly login lub haslo";
    }
    return 0;
}
