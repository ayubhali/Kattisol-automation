#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double P;
    cin >> P;

    double payoutOne = 100 / P;
    double payoutTwo = 100 / (100 - P);

    cout << fixed << setprecision(10);

    cout << payoutOne << endl;
    cout << payoutTwo << endl;

    return 0;
}
