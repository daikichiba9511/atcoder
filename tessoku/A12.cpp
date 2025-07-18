#include <iostream>
#include <vector>

/**
 * 答えがx以下かを判定して、Yesならtrueを返す
 *
 * @param x 判定する値. 何秒後か [s]
 * @param v 配列. 各要素はプリンターが１枚印刷するのにかかる時間[s/枚]
 * @param target 総和がtarget以上かどうか
 *
 * @return x以下ならtrue, それ以外はfalse
 */
bool check(long long x, std::vector<long long> &v, long long target) {
  long long n = v.size();
  long long sum = 0;
  for (long long i = 0; i < n; ++i) {
    sum += x / v[i];
  }
  if (sum >= target) {
    return true;
  } else {
    return false;
  }
}

int main() {
  using namespace std;
  long long n, k;
  cin >> n >> k;
  vector<long long> a(n);
  for (long long i = 0; i < n; ++i) {
    cin >> a[i];
  }

  // 何秒後にk枚以上の印刷がされるかを二分探索
  long long l = 0, r = 1'000'000'000;
  while (l < r) {
    long long mid = (l + r) / 2;
    bool ok = check(mid, a, k);
    if (ok) {
      r = mid; // 答えがmid以下なら、さらに小さい値
    } else {
      l = mid + 1; // 答えがmidより大きいなら、mid+1以上
    }
  }
  cout << l << endl; // lが最小の値
  return 0;
}