#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char str[1001];
    char str2[4] = "COV";

    cin.get(str, 1001);

    if (strstr(str, str2) != NULL) {
        cout << "Veikur!";
    }

    else {
        cout << "Ekki veikur!";
    }

    return 0;
}