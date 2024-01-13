#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> pieceset = {1,1,2,2,2,8};

    vector<int> input(6);

    vector<int> needed;

    for (int i = 0; i < 6; i++) {
        cin >> input[i];

        needed.push_back(pieceset[i] - input[i]); //take constants 
    }

    for (int i = 0; i < 6; i++) {
        cout << needed[i]  << " ";
    }

    return 0;
}