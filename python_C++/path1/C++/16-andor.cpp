//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 16. Сложные условия
//
#include <iostream>

using namespace std;

int main()
{
  int a = 2;
  cout << a << endl;	
  if (9 < a  and  a < 100)
    cout << "Two-digit number!";
  else
    cout << "Not a two-digit number.";
  cout << endl;  

  a = 22;
  cout << a << endl;	
  if (a < 10  or  a > 99)
    cout << "Not a two-digit number again... :(";
  else
    cout << "Wow! A two-digit number!";
  cout << endl;  

  float x = 0.5, y = 1.5;
  if( not(y >= 0 and x >= 0 and y <= 1-x) )  {
    cout << "Point not in the triangle." << endl;
    }
  if( y < 0 or x < 0 or y > 1-x )  {
    cout << "Point not in the triangle." << endl;
    }

  int day = 3, hour = 20;
  bool isHoliday = (day > 5);
  bool nightHour = (hour >= 18 or hour <= 6);
  if (isHoliday or (not isHoliday and nightHour))
    cout << "Reduced rate!";
  else
    cout << "Congratulations! Full rate!";
  cout << endl;
  
  if( isHoliday or nightHour )
    cout << "Sorry, reduced rate...";
  else
    cout << "Wow! Full rate!";

  cin.get();	
}

