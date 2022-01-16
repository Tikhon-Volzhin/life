import pickle

inf = float("inf")
class Cells:
    def __init__(self):
        self.cells_alive = {}
        self.minX = inf
        self.maxX = -inf
        self.minY = inf
        self.maxY = -inf

    def insert(self, pointer):
        if (pointer not in self.cells_alive) or (not self.cells_alive[pointer][0]):
            x, y = pointer
            self.minX = min(x, self.minX)
            self.maxX = max(x, self.maxX)
            self.minY = min(y, self.minY)
            self.maxY = max(y, self.maxY)

            n = 0

            def cells_near(position):
                if position in self.cells_alive:
                    c1, c2 = self.cells_alive[position]
                    self.cells_alive[position] = (c1, c2 + 1)
                    return int(c1)
                else:
                    self.cells_alive[position] = (False, 1)
                    return 0

            n += cells_near((x - 1, y - 1))
            n += cells_near((x - 1, y))
            n += cells_near((x - 1, y + 1))
            n += cells_near((x, y - 1))
            n += cells_near((x, y + 1))
            n += cells_near((x + 1, y - 1))
            n += cells_near((x + 1, y))
            n += cells_near((x + 1, y + 1))

            self.cells_alive[pointer] = (True, n)

    def delete(self, position):
        if (position in self.cells_alive) and (self.cells_alive[position][0]):
            x, y = position

            def dec_c2(posn):
                c1, c2 = self.cells_alive[posn]
                self.cells_alive[posn] = (c1, c2 - 1)

            dec_c2((x - 1, y - 1))
            dec_c2((x - 1, y))
            dec_c2((x - 1, y + 1))
            dec_c2((x, y - 1))
            dec_c2((x, y + 1))
            dec_c2((x + 1, y - 1))
            dec_c2((x + 1, y))
            dec_c2((x + 1, y + 1))

            self.cells_alive[position] = (False, self.cells_alive[position][1])

    def clean(self):
        self.minX = inf
        self.maxX = -inf
        self.minY = inf
        self.maxY = -inf
        new_cells = {}
        for posn in iter(self.cells_alive):
            if self.cells_alive[posn] != (0, 0):
                x, y = posn
                self.minX = min(x, self.minX)
                self.maxX = max(x, self.maxX)
                self.minY = min(y, self.minY)
                self.maxY = max(y, self.maxY)
                new_cells[posn] = self.cells_alive[posn]
        self.cells_alive = new_cells

    def next_gen(self):
        model = Cells()
        for pointer in iter(self.cells_alive):
            c1, c2 = self.cells_alive[pointer]
            if (c2 == 3) or (c1 and c2 == 2):
                model.insert(pointer)
        return model

    def save(self, name):
        file = open(name, 'wb')
        pickle.dump(self, file)
        file.close()

    def load(name):
        file = open(name, 'rb')
        model = pickle.load(file)
        file.close()
        return model