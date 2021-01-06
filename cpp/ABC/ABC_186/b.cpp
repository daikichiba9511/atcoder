#include <bits/stdc++.h>
using namespace std;
int INF = 1e+8;

bool is_more_than_min(int i, int min)
{
    return i > min;
}

int main()
{
    int H, W;
    cin >> H >> W;
    vector<vector<int>> v(H, vector<int>(W));
    for (auto &v_i : v) for (int i = 0; i < W; ++i) cin >> v_i[i];
    int min = INF;
    for (auto &v_i : v)
    {
        for (auto &v_ij : v_i)
            if (v_ij < min) min = v_ij;
    }
    int ans = 0;
    for (auto &v_i : v)
    {
        for (auto &v_ij : v_i)
            if (min < v_ij)
                ans += (v_ij - min);
    }
    cout << ans << endl;
}