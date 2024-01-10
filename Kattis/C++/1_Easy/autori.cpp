#include <iostream>
#include <string>
using namespace std;

int main() {
    string input, result;
    cin >> input;

    result += input[0];

    for (int i = 1; i < input.length(); i++) {
        if (input[i] == '-') {
            result += input[i + 1];
        }
    }

    cout << result << endl;

    return 0;
}
