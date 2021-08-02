class Rectangle:

    def __str__(self):
        #Rectangle(width=5, height=10
        return "Rectangle(width="+ str(self.width) + ", height=" + str(self.height) +")"

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        #* `get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        shape_picture = ""
        count = 0
        for vertical in range(0, self.height):
            shape_picture += ("*" * self.width + "\n")
        if(self.width > 50 or self.height > 50 ):
            return "Too big for picture."
        else: 
            return shape_picture

    def get_amount_inside(self, shape):
        amount_inside = (self.width * self.height)//(shape.width * shape.height)#this will calculate how many time the shape can fit in the rectange
        return amount_inside


class Square(Rectangle):
    
    def __str__(self):
        return "Square(side="+ str(self.width) +")"

    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def get_area(self):
        return self.width * self.height
