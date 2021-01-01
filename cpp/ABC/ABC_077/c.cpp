#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n ;
    vector<long long> A(n), B(n), C(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> C[i];
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    sort(C.begin(), C.end());

    vector<long long>bc(n);

    for (int i = 0; i < n; i++) {
        long long x = upper_bound(C.begin(), C.end(), B[i]) - B.begin();
        bc[i] = n - x;
    }

    for (int i = n-2; i >=0 ; i--) {
        bc[i] += bc[i+1];
    }

    long long ans = 0;

    for (int i; i<n; i++) {
        long long x = upper_bound(B.begin(), B.end(), A[i]) - B.begin();
        ans += bc[x];
    }

    cout << ans << endl;

}