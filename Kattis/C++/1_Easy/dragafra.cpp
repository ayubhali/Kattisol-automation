#include <iostream>
using namespace std;

int main()
{
    int windows;
    int curtains;
    int covered;

    cin >> windows >> curtains;

    covered = windows - curtains;

    cout << covered;

    return 0;
}