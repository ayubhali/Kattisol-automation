#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int g, t, n;
    cin >> g >> t >> n;

    int remaining_capacity = g - t;
    int max_trailer_weight = remaining_capacity * 90 / 100; 

    vector<int> weight(n); 

    int total_weight_of_items = 0;
    for (int i = 0; i < n; i++) {
        cin >> weight[i];
        total_weight_of_items += weight[i];
    }

    int max_possible_trailer_weight = max_trailer_weight - total_weight_of_items;
    cout << max_possible_trailer_weight << endl;

    return 0;
}
