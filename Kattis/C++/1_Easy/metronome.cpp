#include <iostream>
#include <iomanip>  
using namespace std;

int main() {
    int ticks;

    cin >> ticks;

    cout << fixed << setprecision(2); 

    cout << ticks / 4.0 << endl;
    
    return 0;
}
