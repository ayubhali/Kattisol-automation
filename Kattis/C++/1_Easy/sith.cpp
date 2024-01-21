#include <iostream>
#include <string>
using namespace std;

int main() {
    string force_user;
    int a, b, result;

    getline(cin, force_user);
    cin >> a >> b >> result;

    if ((a - b) >= 0 && result == (a - b) && result == abs(a - b)) {
        cout << "VEIT EKKI" << endl;
    } 
    else if (result == a - b) {
        cout << "JEDI" << endl;
    } 
    else if (result == abs(a - b)) {
        cout << "SITH" << endl;
    } else {
        cout << "VEIT EKKI" << endl;
    }

    return 0;
}
