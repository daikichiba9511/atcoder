
#include <bits/stdc++.h>

template <typename T>
void dbgp(const T &v)
{
    std::cerr << v;
}

template <typename T>
void dbgp(const std::vector<T> &v)
{
    std::cerr << "[";
    for (size_t i = 0; i < v.size(); ++i)
    {
        dbgp(v[i]);
        if (i < v.size() - 1)
        {
            std::cerr << ", ";
        }
    }
    std::cerr << "]";
}

template <typename T>
void dbgp(const std::vector<std::vector<T>> &v)
{
    std::cerr << "[\n";
    for (size_t i = 0; i < v.size(); ++i)
    {
        std::cerr << "  ";
        dbgp(v[i]);
        if (i < v.size() - 1)
        {
            std::cerr << ",";
        }
        std::cerr << "\n";
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
    int n;
    std::cin >> n;
    std::string row;
    std::vector<std::vector<std::string>> s(n, std::vector<std::string>(n));
    std::vector<std::vector<std::string>> t(n, std::vector<std::string>(n));
    for (int i = 0; i < n; ++i)
    {
        std::cin >> row;
        for (int j = 0; j < n; ++j)
        {
            s[i][j] = row[j];
        }
    }
    for (int i = 0; i < n; ++i)
    {
        std::cin >> row;
        for (int j = 0; j < n; ++j)
        {
            t[i][j] = row[j];
        }
    }
    dbg(s);
    dbg(t);
    return 0;
}