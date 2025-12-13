#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using ll = long long;
// -- Macros
#define rep(i, n) for (ll i = 0; i < (n); ++i)
// -- Functions
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
  string s;
  cin >> s;
  // |S| <= 1000

  vector<int> t;
  rep(i, (int)s.size()) {
    if (s[i] == '#') {
      t.push_back(i + 1);
      if (t.size() == 2) {
        cout << t[0] << "," << t[1] << endl;
        t.clear();
      }
    }
  }
}