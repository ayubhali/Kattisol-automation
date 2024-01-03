#include <iostream>
using namespace std;

int main()
{
    int a,b,c;

    cin >> a >> b >> c;

    int min_time = c - a - b;

    cout << min_time << endl;

    return 0;
}