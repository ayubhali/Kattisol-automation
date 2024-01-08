#include <iostream>
using namespace std;

int main()
{
    int stones;
    cin >> stones;

    if (stones % 2 == 0) {
        cout << "Bob";  
    }

    else {
        cout << "Alice";
    }

    return 0;
}