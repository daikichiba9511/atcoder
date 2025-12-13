#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
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
  int n, x;
  cin >> n;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  cin >> x;

  for (auto ai : a) {
    if (ai == x) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
  return 0;
}