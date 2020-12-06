#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main() {

    string line;
    while (getline(cin, line)) {
        stringstream input(line);
        vector<int> ints;
        while (true) {
            int n;
            input >> n;
            if (!input)
                break;
            ints.push_back(n);
        }

        int my_sum = 0;
        for (int n : ints) {
            my_sum += n;
        }

        for (int n : ints) {
            if (my_sum - n == n) {
                cout << n << '\n';
                break;
            }
        }

    }

    return 0;
}