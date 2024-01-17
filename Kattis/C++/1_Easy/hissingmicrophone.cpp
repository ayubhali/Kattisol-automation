#include <iostream>
#include <string>
using namespace std;

int main()
{
    string letter;
    cin >> letter;

    for (int i = 0; i < letter.size(); i++) {
        if (letter[i] == 's') {
            if (letter[i + 1] == 's') {
                cout << "hiss";
                return 0;
            }
        }
    }

    cout << "no hiss";

    return 0;
}