# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__ (self, ax, ay , bx , by , cx, cy ):
        self.ax = ax
        self.bx = bx
        self.cx = cx
        self.ay = ay
        self.by = by
        self.cy = cy

     
    def area(self):         

        return abs(self.ax*(self.by - self.cy) + self.bx*(self.cy - self.ay) + self.cx*(self.ay - self.by) ) / 2.0
    
    
    def per(self): #периметр 
        from math import sqrt  
        self.ab = sqrt((self.bx - self.ax)**2 + (self.by - self.ay)**2)
        self.bc = sqrt((self.cx - self.bx)**2 + (self.cy - self.by)**2)
        self.ac = sqrt((self.cx - self.ax)**2 + (self.cy - self.ay)**2)
        per = self.ab + self.bc + self.ac
        return(per)
        
    def high(self): 
        min_ = 0
        min_ = min(self.ab, self.bc, self.ac)
        """ 
        if self.bc >= self.ac <= self.ab:
            min_ = self.ac
        elif self.ac >= self.bc <= self.ab:
            min_ = self.bc
        else:
            min_ = self.ab
        """
        high = 2 * self.area() / min_

        return(high)

tri = triangle(1, 1, 2, 4, 3, 2)

print("Площадь треугольника: ",tri.area())
print("Периметр треугольника: ",tri.per())
print("Высота треугольника: ", tri.high())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class  is_trapezium:
     
    def __init__ (self, ax, ay , bx , by , cx, cy, dx, dy ):
        
        from math import sqrt
        
        self.ax = ax
        self.bx = bx
        self.cx = cx
        self.ay = ay
        self.by = by
        self.cy = cy
        self.dx = dx
        self.dy = dy
        
        self.ab = sqrt((self.bx - self.ax)**2 + (self.by - self.ay)**2)
        self.bc = sqrt((self.cx - self.bx)**2 + (self.cy - self.by)**2)
        
        # self.ac = sqrt((self.cx - self.ax)**2 + (self.cy - self.ay)**2)
        
        self.cd = sqrt((self.dx - self.cx)**2 + (self.dy - self.cy)**2)
        self.da = sqrt((self.ax - self.dx)**2 + (self.ay - self.dy)**2)
     
    def isosceles(self):
        if self.ab == self.cd:
            return "Трапеция равнобедренная"
        else:
            return "Трапеция не равнобедренная"
    
    def len_tra(self):
        return self.ab, self.bc, self.cd, self.da
    
    def area(self):
        from math import sqrt
        return (self.da + self.bc) * sqrt(self.ab**2 - ((self.da - self.bc)**2)/4) / 2
      

tra = is_trapezium(-6,0,-2,2,2,2,6,0)

print(tra.isosceles())
print("Длины сторон: ",tra.len_tra())
print("Площадь трапеции: ",tra.area())

