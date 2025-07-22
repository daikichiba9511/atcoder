#include <algorithm>
#include <iostream>
#include <vector>
using ll = long long;
// -- Macros
#define rep(i, n) for (ll i = 0; i < (n); ++i)

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

struct Input {
  int d;
  std::vector<std::vector<int>> s;
  std::vector<int> c;

  Input(int d, const std::vector<std::vector<int>> &s,
        const std::vector<int> &c)
      : d(d), s(s), c(c) {}
};

/*
 * @param input 入力データ
 * @param out 出力データ. t[i] は i日目に選んだtype
 */
int compute_score(const Input &input, const std::vector<int> &out) {
  int score = 0;
  std::vector<int> last(26, 0);
  for (size_t d = 0; d < out.size(); ++d) {
    // type_iを選んだ日付dを記録しておく
    last[out[d]] = d + 1;
    // d日目が終わった時に、選ばれてないtype分スコアが減少する
    for (int j = 0; j < 26; ++j) {
      score -= (d + 1 - last[j]) * input.c[j];
    }
    score += input.s[d][out[d]];
    // std::cout << score << "\n";
  }
  return score;
}

int main() {
  using namespace std;
  int d;
  cin >> d;
  vector<int> c(26);
  rep(i, 26) cin >> c[i];
  vector<vector<int>> s(d, vector<int>(26));
  rep(i, d) rep(j, 26) cin >> s[i][j];
  vector<int> t(d);
  rep(i, d) cin >> t[i];
  int m;
  cin >> m;
  vector<pair<int, int>> dq(m);
  rep(i, m) { cin >> dq[i].first >> dq[i].second; }

  Input input(d, s, c);
  for (int &ti : t) {
    --ti; // 0-indexedに変換
  }
  for (const auto &q : dq) {
    int day = q.first - 1;               // 0-indexedに変換
    int type = q.second - 1;             // 0-indexedに変換
    int old_type = t[day];               // 元のtypeを保存
    t[day] = type;                       // 指定された日付にtypeを設定
    int score = compute_score(input, t); // スコアを計算
    // t[day] = old_type;                   // 元のtypeに戻す
    std::cout << score << "\n"; // スコアを出力
  }
}
