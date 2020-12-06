//
// Created by matthew on 9/18/20.
//

#include <iostream>

using namespace std;

int main() {

    int X, Y, N;

    cin >> X >> Y >> N;

    for (int i = 1; i < N + 1; i++) {

        string out_string;

        if (i % X == 0) {
            out_string = "Fizz";
        }
        if (i % Y == 0) {
            out_string += "Buzz";
        }
        if (out_string.empty()) {
            out_string = to_string(i);
        }
        cout << out_string << '\n';

    }

    return 0;
}