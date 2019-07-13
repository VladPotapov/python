//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 12. Вещественные числа
//
#include <iostream>
#include <iomanip>
#include <cmath>
#include <random>

using namespace std;

int main()
{
  float xx = 4.321;
  cout << xx << endl;
  
  float qElectron = 1.60217662e-19;
  cout << qElectron << endl;
  
  float distToSun = 1.496e11;
  cout << distToSun << endl;
  
  float x = 0.1, y = 0.2;
  float sum = x + y;
  float diff = sum - 0.3;
  cout << sum << endl;
  cout << diff << endl;
  cout << fixed << setprecision(9);
  cout << x+y << endl << diff << endl;
  cout << scientific << setprecision(9);
  cout << x+y << endl << diff << endl;
  
  cout << fixed << setprecision(9);
  cout << x+y << endl << diff << endl;
  
  cout << scientific << setprecision(9);
  cout << x+y << endl << diff << endl;
  
  float X = 1.6, Y = -1.6;
  int intX, intY;
  intX = floor(X);  // = 1
  intY = floor(Y);  // = -2
  cout << X << " " << Y << endl;  
  cout << "Floor: " << intX << " " << intY << endl;  
  intX = ceil(X);   // = 2
  intY = ceil(Y);   // = -1
  cout << "Ceil: " << intX << " " << intY << endl;  
  
  float a = 1.5, b = 2.5;
  float xRand = a + (b-a)*float(rand())/RAND_MAX;    
  cout << fixed << setprecision(3);
  cout << xRand << endl;

  xRand = a + (b-a)*float(rand())/RAND_MAX;    
  cout << xRand << endl;

  xRand = a + (b-a)*float(rand())/RAND_MAX;    
  cout << xRand << endl; 
  
  cin.get();	
}

