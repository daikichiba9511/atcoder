#include <bits/stdc++.h>
using namespace std;

std::string dec_to_bin_bit(int n) {
  if (n == 0) return "0";
  std::string bits;
  for (int mask = 1 << (sizeof(int) * 8 - 1); mask > 0; mask >>= 1) {
    if (n & mask) {
      bits += '1';
    } else if (!bits.empty()) {
      // 最上位の1が出るまで先頭の0をスキップ
      bits += '0';
    }
  }
  return bits;
}

int main() {
  double pi = acos(-1.0);
  double x = 30.0;
  printf("%.12lf\n", sin(x / 180.0 * pi));  // sin(pi / 6)
  printf("%.12lf\n", cos(x / 180.0 * pi));  // cos(pi / 6)

  double y = 60.0;
  printf("%.12lf\n", sin(y / 180.0 * pi));  // sin(pi / 3)
  printf("%.12lf\n", cos(y / 180.0 * pi));  // cos(pi / 3)

  printf("---------------------------------------\n");
  vector<double> angles = {30.0, 60.0, 90.0, 120.0, 150.0, 180.0};
  swap(angles[0], angles[1]);  // Swap 30 and 60 degrees
  printf("%.12lf %f\n", sin(angles[0] / 180.0 * pi), angles[0]);  // sin(pi / 6)

  // 最小公倍数
  int gcd = __gcd(30, 60);
  printf("%d %f\n", gcd, 30.0 / gcd * 60);  // LCM of 30 and 60 degrees

  // 乱数
  printf("%f\n", (double)rand() / RAND_MAX);  // Random number between 0 and 1

  // 時間計測
  int ti = clock();  // Start time measurement
  for (int i = 0; i < 1000000; ++i);
  int tf = clock() - ti;  // End time measurement
  printf("%d\n", tf);     // Print elapsed time

  vector<int> v = {1, 2, 3, 4, 5};
  reverse(v.begin(), v.end());  // Reverse the vector
  for (int i : v) {
    printf("%d ", i);  // Print reversed vector
  }
  printf("\n------------\n");
  // sort range is [l, r)
  reverse(v.begin() + 1, v.begin() + 3);  // Reverse back to original order
  for (int i : v) {
    printf("%d ", i);  // Print reversed vector
  }
  printf("\n------------\n");
  // ---- stack
  stack<int> st;
  st.push(1);
  st.push(2);
  st.push(3);

  while (!st.empty()) {
    printf("%d ", st.top());  // Print top element
    st.pop();                 // Remove top element
  }
  printf("\n------ queue ------\n");
  // --- queue
  queue<int> q;
  q.push(1);
  q.push(2);
  q.push(3);

  while (!q.empty()) {
    printf("%d ", q.front());  // Print front element
    q.pop();                   // Remove front element
  }
  printf("\n------ priority queue -------\n");
  // --- priority queue
  priority_queue<int> pq;
  pq.push(1);
  pq.push(3);
  while (!pq.empty()) {
    printf("%d ", pq.top());  // Print top element
    pq.pop();                 // Remove top element
  }
  printf("\n------ map -------\n");
  map<string, int> mp;
  mp["apple"] = 1;
  mp["banana"] = 2;
  mp["orange"] = 3;
  for (const auto &[key, value] : mp) {
    printf("%s: %d\n", key.c_str(), value);
  }
  printf("\n------ lower_bound -------\n");
  vector<int> arr = {10, 20, 30, 40, 50};
  cout << lower_bound(arr.begin(), arr.end(), 31) - arr.begin()
       << endl;  // Find the first position where 30 can be inserted

  printf("\n------ set -------\n");
  set<int> s;
  s.insert(1);
  s.insert(2);
  s.insert(3);
  s.insert(2);  // Duplicate insertion, will not change the set
  for (auto it = s.begin(); it != s.end(); ++it) {
    printf("%d ", *it);  // Print elements in the set
  }

  printf("\n----- pair -------\n");
  pair<int, string> p = {1, "apple"};
  printf("%d %s\n", p.first, p.second.c_str());  // Print pair

  printf("\n----- tuple -------\n");
  tuple<int, string, double> t = {1, "banana", 3.14};
  printf("%d %s %.2f\n", get<0>(t), get<1>(t).c_str(),
         get<2>(t));  // Print tuple

  printf("\n----- assert -------\n");
  assert(1 + 1 ==
         2);  // Check if the condition is true, if not, terminate the program
  //   assert(1 + 1 == 3); // This will cause the program to terminate

  printf("\n----- count -------\n");
  vector<int> a = {1, 2, 3, 4, 5, 1, 2, 1};
  printf("%ld\n", count(a.begin(), a.end(), 1));  // Count occurrences of 1

  printf("\n----- find -------\n");
  vector<int> b = {1, 2, 3, 4, 5};
  printf("%ld\n",
         find(b.begin(), b.end(), 3) - b.begin());  // Find position of 3

  printf("\n --- next_permutation ---\n");
  int n = 3;
  vector<int> v3 = {0, 1, 2};
  do {
    for (int i = 0; i < n; ++i) {
      printf("%d ", v3[i]);  // Print current permutation
    }
    printf("\n");
  } while (next_permutation(v3.begin(), v3.end()));

  printf("\n --- next_permutation (descending) ---\n");
  // 順列を生成する
  vector<int> v4 = {0, 1, 2};
  do {
    for (int i = 0; i < n; ++i) {
      printf("%d ", v4[i]);  // Print current permutation
    }
    printf("\n");
  } while (next_permutation(v4.begin(), v4.end(), [](int a, int b) {
    return a > b;
  }));  // Sort in descending order

  printf("\n --- __builtin_popcount ---\n");
  // 整数を二進数で表した時に1であるようなビットの個数を返す
  // x = 42 => 101010 (= 2**5 + 2**3 + 2**1 = 32 + 8 + 2 = 42)
  printf("%d\n", __builtin_popcount(42));

  printf("\n --- dec_to_bin_bit ---\n");
  int x2 = 42;
  printf("%d => %s\n", x2, dec_to_bin_bit(x2).c_str());
}