//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 15. ���������� ����������
//
#include <iostream>

using namespace std;

int main()
{
  bool bb = true;
  bb = false;
  cout << sizeof(bb) << endl;
  cout << sizeof(bool) << endl;
	
  int aa;
  cout << "a = ";
  cin >> aa;
  bool isEven = (aa % 2 == 0);
  cout << aa << " " << isEven << endl;

  int a = 4, b = 6, c = 4;  
  bool found = false;  // ���� �� ����� ���� ������
  found = (a == b);        // ��������� ���� a-b
  if(a == c) found = true; // ��������� ���� a-c
  if(b == c) found = true; // ��������� ���� b-c
  if( found )
    cout << "Found equal!";
  else 
    cout << "No equal.";
  
  cin.get();	
}

