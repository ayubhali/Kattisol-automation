#include <iostream> 
using namespace std; 

int main() 
{ 
    int numtemps; 
    int count = 0;

    cin >> numtemps;

    int temp[numtemps]; 

    for (int i = 0; i < numtemps; i++) { 
        cin >> temp[i]; 
    
        if (temp[i] < 0) {
            count++;
        } 
    } 
    cout << count << endl;

    return 0; 
}