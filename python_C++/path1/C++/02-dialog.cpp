//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 2. ��� ���� �����?
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
