#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

int main() {
  using namespace std;

  int n;
  cin >> n;

  vector<int> a(n);
  vector<int> b(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    b[i] = a[i]; // bもaと同じ値を持つ
  }

  sort(b.begin(), b.end());
  map<int, int> value2rank;
  int current_rank = 1;
  for (int &bi : b) {
    if (!value2rank.contains(bi)) {
      value2rank[bi] = current_rank++;
    }
  }

  for (auto &ai : a) {
    cout << value2rank[ai] << " ";
  }
  cout << endl;
}