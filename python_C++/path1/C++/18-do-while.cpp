//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 18. ���� � ������������
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

