#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double costPerSquareMeter, width, length, totalCost = 0;
    int numberOfLawns;

    cin >> costPerSquareMeter;

    cin >> numberOfLawns;

    for(int i = 0; i < numberOfLawns; i++) {
        cin >> width >> length;

        totalCost += width * length * costPerSquareMeter;
    }

    cout << fixed << setprecision(8) << totalCost << endl;

    return 0;
}
