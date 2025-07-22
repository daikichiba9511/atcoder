#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  using namespace std;
  int n, k;
  cin >> n >> k;
  vector<int> a(n), b(n), c(n), d(n);
  vector<int> p(n * n), q(n * n);
  for (int i = 0; i < n; ++i)
    cin >> a[i];
  for (int i = 0; i < n; ++i)
    cin >> b[i];
  for (int i = 0; i < n; ++i)
    cin >> c[i];
  for (int i = 0; i < n; ++i)
    cin >> d[i];

  // 半分全列挙
  // P, Qを作っていく
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      p[i * n + j] = a[i] + b[j];
      q[i * n + j] = c[i] + d[j];
    }
  }

  // Qをソート
  sort(q.begin(), q.end());

  // 二分探索
  for (int i = 0; i < n * n; ++i) {
    // qの中にk-p[i]が存在するかどうかをO(log N)で調べる
    int pos_i = lower_bound(q.begin(), q.end(), k - p[i]) - q.begin();
    if (pos_i < n * n && q[pos_i] == k - p[i]) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;

  return 0;
}