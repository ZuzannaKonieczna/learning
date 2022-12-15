#include <iostream>

using namespace std;

int main()
{
    int pin , pieniadze;
    cout << "Witaj" << endl;
    cout << "Podaj pin ";
    cin >> pin ;

    if (pin == 2008){
        cout << "Ile pieniedzy chcesz wyplacic ";
        cin >> pieniadze ;
        cout << "Milego dnia" << endl;
    }
    else {
        cout << "zly pin " <<endl;
    }
    return 0;
}
