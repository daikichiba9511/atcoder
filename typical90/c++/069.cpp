#include <iostream>

const int MOD = 1000000007;

int binpower(int a, int b) {
  int ans = 1;
  while (b != 0) {
    if (b % 2 == 1) {
      ans = (long long)(ans)*a % MOD;
    }
    a = (long long)(a)*a % MOD;
    b /= 2;
  }
  return ans;
}

int main() {
  long long N;
  int K;
  std::cin >> N >> K;

  if (K == 1) {
    std::cout << (N == 1 ? 1 : 0) << std::endl;
  } else if (N == 1) {
    std::cout << K % MOD << std::endl;
  } else if (N == 2) {
    std::cout << (long long)(K) * (K - 1) % MOD << std::endl;
  } else {
    std::cout << (long long)(K) * (K - 1) * binpower(K - 2, N - 2) % MOD
              << std::endl;
  }
  return 0;
}
