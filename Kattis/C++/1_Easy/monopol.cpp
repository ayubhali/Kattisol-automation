#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() 
{
    int n, distance;
    cin >> n; 

    int count = 0;

    vector<int> possibleSums = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    vector<int> waysToSum = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1};

    for (int i = 0; i < n; i++) {
        cin >> distance; // Read each hotel's distance
        for (int j = 0; j < possibleSums.size(); ++j) {
            if (distance == possibleSums[j]) {
                count += waysToSum[j]; 
                break;
            }
        }
    }

    double probability =  (double) (count) / 36.0;

    cout << fixed << setprecision(17);
    cout << probability << endl;

    return 0;
}
