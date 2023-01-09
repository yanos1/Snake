from game_utils import get_random_wall_data, WIDTH, HEIGHT, UP, DOWN, RIGHT
class Wall:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        x,y, direction = get_random_wall_data()
        self.location = (x,y)
        self.direction = direction
        self.oriantetion = self.choose_oriantion()
        self.locations = self.get_location(x,y,direction)


    def choose_oriantion(self):
        if self.direction in ["Up", "Down"]:
            return 0
        if self.direction in ["Right", "Left"]:
            return 1

    def get_location(self, x, y, direction):
        if direction in ["Up", "Down"]:
            return [(x, y - self.size//2 + i) for i in range(self.size)
                    if y - self.size//2 + i < HEIGHT and y - self.size//2 + i>=0]

        if direction in ["Right", "Left"]:
            return [(x - self.size//2 + i, y) for i in range(self.size)
                    if x - self.size//2 + i >= 0 and x- self.size//2 + i < WIDTH]

    def in_board(self, coordinate):
        if (0,0) <= coordinate < (WIDTH, HEIGHT):
            return True
        return False

    def move_wall(self):
        if self.direction == UP:
            cor = (self.location[0], self.location[1] + self.size//2 + 1)
        elif self.direction == DOWN:
            cor = (self.location[0], self.location[1] - self.size//2 - 1)
        elif self.direction == RIGHT:
            cor = (self.location[0] + self.size//2 + 1 , self.location[1])
        else:
            cor = (self.location[0] - self.size//2 - 1 , self.location[1])
        if self.in_board(cor):
            self.locations.insert(0, cor)
        self.locations.pop()