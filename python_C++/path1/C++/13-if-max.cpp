//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 13. �������� ��������. ����� ��������� �� ����
//
#include <iostream>

using namespace std;

int main()
{
  int a = 6, b = 4, M;
  
  if (a > b) M = a; 
  else       M = b; 
  cout << a << " " << b << " -> " << M << endl;
  
  M = a; 
  if (b > a) M = b;
  cout << a << " " << b << " -> " << M << endl;

  M = max(a, b);  
  cout << a << " " << b << " -> " << M << endl;
  
  if (a > b) { 
    int temp = a; 
    a = b; 
    b = temp;
    }
  cout << a << " " << b << endl;
  
  cin.get();	
}

