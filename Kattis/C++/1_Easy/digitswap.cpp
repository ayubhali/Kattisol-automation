#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    string num;
    cin >> num;

    swap(num[0], num[1]);

    cout << num << endl;

    return 0;
}