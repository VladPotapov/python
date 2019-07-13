//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 8. Машинка с процедурами с параметрами
//
#include "TXLib.h"          

void drawCarBody(int x, int y) 
  {
  POINT carBody[8] = {
         {x,y}, {x,y-25}, {x+10,y-25}, {x+40,y-45},
         {x+80,y-45}, {x+100,y-25}, {x+140,y-15}, {x+140,y}
         };
  txSetFillColor(TX_LIGHTBLUE);       
  txPolygon(carBody, 8);       
  }

void drawCarWindows(int x, int y) 
  {
  POINT backWindow[4] = { {x+20,y-25}, {x+45,y-40}, {x+50,y-40}, {x+50,y-25}};
  POINT frontWindow[4] = { {x+55,y-40}, {x+75,y-40}, {x+90,y-25}, {x+55,y-25}};
  txSetFillColor(TX_BLACK);       
  txPolygon(backWindow, 4);       
  txPolygon(frontWindow, 4);
  }

void drawCarWheels(int x, int y) 
  {
  txSetFillColor(TX_GRAY);       
  txCircle(x+30, y, 13);       
  txCircle(x+100, y, 13);       
  }            

void drawCar(int x, int y) 
  {
  drawCarBody(x, y);
  drawCarWindows(x, y);
  drawCarWheels(x, y);   
  }     

int main()
{
  txCreateWindow(500, 400);
  drawCar(100, 100);
}

