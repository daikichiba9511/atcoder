#include <bits/stdc++.h>

int main()
{
    int N, A;
    std::cin >> N;
    std::set<int> s;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        s.insert(A);
    }

    std::cout << s.size() << "\n";
    for (auto s_i : s)
    {
        std::cout << s_i << " ";
    }
    return 0;
}