#include <cmath>
#include <iomanip>
#include <iostream>

/*
 * x^3 + x - k = 0
 * の解を求める
 */
bool is_ok(double x, double k) {
  double y = x * x * x + x;
  return y >= k;
}

int main() {
  using namespace std;
  // N<10^5
  double n;
  cin >> n;
  double ng = -1.0, ok = 100.0;
  while (abs(ok - ng) > 0.000001) {
    double mid = (ng + ok) / 2;
    if (is_ok(mid, n)) {
      ok = mid;
    } else {
      ng = mid;
    }
    // cout << "mid: " << mid << ", ok: " << ok << ", ng: " << ng << endl;
  }
  cout << fixed << setprecision(6) << ok << endl; // okが最小の値
}