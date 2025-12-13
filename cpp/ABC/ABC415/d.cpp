#include <algorithm>
#include <bitset>
#include <chrono>
#include <cmath>
#include <iostream>
#include <string>
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
  vector<int> a(m);
  vector<int> b(m);
  rep(i, m) cin >> a[i] >> b[i];
}