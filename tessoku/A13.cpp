#include <algorithm>
#include <iostream>
#include <vector>

int solve1() {
  using namespace std;
  using ll = long long;
  int n;
  ll k;
  cin >> n >> k;
  vector<ll> a(n);
  for (ll i = 0; i < n; ++i) {
    cin >> a[i];
  }

  ll ans = 0;
  for (ll i = 0; i < n; ++i) {
    ll j = lower_bound(a.begin(), a.end(), a[i] + k + 1) - a.begin();
    // cerr << "j: " << j - i - 1 << endl;
    ans += j - i - 1;
  }
  cout << ans << endl;
  return 0;
}

int solve2() {
  using namespace std;
  using ll = long long;

  int n;
  ll k;
  cin >> n >> k;
  vector<ll> a(n);
  for (ll i = 0; i < n; ++i) {
    cin >> a[i];
  }

  vector<ll> r(n);
  for (ll i = 0; i < n; ++i) {
    r[i] = 0;
  }

  for (ll i = 0; i < n; ++i) {
    // スタート地点を決める
    if (i == 0) {
      r[i] = 0;
    } else {
      r[i] = r[i - 1];
    }

    // ギリギリまで増やしていく
    while (r[i] < n && a[r[i]] - a[i] <= k) {
      ++r[i];
    }
  }

  ll ans = 0;
  for (ll i = 0; i < n; ++i) {
    ans += r[i] - i - 1;
    // cerr << r[i] - i - 1 << endl;
  }
  cout << ans << endl;
  return 0;
}

int main() {
  // solve1();
  solve2();
}