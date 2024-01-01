# 14. To find the Euclidean distance between two points 
# in a two dimensional space using class and object.

class points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx ** 2 + dy ** 2) ** 0.5

x1, y1 = map(float, input("Enter coordinates of Point 1 (x y): ").split())
x2, y2 = map(float, input("Enter coordinates of Point 2 (x y): ").split())

point1 = points(x1, y1)
point2 = points(x2, y2)

distance = point1.dist(point2)
print(f"Euclidean distance between Point 1 and Point 2: {distance}")
