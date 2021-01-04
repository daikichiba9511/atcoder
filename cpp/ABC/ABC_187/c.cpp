#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<string> S(N);
    for (string &s : S) // vector Sの要素の参照を取得、それに標準入力からの値を代入してる
        cin >> s;
    // unorder_set
    // https://cpprefjp.github.io/reference/unordered_set/unordered_set.html
    // 同一キーの要素を複数格納できず、格納順が規定されていないコンテナである。(上記リンク先より引用)
    // 重複したものを探すのは時間の無駄なのでここで重複してる要素を単一の要素に帰る
    unordered_set<string> h(S.begin(), S.end()); // pythonだとsetみたいなもの？
    for (string &s : S) // python for ~ in iteratorと同じ使い方ができる
        // 取ってきたsに!を足して同じ奴が一つあれば1が返ってきて、sは不満文字列
        if (h.count("!" + s)) // 指定したキーの要素数を取得
        {
            cout << s << endl;
            return 0;
        }
        cout << "satisfiable" << endl;
}