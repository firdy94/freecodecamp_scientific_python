class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, val):
        self.width = val

    def set_height(self, val):
        self.height = val

    def get_area(self):
        area = self.width*self.height
        return area

    def get_perimeter(self):
        perimeter = 2*(self.width+self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        line = ''
        if self.width > 50 or self.height > 50:
            return ('Too big for picture.')
        else:
            for i in range(1, self.height+1):
                line += '*'*self.width+'\n'

        return line

    def get_amount_inside(self, shape):
        ref_area = self.get_area()
        test_area = shape.get_area()
        num_inside = ref_area//test_area
        return num_inside


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_width(self, val):
        self.width = val
        self.height = val

    def set_height(self, val):
        self.height = val
        self.width = val

    def set_side(self, val):
        self.set_width(val)
        self.set_width(val)


