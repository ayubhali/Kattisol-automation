#include <iostream>
#include <string>
using namespace std;

int main()
{
    int repeat = 3;
    string word;
    cin >> word;

    for (int i = 0; i < repeat; i++) {
        cout << word << " ";
    }   

    return 0;
}