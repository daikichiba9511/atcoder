// #include <algorithm>
// #include <chrono>
// #include <cmath>
#include <iostream>
#include <unordered_map>
// #include <vector>

using ll = long long;
// -- Macros
#define rep(i, n) for (ll i = 0; i < (n); ++i)
// -- Functions
template <typename T>
bool chmin(T &a, const T &b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template <typename T>
bool chmax(T &a, const T &b) {
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
  unordered_map<int, int> cnt;
  ll ans = 0;
  rep(i, n) {
    int ai;
    cin >> ai;
    // j - a[j] = i + a[i] を満たす個数を加えていく
    ans += cnt[i - ai];
    cnt[i + ai]++;
  }
  cout << ans << "\n";
}