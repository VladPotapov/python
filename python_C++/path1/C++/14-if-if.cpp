//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 14. ��������� �������� ���������
//
#include <iostream>

using namespace std;

int main()
{
  int temp = 78;
  
  if(temp < 75) 
    cout << "Mode 1"; 
  else 
    if(temp < 90) 
      cout << "Mode 2";
    else 
      cout << "Mode 3"; 
  cout << endl;
      
  if(temp < 75) 
    cout << "Mode 1"; 
  else if(temp < 90) 
    cout << "Mode 2";
  else 
    cout << "Mode 3"; 
  cout << endl;
  
  temp = 80; 
  if( temp < 90 ) 
    if( temp < 75 ) 
      cout << "Mode 1";
    else 
      cout << "Mode 2";
  cout << endl;

  temp = 98;
  if( temp < 90 ) { 
    if( temp < 75 ) 
      cout << "Mode 1";
    }
  else 
    cout << "Mode 2";
    
  
  cin.get();	
}

