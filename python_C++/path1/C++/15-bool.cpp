//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 15. Логические переменные
//
#include <iostream>

using namespace std;

int main()
{
  bool bb = true;
  bb = false;
  cout << sizeof(bb) << endl;
  cout << sizeof(bool) << endl;
	
  int aa;
  cout << "a = ";
  cin >> aa;
  bool isEven = (aa % 2 == 0);
  cout << aa << " " << isEven << endl;

  int a = 4, b = 6, c = 4;  
  bool found = false;  // пока не нашли пару равных
  found = (a == b);        // проверяем пару a-b
  if(a == c) found = true; // проверяем пару a-c
  if(b == c) found = true; // проверяем пару b-c
  if( found )
    cout << "Found equal!";
  else 
    cout << "No equal.";
  
  cin.get();	
}

