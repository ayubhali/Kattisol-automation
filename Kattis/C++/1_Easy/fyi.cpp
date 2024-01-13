#include <iostream>
using namespace std;

int main() 
{
    string phonenumber;

    cin >> phonenumber;

    if (phonenumber.substr(0, 3) == "555") {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
