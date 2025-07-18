#include <bits/stdc++.h>

int main() {
  using namespace std;
  int n, q;
  cin >> n;
  vector<int> v(n);
  for (int i = 0; i < n; ++i) {
    cin >> v[i];
  }
  cin >> q;
  sort(v.begin(), v.end());

  for (int i = 0; i < q; ++i) {
    int x;
    cin >> x;
    int pos = lower_bound(v.begin(), v.end(), x) - v.begin();
    cout << pos << endl;
  }
}