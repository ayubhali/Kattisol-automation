#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n, w, h;
    cin >> n >> w >> h;

    double diagonal = sqrt(w * w + h * h);

    for(int i = 0; i < n; i++) {
        int length;
        cin >> length;

        if(length <= diagonal) {
            cout << "DA" << endl;
        } else {
            cout << "NE" << endl;
        }
    }

    return 0;
}
