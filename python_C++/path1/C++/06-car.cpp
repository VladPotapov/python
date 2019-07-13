//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 6. Машинка
//
#include "TXLib.h"          

int main() 
  { 
  txCreateWindow(500, 400);

  POINT c[] = {
         {20,95}, {20,70}, {30,70}, {60,50},
         {100,50}, {120,70}, {160,80}, {160,95}
         };
  txSetFillColor(TX_LIGHTBLUE);       
  txPolygon(c, 8);       

  POINT a[] = { {40,70}, {65,55}, {70,55}, {70,70}};
  txSetFillColor(TX_BLACK);       
  txPolygon(a, 4);       

  POINT b[] = { {75,55}, {95,55}, {110,70}, {75,70}};
  txPolygon(b, 4);

  txSetFillColor(TX_GRAY);       
  txCircle(50, 95, 13);       
  txCircle(120, 95, 13);       
  }

