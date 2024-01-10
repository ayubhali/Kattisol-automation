#include <iostream>
#include <string>
using namespace std;

int main()
{
    int nums;
    cin >> nums; 

    string str[nums];

    for (int i = 0; i < nums; i++) {
        cin >> str[i];  
    }

    for (int j = 0; j < nums; j++) {
        if (j % 2 == 0) {
            cout << str[j] << endl;
        }
    }

    return 0;
}