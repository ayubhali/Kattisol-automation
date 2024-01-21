#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string word;
    cin >> word;

    int countB = count(word.begin(), word.end(), 'b');
    int countK = count(word.begin(), word.end(), 'k');

    if (countB > countK) {
        cout << "boba" << endl;
    } 
    else if (countK > countB) {
        cout << "kiki" << endl;
    } 
    else if (countB == countK && countB != 0) {
        cout << "boki" << endl;
    } 
    else {
        cout << "none" << endl;
    }

    return 0;
}
