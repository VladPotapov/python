//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 2. Как тебя зовут?
//
#include <iostream>
#include <limits>

using namespace std;

int main()
{
  string name;    
  cout << "What is your name? ";   
  cin >> name;   
  
  cout << "Hello, " << name << "!";   
  
  cin.ignore( numeric_limits<streamsize>::max(), '\n' );    
  cin.get();
}
