#include <iostream>
#include <string>
using namespace std;

int main() {
    int L, N, emptyCells = 0;
    cin >> L >> N;

    for (int i = 0; i < N; ++i) {
        string lane;
        cin >> lane;
        for (char cell : lane) {
            if (cell == '.') 
            emptyCells++;
        }
    }

    cout.precision(5);
    cout << (double)emptyCells / (L * N) << endl;

    return 0;
}
