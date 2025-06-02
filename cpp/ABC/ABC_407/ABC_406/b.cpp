#include <bits/stdc++.h>

int main()
{
    int n, k;
    long long a;

    std::cin >> n >> k;

    // 桁数の計算
    long long m = 1;
    for (int i = 0; i < k; ++i)
    {
        m *= 10;
    }

    long long x = 1;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> a;

        // overflow対策
        if (a > ((m - 1) / x))
        {
            x = 1;
        }
        else
        {
            x *= a;
        }
    }
    std::cout << x << "\n";
    return 0;
}