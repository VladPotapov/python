//
// Программа к учебному пособию
// К.Ю. Поляков. Программирование на языках Python и C++
// Часть 1 (8 класс)
// Программа № 5. Геометрические фигуры
//
#include "TXLib.h"          

int main() 
  { 
  txCreateWindow (800, 600);
  
  txSetColor(TX_GREEN, 5);
  txLine(100, 20, 10, 150);
  
  txSetColor(TX_BLUE, 2);
  txSetFillColor( TX_YELLOW );
  POINT contour[3] = {{0,0}, {100,100}, {0,50}};
  txPolygon( contour, 3 );
  
  txSetColor(TX_PINK, 1);
  txRectangle( 150, 50, 200, 130 );

  txSetFillColor( TX_TRANSPARENT );
  txCircle(100, 100, 50);

  }

