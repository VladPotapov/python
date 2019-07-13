//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 19. Бесконечный цикл с выходом по break
//
#include <iostream>

using namespace std;

int main()
{
  int yearBirth;
  bool isValid;
  while ( 1 ) {
    cout << "year of birth: ";
    cin >> yearBirth;
    isValid = (1900 <= yearBirth and
                     yearBirth <= 2018); 
    if ( isValid ) break;
    cout << "Invalid year of birth! Oh-oh-oh!" << endl;
    }
  cout << "OK"; 

  cin.get();	
}

