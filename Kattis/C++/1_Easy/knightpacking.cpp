#include <iostream>
using namespace std;

int main()
{
    int boardsize;

    cin >> boardsize;

    if (boardsize % 2 == 1) {
        cout << "first";
    }

    else {
        cout << "second";
    }

    return 0;
}