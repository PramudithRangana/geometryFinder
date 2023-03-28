class Circumference:
    @staticmethod
    def Square(length, width):
        circumference = length * width
        return circumference

    @staticmethod
    def Rectangle(length, width):
        circumference = 2 * (length + width)
        return circumference

    @staticmethod
    def Triangle(first_line, second_line, third_line):
        circumference = first_line + second_line + third_line
        return circumference

    @staticmethod
    def Trapezium(first_line, second_line, third_line, forth_line):
        circumference = first_line + second_line + third_line + forth_line
        return circumference

    @staticmethod
    def Circle(radius):
        circumference = 2 * 3.142857142857143 * radius
        return circumference

    @staticmethod
    def Ellipse(min_radius, max_radius):
        circumference = 3.142857142857143 * (2 * ((min_radius ** 2) + (max_radius ** 2))) ** 0.5
        return circumference

    @staticmethod
    def Parallelogram(length, width):
        circumference = 2 * (length + width)
        return circumference

    @staticmethod
    def Cube(length):
        circumference = 6 * (length ** 2)
        return circumference

    @staticmethod
    def Rectangular_Cube(length, width, height):
        circumference = 2 * ((width * length) + (width * height) + (length * height))
        return circumference

    @staticmethod
    def Pyramid(length, angle_height):
        circumference = length * (length + (2 * angle_height))
        return circumference

    @staticmethod
    def Sphere(radius):
        circumference = 4 * 3.142857142857143 * (radius ** 2)
        return circumference

    @staticmethod
    def Cylinder(radius, height):
        circumference = (2 * 3.142857142857143 * radius) * (radius + height)
        return circumference

    @staticmethod
    def Cone(radius, height):
        circumference = (3.142857142857143 * radius) * (radius + height)
        return circumference

    @staticmethod
    def Tetrahedron(length):
        circumference = (length ** 2) * 1.7320508075688772935274463415059
        return circumference


class Area:
    @staticmethod
    def Square(length):
        area = length ** 2
        return area

    @staticmethod
    def Rectangle(length, width):
        area = length * width
        return area

    @staticmethod
    def Triangle(base_line, height):
        area = (base_line * height) / 2
        return area

    @staticmethod
    def Trapezium(top_line, bottom_line, height):
        area = ((top_line + bottom_line) / 2) * height
        return area

    @staticmethod
    def Circle(radius):
        area = 3.142857142857143 * (radius ** 2)
        return area

    @staticmethod
    def Ellipse(min_radius, max_radius):
        area = min_radius * max_radius * 3.142857142857143
        return area

    @staticmethod
    def Parallelogram(length, height):
        area = length * height
        return area

    @staticmethod
    def Cube(length):
        area = length ** 3
        return area

    @staticmethod
    def Rectangular_Cube(length, width, height):
        area = length * width * height
        return area

    @staticmethod
    def Pyramid(length, total_height):
        area = ((length ** 2) * total_height) / 3
        return area

    @staticmethod
    def Sphere(radius):
        area = (4 * 3.142857142857143 * (radius ** 3)) / 3
        return area

    @staticmethod
    def Cylinder(radius, height):
        area = (3.142857142857143 * (radius ** 2) * height)
        return area

    @staticmethod
    def Cone(radius, total_height):
        area = (3.142857142857143 * (radius ** 2) * total_height) / 3
        return area

    @staticmethod
    def Tetrahedron(length):
        area = (length ** 3) / 12 * 1.4142135623730950488016887242097
        return area


'''
if __name__ == '__main__':
    c = Circumference()
    a = Area()

    rc = c.Tetrahedron(5)
    print('Circumference : ', rc)
    ra = a.Cylinder(5, 4)
    print('area :', ra)
'''
