#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int numqaly;

    cin >> numqaly;

    float q, y, accumulation = 0;   

    for (int i = 0; i < numqaly; i++) { 
        cin >> q >> y;
        accumulation += q * y;
    }
    cout << fixed << setprecision(3) << accumulation;

    return 0;
}