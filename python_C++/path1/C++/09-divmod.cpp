//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 9. Деление и остаток
//
#include <iostream>

using namespace std;

int main()
{
  int i;
  cout << sizeof(i) << endl;
  cout << sizeof(int) << endl;
  
  cout << 7 / 4 << " " << 7 % 4 << endl;
  cout << 4 / 7 << " " << 4 % 7 << endl;
  
  int timeSec = 289;
  int minutes = timeSec / 60;    // 4
  int seconds = timeSec % 60;    // 49
  cout << timeSec << " sec = " 
       << minutes << " min " << seconds << " sec." << endl;

  cout << 7.0 / 4 << endl;
  int a = 3, b = 4;
  float x;
  x = a / b;          // 0
  cout << x << endl;
  x = a / float(b);   // 0.75
  cout << x << endl;
  x = float(a) / b;   // 0.75
  cout << x << endl;
  x = float(a) / float(b); // 0.75
  cout << x << endl;

  cin.get();	
}

