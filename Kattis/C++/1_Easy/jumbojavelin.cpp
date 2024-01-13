#include <iostream>
using namespace std;

int main()
{   
    int numrods, netlength, sum = 0;
    cin >> numrods;

    int rodlengths;

    for (int i = 0; i < numrods; i++) {
        cin >> rodlengths;
        sum += rodlengths;
    }

    netlength = sum - (numrods - 1);

    cout << netlength;

    return 0;
}