screen_x = 200
screen_y = 200
square_size = 100
square_x1 = screen_x - square_size // 2
square_y1 = screen_y - square_size // 2
square_x1_bottom = square_x1
square_y1_bottom = square_y1 + square_size
square_x2 = screen_x + square_size // 2
square_y2 = screen_y + square_size // 2
square_y2_top = square_y2 - square_size
square_x2_top = square_x2

print(square_x1, square_y1)
print(square_x1_bottom, square_y1_bottom)
print(square_x2, square_y2)
print(square_x2_top, square_y2_top)


from graph import *
polygon([(square_x1, square_y1), (square_x1_bottom, square_y1_bottom), (square_x2, square_y2), (square_x2_top, square_y2_top), (square_x1, square_y1)])
penColor('black')
point(screen_x, screen_y)
run()