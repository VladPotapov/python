//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 18. Цикл с постусловием
//
#include <iostream>

using namespace std;

int main()
{
  int yearBirth;
  bool isValid;
  do {
    cout << "year of birth: ";
    cin >> yearBirth;
    isValid = (1900 <= yearBirth and
                     yearBirth <= 2018); 
    if ( not isValid )
      cout << "Invalid year of birth! Oh-oh-oh!" 
           << endl;
    }
  while( not isValid );
  cout << "OK"; 

  cin.get();	
}

