//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 23. Анимация с управлением клавишами
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
   	 
     short left = GetAsyncKeyState(VK_LEFT);    
     short right = GetAsyncKeyState(VK_RIGHT);    
     short up = GetAsyncKeyState(VK_UP);    
     short down = GetAsyncKeyState(VK_DOWN);    
	   
     drawBall(xCenter, yCenter, R);
     txSleep(20);    
     clearBall(xCenter, yCenter, R);

     if ( left ) xCenter -= 5;
     if ( right ) xCenter += 5;
     if ( up ) yCenter -= 5;
     if ( down ) yCenter += 5;
     }

   //txEnd();  
  }

