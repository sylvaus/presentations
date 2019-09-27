from enum import Enum, auto
from queue import Queue
from typing import Tuple, Optional

import pygame
from pygame import Vector2, Surface
from pygame.sprite import spritecollide, Group
from pygame.time import Clock

BLACK = (0, 0, 0)


class Directions(Enum):
    TOP = auto()
    LEFT = auto()
    BOTTOM = auto()
    RIGHT = auto()


OPPOSITE_DIRECTION_MAP = {
    Directions.TOP: Directions.BOTTOM
    , Directions.LEFT: Directions.RIGHT
    , Directions.BOTTOM: Directions.TOP
    , Directions.RIGHT: Directions.LEFT
}

DIRECTION_VECTOR_MAP = {
    Directions.TOP: Vector2(0, -1)
    , Directions.LEFT: Vector2(-1, 0)
    , Directions.BOTTOM: Vector2(0, 1)
    , Directions.RIGHT: Vector2(1, 0)
}

pygame.init()


def create_screen(size: Tuple[int, int] = (640, 480)):
    return pygame.display.set_mode(size)


class Block(pygame.sprite.Sprite):
    def __init__(self, size: Tuple[int, int], center: Vector2, color=(255, 255, 255), *groups):
        super().__init__(*groups)

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (center.x, center.y)

    @property
    def center(self):
        return Vector2(self.rect.center[0], self.rect.center[1])

    @center.setter
    def center(self, center: Vector2):
        self.rect.center = (center.x, center.y)

    def move(self, delta: Vector2):
        self.rect.center = (self.rect.center[0] + delta.x, self.rect.center[1] + delta.y)

    def update(self, *args):
        pass


class Snake:
    BLOCK_LENGTH = 16
    BLOCK_SIZE = (BLOCK_LENGTH, BLOCK_LENGTH)

    def __init__(self, start_position: Vector2, length: int, direction: Directions):
        self.group = Group()
        self.queue = Queue()
        self.dir = direction

        for index in range(length):
            position = start_position + index * DIRECTION_VECTOR_MAP[direction] * self.BLOCK_LENGTH
            block = Block(self.BLOCK_SIZE, position, (255, 255, 255), self.group)
            self.queue.put(block)
            if index == (length - 1):
                self.head = block

    def draw(self, screen: Surface):
        self.group.draw(screen)

    def move(self, direction: Optional[Directions], keep_tail):
        if direction == OPPOSITE_DIRECTION_MAP[self.dir] or direction == None:
            direction = self.dir

        self.dir = direction
        block = self.queue.get()
        self.group.remove(block)
        position = self.head.center + DIRECTION_VECTOR_MAP[direction] * self.BLOCK_LENGTH
        block = Block(self.BLOCK_SIZE, position, (255, 255, 255), self.group)
        self.queue.put(block)
        self.head = block


def get_direction(block):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                block.move(DIRECTION_VECTOR_MAP[Directions.TOP] * 4)
            if pressed_keys[pygame.K_DOWN]:
                block.move(DIRECTION_VECTOR_MAP[Directions.BOTTOM] * 4)
            if pressed_keys[pygame.K_LEFT]:
                block.move(DIRECTION_VECTOR_MAP[Directions.LEFT] * 4)
            if pressed_keys[pygame.K_RIGHT]:
                block.move(DIRECTION_VECTOR_MAP[Directions.RIGHT] * 4)


def main():
    size = (640, 480)
    fps = 5

    screen = create_screen(size)
    clock = Clock()
    counter = 0
    score = 0
    snake = Snake(Vector2(300, 300), 6, Directions.RIGHT)
    while True:
        # TODO: Implement the get direction to get the user input and move the snake accordingly
        # get_direction()

        # TODO: Optional Add the code to display the score
        # The score will increase every seconds

        # Update
        counter += 1
        keep_tail = not bool(counter % 3)
        snake.move(Directions.TOP, keep_tail)

        # Draw
        screen.fill(BLACK)
        snake.draw(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
