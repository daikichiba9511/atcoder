#include<bits/stdc++.h>
using namespace std;

int main(){
    int i = 30;
    double d = 1.5;
    string s = "hello";

    cout << i + d << endl;
    cout << i * d << endl;
    cout << 45/2 << endl;
    cout << i * d / 2 << endl; //小数点以下切り捨て
    /*
    以下の処理はコンパイルエラー
    cout << s + 1 << endl; // string型
    cout << s * i << endl; // string型とint型
    cout << s + d << endl; // string型とdouble型
     */
}