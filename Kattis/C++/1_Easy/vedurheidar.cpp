#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    int windSpeed, n;
    cin >> windSpeed >> n; 

    vector<pair<string, int>> roads(n);

    for (int i = 0; i < n; i++) {
        cin >> roads[i].first >> roads[i].second;
    }

    for (auto road : roads) {
        if (windSpeed <= road.second) {
            cout << road.first << " opin" << endl;
        } else {
            cout << road.first << " lokud" << endl;
        }
    }

    return 0;
}
