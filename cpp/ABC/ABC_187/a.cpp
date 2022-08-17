#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    int s_a = 0;
    int s_b = 0;
    for (int i = 0; i < 3; i++)
    {
        s_a += a % 10;
        s_b += b % 10;
        a /= 10;
        b /= 10;
    }
    if (s_a >= s_b)
        cout << s_a << endl;
    else
        cout << s_b << endl;
}
