//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 3. ����� �����
//
#include <iostream>
#include <limits>

using namespace std;

int main()
{
  int num1, num2, sum;   
  
  cout << "Give me two numbers: ";
  cin >> num1 >> num2;   
  
  sum = num1 + num2;
  
  cout << num1 << "+" << num2 << "=" << sum << endl;
  
  cout << num1 << "+" << num2 << "=" << num1+num2;

  cin.ignore( numeric_limits<streamsize>::max(), '\n' );    
  cin.get();
}
