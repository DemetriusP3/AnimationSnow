from pygame import *
from random import randint


# basses class
class Window:
    def __init__(self, name, size=(800, 600), fps=30):
        # name, size
        self.name = name
        self.size = size
        self.width, self.height = size

        self.run = True

        init()
        time.set_timer(USEREVENT, 500)

        self.win = display.set_mode(size)
        display.set_caption(name)
        cadr = time.Clock()

        self.snows = sprite.Group()

        while self.run:
            self.event_handling()

            self.win.blit(image.load('bg.png'), (0, 0))

            self.snows.draw(self.win)

            cadr.tick(fps)
            display.update()
            self.snows.update(self.height)

    def event_handling(self):
        for e in event.get():
            if e.type == QUIT:
                self.run = False
            elif e.type == USEREVENT:
                self.snows.add(Snow(randint(0, self.width), self.snows))

    def create_snows(self):
        pass

class Snow(sprite.Sprite):
    def __init__(self, x, gruop, size=5):
        sprite.Sprite.__init__(self)
        self.image = image.load("snow.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

        self.speed = randint(1, 4)

        self.add(gruop)

    def update(self, *args):
        if self.rect.y < args[0]:
            self.rect.y += self.speed
        else:
            self.kill
