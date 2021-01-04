#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF_ll = 1e17;
const int INF = 1e8;

int main()
{
    ll N;
    vector<ll> H(1e+5, 0), S(1e+5, 0);

    cin >> N;
    for (ll i = 0; i < N; ++i)
        cin >> H[i] >> S[i];

    vector<ll> seconds(N);
    bool canflag; // optが探索区間内にあって、達成可能か
    // 区間内にある最大値を返す
    ll low = 1;
    ll high = INF_ll;
    ll mid;
    // 二分探索で最適値が達成可能区間内にあるか判定する
    while (high - low > 1)
    {
        mid = (low + high) / 2; // 中点
        canflag = true;

        for (ll j = 0; j < N; j++)
        {
            if (H[j] > mid)
                canflag = false;
            seconds[j] = (mid - H[j]) / S[j]; // midが達成ラインの高さとした時の各風船のその達成ラインの高さまでの制限時間
        }

        sort(seconds.begin(), seconds.end());
        for (ll j = 0; j < N; j++)
        {
            // 制限時間の短いやつから割っていくと考えた時に
            // j番目に余裕のある風船をj秒後に制限時間を超えていなかチェック
            // 超えていなければj番目の風船は割れる<->midがopt>X=mid条件を満たさない
            if (seconds[j] < j)
            {
                canflag = false;
                break;
            }
        }
        if (canflag)
            high = mid;
        else
            low = mid;
    }
    cout << high << endl;
    return 0;
}