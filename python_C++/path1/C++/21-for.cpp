//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 21. ���� �� ����������
//
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  for( int k=0; k<10; k++ ) 
    cout << "Hello!" << endl;
    
  for( int k=10; k<=99; k++ ) {
    int squareK = k*k;
    if( squareK % 100 == k ) 
      cout << k << endl;          
    }     

  for ( int k=99; k>0; k-=2 )
    cout << k*k << " ";          
  cout << endl;          

  for ( float x=1.5; x<=2; x +=0.1 )
    cout << x << " " << x*x << endl;

  cin.get();	
}

