//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 20. Вычисления квадратного корня по формуле Герона
//
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  float a;
  cout << "a = ";
  cin >> a;
  
  float x = a, x0 = 0;         
  float eps = 0.00001;           
  while( abs(x-x0) > eps ) {   
    x0 = x;                    // (1)
    x = (x + a/x) / 2;         // (2)     
    } 
  cout << x << endl;
  cout << sqrt(a) << endl;
  
  cout << "OK"; 

  cin.get();	
}

