#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    while (true) {
        int N, M;
        cin >> N;
        cin >> M;
        if (N == 0 and M == 0) {
            break;
        }

        unordered_set <int> nSet{};


        for (int n = 0; n < N; n++) {
            int cd;
            cin >> cd;
            nSet.insert(cd);
        }
        int totalToSell = 0;
        for (int m = 0; m < M; m++) {
            int cd;
            cin >> cd;
            totalToSell += nSet.find(cd) != nSet.end();
        }
        cout << totalToSell << '\n';
    }
    return 0;
}