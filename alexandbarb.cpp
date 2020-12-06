#include <iostream>

using namespace std;

int main() {

    int k, m, n;

    cin >> k >> m >> n;

    k -= (m + n) * (k / (m + n));

    if (k < m) {
        cout << "Barb" << endl;
    } else {
        cout << "Alex" << endl;
    }

    return 0;
}