#include <iostream>
#include <vector>
#include <algorithm>

int search(int x, std::vector<int> &v) {
  int L = 0, R = v.size() - 1;
  while (L < R) {
    int M = (L + R) / 2;
    if (v[M] < x)
      L = M + 1;
    else
      R = M;
  }
  return L;
}

int main() {
  using namespace std;
  int n, x;
  cin >> n >> x;
  vector<int> v(n);
  for (int i = 0; i < n; ++i) {
    cin >> v[i];
  }
  sort(v.begin(), v.end());
  cout << search(x, v) + 1 << endl;
}