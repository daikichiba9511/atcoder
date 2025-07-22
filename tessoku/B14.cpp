#include <algorithm>
#include <cstddef>
#include <iostream>
#include <vector>

int main() {
  using namespace std;
  using ll = long long;

  int n, k;
  cin >> n >> k;
  vector<ll> a(n + 1);
  a[0] = 0;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i];
  }

  int mid = n / 2;

  // bit全探索で、冪集合を求める
  // N<=30なので、O(N^2)で 2**15 = 32768 = O(10^5) 個の組み合わせを求める
  vector<ll> p, l;
  for (int bit = 0; bit < (1 << mid); ++bit) {
    ll sum = 0;
    for (int i = 0; i < mid; ++i) {
      if (bit & (1 << i)) {
        sum += a[i + 1]; // a[0]は0なので、a[i + 1]を使う
      }
    }
    p.push_back(sum);
  }

  for (int bit = 0; bit < (1 << (n - mid)); ++bit) {
    ll sum = 0;
    for (int i = 0; i < n - mid; ++i) {
      if (bit & (1 << i)) {
        sum += a[i + mid + 1]; // a[0]は0なので、a[i + mid + 1]を使う
      }
    }
    l.push_back(sum);
  }

  for (auto &x : p) {
    cerr << x << " ";
  }
  cerr << endl;
  for (auto &x : l) {
    cerr << x << " ";
  }
  cerr << endl;

  sort(l.begin(), l.end());

  // pの各要素に対して、k-p[i]がlに存在するかを二分探索で調べる O(N^2 log N)
  for (size_t i = 0; i < p.size(); ++i) {
    int pos_i = lower_bound(l.begin(), l.end(), k - p[i]) - l.begin();
    if ((size_t)pos_i < l.size() && l[pos_i] == k - p[i]) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
  return 0;
}