#include <iostream>
using namespace std;

int main() {
    unsigned int n, reversed = 0;
    cin >> n;

    while (n > 0) {
        reversed = (reversed << 1) | (n & 1); 
        n >>= 1; 
    }
    
    cout << reversed << endl;

    return 0;
}