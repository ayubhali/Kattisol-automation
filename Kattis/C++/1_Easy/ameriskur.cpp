#include <iostream>
#include <iomanip> 
using namespace std;

int main()
{
    double footballfield = 0.09144;
    int num;
    double result;

    cin >> num;

    result = footballfield * num;

    cout << setprecision(17) << result << endl;

    return 0;
}