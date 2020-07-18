import time

class squareOccupied(Exception):
    pass


class goalReached(Exception):
    def __init__(self, move):
        self.totalMoves = move
        super().__init__()


class Knight(object):
    def __init__(self, moves = 0):
        self.moves = moves
        self.alive = True
    
    def check(self, x, y, map):
        if self.alive:
            if map[(x, y)].isGoal: raise goalReached(self.moves)
            for (xAdd, yAdd) in [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]:
                try:
                    self.move(map[x + xAdd, y + yAdd])
                except squareOccupied:
                    pass
                except KeyError:
                    pass      
        self.alive = False

    def move(self, square):
        if square.occupied: raise squareOccupied()
        square.occupied = Knight(self.moves + 1)


class Square(object):
    def __init__(self, *pos):
        self.pos = pos
        self.occupied = None
        self.isGoal = False


class Chessboard(object):
    def __init__(self):
        self.map = dict()
        self.mapTraverse("self.map[(x, y)] = Square(x, y)")

    def mapTraverse(self, code):
        for x in range(301):
            for y in range(301):
                exec(code)

    def calculate(self, start, goal):
        self.map[start].occupied = Knight()
        self.map[goal].isGoal = True
        try:
            while True:
                self.step()
        except goalReached as solution:
            print("the minimum move is: " + str(solution.totalMoves))

    def step(self):
        self.mapTraverse("if self.map[(x, y)].occupied: self.map[(x, y)].occupied.check(x, y, self.map)")


startTime = time.time()

chessboard = Chessboard()
chessboard.calculate((12, 17), (225, 230))

endTime = time.time()
print("runtime = " + str(endTime - startTime))
input()
