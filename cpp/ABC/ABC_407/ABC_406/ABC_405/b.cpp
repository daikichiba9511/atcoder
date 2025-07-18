#include <bits/stdc++.h>

template <typename T>
void dbgp(const T &v)
{
    std::cerr << v << "\n";
}

template <typename T>
void dbgp(const std::vector<T> &v)
{
    std::cerr << "[";
    for (size_t i = 0; i < v.size(); ++i)
    {
        std::cerr << v[i];
        if (i < v.size() - 1)
        {
            std::cerr << ", ";
        }
    }
    std::cerr << "]";
}

#define dbg(x)                                 \
    do                                         \
    {                                          \
        std::cerr << "[DBG]: " << #x << " = "; \
        dbgp(x);                               \
        std::cerr << "\n";                     \
    } while (0)

int main()
{
    int n, m;
    std::cin >> n >> m;
    std::map<int, int> freq;
    std::vector<int> a;
    for (int i = 0; i < n; ++i)
    {
        int ai;
        std::cin >> ai;
        a.push_back(ai);
        ++freq[ai];
    }

    if (static_cast<int>(freq.size()) != m)
    {
        std::cout << 0 << "\n";
        return 0;
    }

    std::reverse(a.begin(), a.end());

    int cnt = 0;
    for (auto ai : a)
    {
        ++cnt;
        --freq[ai];
        if (freq[ai] == 0)
        {
            break;
        }
    }

    std::cout << cnt << "\n";

    return 0;
}