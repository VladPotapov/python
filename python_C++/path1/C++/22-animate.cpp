//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 22. Анимация
//
#include "TXLib.h"          
#include <iostream>

using namespace std;

void drawBall(int xCenter, int yCenter, int R) 
  {
  txSetColor(TX_TRANSPARENT);   
  txSetFillColor(TX_YELLOW);
  txCircle(xCenter, yCenter, R);
  }

void clearBall(int xCenter, int yCenter, int R) 
  {
  txSetColor(TX_TRANSPARENT);   
  txSetFillColor(TX_BLUE);
  txCircle(xCenter, yCenter, R);
  }

int main() 
  { 
   txCreateWindow(400, 400);
   //txBegin();    
   txSetFillColor(TX_BLUE);
   txRectangle(0, 0, 400, 400);

   int R = 10, 
       xCenter = R, yCenter = 200;
   while( xCenter <= 400-R ) {
   	 if( GetAsyncKeyState(VK_ESCAPE) ) break;   
     drawBall(xCenter, yCenter, R);
     txSleep(20);    
     clearBall(xCenter, yCenter, R);
     xCenter += 5;
     }

   //txEnd();  
  }

