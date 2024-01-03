#include <iostream>
using namespace std;

int main()
{
    int year = 2022;
    int n;
    int k;

    cin >> n;
    cin >> k;

    int improvements = n/k;

    cout << year + improvements;

    return 0;
}