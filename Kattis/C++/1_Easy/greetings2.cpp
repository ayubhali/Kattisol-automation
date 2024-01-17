#include <iostream>
#include <string>
using namespace std;

int main() {
    string message;
    cin >> message;

    for (int i = 0; i < message.length(); ++i) {
        if (message[i] == 'e') {
            message.insert(i, 1, 'e');
            i++; 
        }
    }

    cout << message << endl;

    return 0;
}
