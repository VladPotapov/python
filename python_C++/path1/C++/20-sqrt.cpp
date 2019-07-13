//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 20. ���������� ����������� ����� �� ������� ������
//
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  float a;
  cout << "a = ";
  cin >> a;
  
  float x = a, x0 = 0;         
  float eps = 0.00001;           
  while( abs(x-x0) > eps ) {   
    x0 = x;                    // (1)
    x = (x + a/x) / 2;         // (2)     
    } 
  cout << x << endl;
  cout << sqrt(a) << endl;
  
  cout << "OK"; 

  cin.get();	
}

