#include <iostream>
using namespace std;

int main() {
    int numclass, available, needed;
    cin >> numclass >> available;

    int total_needed = 0;
    for (int i = 0; i < numclass; i++) {
        cin >> needed;
        total_needed += needed;
    }

    if (total_needed <= available) {
        cout << "Jebb" << endl; 
    } 
    else {
        cout << "Neibb" << endl; 
    }

    return 0;
}
