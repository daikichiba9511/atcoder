#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

int main()
{
    int N;
    cin >> N;
    ll X = 0;
    vector<ll> x(N);
    for (ll i = 0; i < N; ++i) {
        ll A, B;
        cin >> A >> B;
        X -= A;
        x[i] = A + A + B;
    }
    sort(x.begin(), x.end());
    ll ans = 0;
    while (X <= 0){
        X += x.back();
        x.pop_back();
        ans++;
    }
    cout << ans << endl;
}