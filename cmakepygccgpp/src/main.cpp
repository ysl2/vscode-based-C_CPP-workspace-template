#include <iostream>
#include "include1.h"
#include "include2.h"

int main()
{
    std::cout << "C++ Version: " << __cplusplus << std::endl;

    std::cout << "3 + 4 = " << add(3, 4) << std::endl;
    std::cout << "3 - 4 = " << sub(3, 4) << std::endl;
    // std::cout << 1 << std::endl;
    // std::cout << std::endl;
    // system("pause");

    return 0;
}
