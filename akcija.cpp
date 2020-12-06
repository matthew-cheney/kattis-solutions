#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {

    int N;

    cin >> N;

    int books[N];
    for (int i = 0; i < N; i++) {
        cin >> books[i];
    }

    sort(books, books+N, greater<int>());

    int counter = 0;
    int cost = 0;
    for (int i = 0; i < N; i++) {
        if (counter < 2) {
            cost += books[i];
            counter++;
        } else {
            counter = 0;
        }
    }

    cout << cost << endl;

    return 0;

}