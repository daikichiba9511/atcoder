#include <bits/stdc++.h>
using namespace std;

int main()
{
    double p;
    cin >> p;
    double x = -1.5 * log2(1.5 / (p * log(2.0)));
    if (x < 0.0)
        cout << p << endl;
    else
    {
        double total = x + p * pow(2, -(x / 1.5));
        cout << fixed << setprecision(10) << total << endl; // 表示桁数を10桁に
    }
}