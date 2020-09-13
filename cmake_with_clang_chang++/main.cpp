#include <iostream>
#include <swap.h>
#include <test.h>
using namespace std;
int main() {
    int i = 1, j = 10;
    swap(i, j);
    cout << i << j << endl;
    test();
    return 0;
}
