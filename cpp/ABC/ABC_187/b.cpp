#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> xy(N);
    for (auto& [x, y] : xy) cin >> x >> y;
    int ans = 0;
    for (int i = 0; i < N; ++i) for (int j = i + 1; j < N; ++j) {
        auto [x1, y1] = xy[i];
        auto [x2, y2] = xy[j];
        if (abs(y1 - y2) <= abs(x1 - x2)) ans++;
    }
    cout << ans << endl;
}