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
  int t;
  cin >> t;
  rep(i, t) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    s = "0" + s; // 1-indexedにするため先頭に0を追加
    vector<int> ok(1 << n, 0);
    ok[0] = 1; // 初期状態は到達可能
    rep(i, (1 << n)) {
      if (ok[i] == 0)
        continue; // 到達不可能な状態はスキップ
      // 状態iのbit列を調べる
      rep(j, n) {
        if (i & (1 << j))
          continue; // j番目のビットが立っている場合は危険な状態になってしまうのでスキップ
        // 状態iから、j番目のビットを立てることでj番目の薬品を選べるか調べる
        int next = i | (1 << j); // ORをとって、j番目のビットを立てる.
        if (s[next] == '0')
          ok[next] = 1;
      }
    }
    // 最終的に状態iからjを選べるか調べるのを
    // i=(1 << n) - 1まで調べた結果遷移できるルートがあるのならYes
    if (ok[(1 << n) - 1]) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }
  return 0;
}