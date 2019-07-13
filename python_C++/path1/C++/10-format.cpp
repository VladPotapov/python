//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 10. Форматный вывод
//
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  int a = 12, b = 5;
  cout << setw(4) << a << setw(4) << b << endl;
  cout << left << setw(4) << a << setw(4) << b;

  cin.get();	
}

