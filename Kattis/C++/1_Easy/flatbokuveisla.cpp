#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    int leftover;
    
    leftover = n % m;

    cout << leftover;

    return 0;
}