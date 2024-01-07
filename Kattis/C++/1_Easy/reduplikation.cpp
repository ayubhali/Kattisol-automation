#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
    int numtimes;

    cin >> str >> numtimes;

    for (int i = 0; i < numtimes; i++) {
        cout << str;
    }

    cout << endl;

    return 0;
}