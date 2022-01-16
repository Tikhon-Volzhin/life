import pygame, sys, time
from cells import *
from gui import *

class Life:
    def __init__(self):
        pygame.init()


        self.cells = Cells()

        self.view = Gui(self.screen)
        self.view.draw_grid()
        self.view.draw_model(self.cells)


        self.cells.insert((0, -1))
        self.cells.insert((0, 0))
        self.cells.insert((0, 1))
        self.view = pygame.display.set_mode((510, 510))



    def input(self, events):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.view.y0 -= 1
            self.view.draw_model(self.cells)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.view.y0 += 1
            self.view.draw_model(self.cells)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.view.x0 -= 1
            self.view.draw_model(self.cells)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.view.x0 += 1
            self.view.draw_model(self.cells)
            time.sleep(0.1)

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.cells = self.cells.next_gen()
                self.view.draw_model(self.cells)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.cells.clean()
                self.cells.save("life.dat")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                self.cells = Cells.load("life.dat")
                self.view.draw_model(self.cells)
            elif event.type == pygame.MOUSEBUTTONUP and event.button in [1, 3]:
                x, y = event.pos
                x = x // self.view.length + self.view.x0
                y = y // self.view.length + self.view.y0
                if event.button == 1:
                    self.cells.insert((x, y))
                else:
                    self.cells.delete((x, y))
                self.view.draw_model(self.cells)

    def action(self):
        while 1:
            self.input(pygame.event.get())
            self.view.draw()

def main():
    life = Life()
    life.action()

if __name__ == '__main__': main()