#include <iostream>
#include <string>
using namespace std;

int main() {  
    string word;

    cin >> word;

    bool foundA = false;
    for (int i = 0; i < word.length(); i++) {
        if (word[i] == 'a') {
            foundA = true;
        }
        if (foundA) {
            cout << word[i];
        }
    }
    
    return 0;
}


