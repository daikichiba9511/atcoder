#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>

using ll = long long;
// -- Macros
#define rep(i, n) for (ll i = 0; i < (n); ++i)
// -- Constants
const std::chrono::duration<double> TIME_LIMIT(1.9);
// const std::chrono::duration<double> TIME_LIMIT(20);
const int START_TEMP = 100;                  // 初期温度
const int END_TEMP = 5;                      // 終了温度
const int DIFF_TEMP = START_TEMP - END_TEMP; // 温度差
// -- Functions
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

unsigned int randxor() {
  static unsigned int x = 123456789, y = 362436069, z = 521288629, w = 88675123;
  unsigned int t = x ^ (x << 11);
  x = y;
  y = z;
  z = w;
  w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
  return w;
}

double calc_temp(const std::chrono::steady_clock::time_point &start) {
  // 時間経過に応じて温度を計算
  const auto elapsed = std::chrono::steady_clock::now() - start;
  return START_TEMP + (END_TEMP - START_TEMP) * elapsed / TIME_LIMIT;
}

// --
struct Input {
  int d;
  std::vector<std::vector<int>> s;
  std::vector<int> c;

  Input(int d, const std::vector<std::vector<int>> &s,
        const std::vector<int> &c)
      : d(d), s(s), c(c) {}
};

/* スコアを計算する関数
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
    t[i] = randxor() % 26; // 0から25の範囲でランダムに選ぶ
  }
  int score = compute_score(input, t);
  return State(t, score);
}

int evaluate_partial(const Input &input, const State &state, int change_day) {
  // change_day移行のみを再計算
  int score = state.score;
  // change_day未満の部分はstate.scoreに含まれているとしてchange_day移行の差分のみを計算

  std::vector<int> last(26, 0);
  for (int d = 0; d < change_day; ++d) {
    last[state.t[d]] = d + 1;
  }

  // change_day以降を再計算
  for (int d = change_day; d < input.d; ++d) {
    last[state.t[d]] = d + 1;
    for (int j = 0; j < 26; ++j) {
      score -= (d + 1 - last[j]) * input.c[j];
    }
    score += input.s[d][state.t[d]];
  }
  return score;
}

int evaluate(const Input &input, const State &state, const int k) {
  int score = 0;
  std::vector<int> last(26, 0);
  for (size_t d = 0; d < state.t.size(); ++d) {
    last[state.t[d]] = d + 1;
    for (int j = 0; j < 26; ++j) {
      score -= (d + 1 - last[j]) * input.c[j];
    }
    score += input.s[d][state.t[d]];
  }
  // k日目以降のスコアを計算
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
  const auto start = std::chrono::steady_clock::now();
  int steps = 0;
  while (true) {
    if (steps % 1000 == 0) {
      if (std::chrono::steady_clock::now() - start > TIME_LIMIT) {
        break; // 時間制限を超えたら終了
      }
    }
    ++steps;

    const int old_score = state.score;
    const double temp = calc_temp(start);
    const double temp_ratio = temp / START_TEMP;

    // int operatoration_type;
    // if (temp_ratio > 0.7) {
    //   operatoration_type = (randxor() % 10 < 4) ? 1 : 0; // 区間反転40%
    // } else if (temp_ratio > 0.3) {
    //   operatoration_type = randxor() % 3; // 均等
    // } else {
    //   operatoration_type = (randxor() % 10 < 7) ? 0 : 2; // 単一要素変更70%
    // }
    int operatoration_type = (randxor() % 10 < 7) ? 0 : 2; // 単一要素変更70%
    // int operatoration_type = randxor() % 3; // 均等に選ぶ

    if (operatoration_type == 0) {
      // 単一要素変更
      const int day = randxor() % d;
      const int type = randxor() % 26;
      const int old_type = state.t[day];
      state.t[day] = type;

      // state.score = evaluate_partial(input, state, day);
      // state.score = evaluate(input, state, 13);
      state.score = compute_score(input, state.t);
      const double prob = exp((state.score - old_score) / temp);
      const bool accept = prob > (double)(randxor() % 10000) / 10000.0;

      if (state.score < old_score && !accept) {
        state.t[day] = old_type;
        state.score = old_score;
      }
    } else if (operatoration_type == 1) {
      // 区間反転
      const int start_day = randxor() % d;
      const int end_day = start_day + randxor() % d;
      if (abs(start_day - end_day) > 16) {
        continue; // 反転する範囲が大きすぎる場合はスキップ
      }
      reverse(state.t.begin() + start_day,
              state.t.begin() + std::min(end_day, d));
      // state.score = evaluate_partial(input, state, start_day);
      // state.score = evaluate(input, state, 13);
      state.score = compute_score(input, state.t);

      const double prob = exp((state.score - old_score) / temp);
      const bool accept = prob > (double)(randxor() % 10000) / 10000.0;
      if (state.score < old_score && !accept) {
        reverse(state.t.begin() + start_day,
                state.t.begin() + std::min(end_day, d)); // 元に戻す
        state.score = old_score;
      }

    } else {
      // swap操作
      const int day1 = randxor() % d;
      const int day2 = randxor() % d;
      if (day1 != day2 && abs(day1 - day2) <= 16) {
        std::swap(state.t[day1], state.t[day2]);

        // state.score = evaluate_partial(input, state, std::min(day1, day2));
        // state.score = evaluate(input, state, 13);
        state.score = compute_score(input, state.t);

        const double prob = exp((state.score - old_score) / temp);
        const bool accept = prob > (double)(randxor() % 10000) / 10000.0;
        if (state.score < old_score && !accept) {
          std::swap(state.t[day1], state.t[day2]); // 元に戻す
          state.score = old_score;
        }
      }
    }
  }
  cerr << "Best score: " << compute_score(input, state.t) << endl;
  for (auto ti : state.t) {
    cout << (ti + 1) << "\n";
  }
  return 0;
  // Score: 109,376,304
}