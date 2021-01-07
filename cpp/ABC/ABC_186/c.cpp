#include <bits/stdc++.h>
using namespace std;

string to_oct(int n)
{
    string s;
    while (n)
    {
        s = to_string(n%8) + s;
        n /= 8;
    }
    return s;
}

int main()
{
    int N;
    cin >> N;
    int cnt = 0;
    for (int i = 1; i <= N; ++i)
    {
        if (to_string(i).find("7") != std::string::npos || to_oct(i).find("7") != std::string::npos)
                continue;
        else cnt++;

    }
    cout << cnt << endl;
}