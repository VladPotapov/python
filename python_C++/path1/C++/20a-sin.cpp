//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 20a. Вычисления синуса с помощью ряда
//
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  float x, sinX;
  float aN, eps = 0.0001;
  
  cout << "x(rad) = ";
  cin >> x;
  
  int N = 1;
  sinX = 0;
  aN = x;
  while ( abs(aN) > eps ) {
    sinX += aN;
    N += 2;     
    aN *= - x*x/(N-1)/N;
  }
  cout << "sin(x) = " << sinX << endl;
  cout << "sin(x) = " << sin(x) << endl;

  cout << "OK"; 

  cin.get();	
}

