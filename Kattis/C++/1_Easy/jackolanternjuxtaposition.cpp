#include <iostream>
using namespace std;

int main()
{   
    int n, m = 1;

    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        m *=  arr[i];
    }

    cout << m;

    return 0;
}