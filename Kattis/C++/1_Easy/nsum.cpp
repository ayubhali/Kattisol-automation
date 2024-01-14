#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int main()
{
    int nums, sum = 0;
    cin >> nums;
    
    vector<int> integers(nums);

    for (int i = 0; i < nums; i++) {
        cin >> integers[i];
    }

    sum = accumulate(integers.begin(), integers.end(), 0);

    cout << sum;

    return 0;
}