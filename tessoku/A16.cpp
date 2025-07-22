#include <algorithm>
#include <iostream>
#include <vector>

using ll = long long;
// -- Macros
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
  using namespace std;
  int n;
  cin >> n;

  vector<int> a(n - 1);
  rep(i, n - 1) { cin >> a[i]; }

  vector<int> b(n - 2);
  rep(i, n - 2) { cin >> b[i]; }

  // dp[i] := i番目の部屋に到達するまでの最小コスト
  vector<int> dp(n, 1e9);
  dp[0] = 0;
  dp[1] = a[0];

  for (int i = 2; i < n; ++i) {
    dp[i] = min(dp[i - 1] + a[i - 1], dp[i - 2] + b[i - 2]);
  }
  cout << dp[n - 1] << '\n';

  return 0;
}