#include <iostream>
#include <cstdlib>
#include <iomanip>

int main()
{
    int x, y;
    std::cin >> x >> y;
    // std::cout << x << " " << y;

    const int total = 36;
    // 36通りを全探索
    int a = 0;
    for (int i = 1; i <= 6; i++)
    {
        for (int j = 1; j <= 6; j++)
        {
            if ((i + j < x) && (std::abs(i - j) < y))
            {
                ++a;
            }
        }
    }
    double pa = static_cast<double>(a) / total;
    std::cout << std::fixed << std::setprecision(20) << 1 - pa << "\n";
    return 0;
}