//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 17. Цикл с условием
//
#include <iostream>

using namespace std;

int main()
{
  int count = 0;
  while(count < 10) {  // заголовок цикла 
    cout << "Hello!" << endl;
    count ++;
    }       

  count = 10;
  while(count > 0) {  // заголовок цикла 
    cout << "Bye!" << endl;
    count --;
    }       

  cin.get();	
}

