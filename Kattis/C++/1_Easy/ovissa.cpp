#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int length;
    char str[100001];

    cin >> str;
    
    length = strlen((str));

    cout << length << endl;

    return 0;
}