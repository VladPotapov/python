//
// ��������� � �������� �������
// �.�. �������. ���������������� �� ������ Python � C++
// ����� 1 (8 �����)
// ��������� � 4. ���������� ���������
//
#include "TXLib.h"          
#include <iostream>

using namespace std;

int main() 
  { 
  txCreateWindow (800, 600);
  txSetPixel(10, 20, TX_LIGHTGREEN);
  txSetPixel(20, 20, RGB(0,255,128));
  cout << txGetPixel(10, 20) << endl;
  cout << hex << txGetPixel(10, 20);
  }

