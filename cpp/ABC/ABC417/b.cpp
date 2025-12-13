#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
#include <unordered_map>
#include <vector>

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
  int n, m;
  cin >> n >> m;
  vector<int> a(n), b(m);
  rep(i, n) cin >> a[i];
  rep(i, m) cin >> b[i];
  for (auto bi : b) {
    auto i = find(a.begin(), a.end(), bi);
    if (i != a.end()) {
      a.erase(i);
    }
  }
  for (auto ai : a) {
    cout << ai << " ";
  }
  cout << "\n";
}