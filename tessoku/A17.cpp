#include <algorithm>
#include <iostream>
#include <vector>

using ll = long long;
// -- Macros
#define rep(i, n) for (ll i = 0; i < (n); ++i)

template <typename T> bool chmin(T &a, const T &b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template <typename T> bool chmax(T &a, const T &b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}

int main() {
  using namespace std;
  int n;
  cin >> n;
  vector<int> a(n - 1);
  rep(i, n - 1) cin >> a[i];
  vector<int> b(n - 2);
  rep(i, n - 2) cin >> b[i];

  // dp[i] := i番目の部屋に到達するまでの最小コスト
  vector<int> dp(n, 1e9);
  vector<int> prev(n, 0); // 前の部屋を記録するための配列
  dp[0] = 0;
  dp[1] = a[0];
  prev[1] = 0;
  for (int i = 2; i < n; ++i) {
    if (chmin(dp[i], dp[i - 1] + a[i - 1])) {
      prev[i] = i - 1; // 前の部屋は i - 1
    }
    if (chmin(dp[i], dp[i - 2] + b[i - 2])) {
      prev[i] = i - 2; // 前の部屋は i - 2
    }
  }

  // 経路を復元
  vector<int> path;
  for (int i = n - 1; i > 0; i = prev[i]) {
    path.push_back(i + 1); // 1-indexedにするため
  }
  path.push_back(1); // スタート地点を追加
  reverse(path.begin(), path.end());

  cout << path.size() << endl;
  for (int room : path) {
    cout << room << " ";
  }
  cout << endl;

  return 0;
}