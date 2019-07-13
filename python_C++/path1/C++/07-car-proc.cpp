//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 7. Машинка с процедурами
//
#include "TXLib.h"          

void drawCarBody() 
  {
  POINT carBody[] = {
         {20,95}, {20,70}, {30,70}, {60,50},
         {100,50}, {120,70}, {160,80}, {160,95}
         };
  txSetFillColor(TX_LIGHTBLUE);       
  txPolygon(carBody, 8);       
  }
  
void drawCarWindows() 
  {
  POINT backWindow[] = { {40,70}, {65,55}, {70,55}, {70,70}};
  POINT frontWindow[] = { {75,55}, {95,55}, {110,70}, {75,70}};
  txSetFillColor(TX_BLACK);       
  txPolygon(backWindow, 4);       
  txPolygon(frontWindow, 4);
  }
  
void drawCarWheels() 
  {
  txSetFillColor(TX_GRAY);       
  txCircle(50, 95, 13);       
  txCircle(120, 95, 13);       
  }            

int main()
{
  txCreateWindow(500, 400);
  drawCarBody();
  drawCarWindows();
  drawCarWheels();
}

