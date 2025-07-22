#include <algorithm>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>

using ll = long long;
// -- Macros
#define rep(i, n) for (ll i = 0; i < (n); ++i)
std::mt19937 rng(42); // 固定シードで初期化
std::uniform_int_distribution<int> dist(0, 25);

// Constants
const std::chrono::duration<double> TIME_LIMIT(1.9);

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

struct State {
  std::vector<int> t;
  int score;

  State(const std::vector<int> &t, int score) : t(t), score(score) {}
};

State init(const Input &input) {
  std::vector<int> t(input.d); // 初期状態では全てのtypeを0に設定
  for (int i = 0; i < input.d; ++i) {
    // randomにtypeを選ぶ
    t[i] = dist(rng); // 0から25の範囲でランダムに選ぶ
  }
  int score = compute_score(input, t);
  return State(t, score);
}

int evaluate(const Input &input, const State &state, const int k) {
  int score = 0;
  std::vector<int> last(26, 0);
  for (size_t d = 0; d < state.t.size(); ++d) {
    last[state.t[d]] = d + 1;
    for (int j = 1; j < 26; ++j) {
      score -= (d + 1 - last[j]) * input.c[j];
    }
    score += input.s[d][state.t[d]];
  }
  for (int j = (int)state.t.size();
       j < std::min((int)state.t.size() + k, input.d); ++j) {
    for (int k = 0; k < 26; ++k) {
      score -= (j + 1 - last[k]) * input.c[k];
    }
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
  Input input = Input(d, s, c);

  State state = init(input);
  auto start = chrono::steady_clock::now();
  while (chrono::steady_clock::now() - start < TIME_LIMIT) {
    int day = rand() % d; // 0からd-1の範囲でランダムに日付を選ぶ
    int type = dist(rng);
    int old_type = state.t[day];             // 元のtypeを保存
    int old_score = state.score;             // 元のスコアを保存
    state.t[day] = type;                     // 指定された日付にtypeを設定
    state.score = evaluate(input, state, 5); // スコアを計算
    if (state.score < old_score) {
      // スコアが悪化した場合は元の状態に戻す
      state.t[day] = old_type; // 元のtypeに戻す
      state.score = old_score; // 元のスコアに戻す
    }
  }
  cerr << "Best score: " << compute_score(input, state.t) << endl;
  for (int ti : state.t) {
    cout << (ti + 1) % 27 << "\n";
  }
  return 0;
}