//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 11. Случайные числа
//
#include <iostream>
#include <random>
#include <ctime>

using namespace std;

int main()
{
  // srand( time(0) );
  
  cout << rand() << endl;
  cout << rand() << endl;
  cout << rand() << endl;

  int a = 10, b = 20;  
  int k = a + rand() % (b-a+1);
  cout << k << endl;
  
  k = a + rand() % (b-a+1);
  cout << k << endl;
  
  k = a + rand() % (b-a+1);
  cout << k << endl;

  cin.get();	
}

