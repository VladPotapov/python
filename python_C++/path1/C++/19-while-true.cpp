//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 19. ����������� ���� � ������� �� break
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

