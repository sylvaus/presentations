from enum import Enum, auto
from queue import Queue
from typing import Tuple, Optional

import pygame
from pygame import Vector2, Surface
from pygame.sprite import spritecollide, Group
from pygame.time import Clock

BORDER_COLOR = (153, 0, 255)

WHITE = (255, 255, 255)

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

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    def update(self, *args):
        pass


class Apple(Block):
    COLOR = (255, 0, 0)  # red
    APPLE_LENGTH = 16
    APPLE_SIZE = (APPLE_LENGTH, APPLE_LENGTH)

    def __init__(self, center: Vector2, *groups):
        Block.__init__(self, self.APPLE_SIZE, center, self.COLOR, *groups)


class Snake:
    BLOCK_LENGTH = 16
    BLOCK_SIZE = (BLOCK_LENGTH - 1, BLOCK_LENGTH - 1)

    def __init__(self, start_position: Vector2, length: int, direction: Directions):
        self.body = Group()
        self.queue = Queue()
        self.dir = direction

        for index in range(length):
            position = start_position + index * DIRECTION_VECTOR_MAP[direction] * self.BLOCK_LENGTH
            # Handle head differently
            if index != (length - 1):
                block = Block(self.BLOCK_SIZE, position, WHITE, self.body)
                self.queue.put(block)
            else:
                block = Block(self.BLOCK_SIZE, position, WHITE)
                self.queue.put(block)
                self.head = block

    def draw(self, screen: Surface):
        self.body.draw(screen)
        self.head.draw(screen)

    def move(self, direction: Optional[Directions], keep_tail):
        # Prevent running in opposite direction and no direction.
        if direction == OPPOSITE_DIRECTION_MAP[self.dir] or direction is None:
            direction = self.dir
        # Updating the direction
        self.dir = direction

        if not keep_tail:
            # Remove the tail block
            block = self.queue.get()
            self.body.remove(block)
        # Add old head to the group
        self.body.add(self.head)
        # Creating head block.
        position = self.head.center + DIRECTION_VECTOR_MAP[direction] * self.BLOCK_LENGTH
        block = Block(self.BLOCK_SIZE, position, WHITE)
        # Adding head block to snake
        self.queue.put(block)
        self.head = block


def get_direction():
    direction = None
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_UP:
            direction = Directions.TOP
        if event.key == pygame.K_DOWN:
            direction = Directions.BOTTOM
        if event.key == pygame.K_LEFT:
            direction = Directions.LEFT
        if event.key == pygame.K_RIGHT:
            direction = Directions.RIGHT
    return direction


def get_exit():
    if pygame.event.get(pygame.QUIT):
        exit(0)


def write_text(
        text: str, center: Tuple[int, int]
        , screen: Surface
        , font_name: str = "freesansbold.ttf"
        , font_size: int = 25
        , color: Tuple[int, int, int] = (255, 255, 255)
        ,
):
    font = pygame.font.Font(font_name, font_size)

    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = center

    screen.blit(text_render, text_rect)


def main():
    size = (640, 480)
    fps = 5
    direction = None
    screen = create_screen(size)
    clock = Clock()
    is_lost = False
    score = 0
    snake = Snake(Vector2(300, 300), 2, Directions.RIGHT)
    apple_group = Group()
    apple = Apple(Vector2(50, 50), apple_group)
    wall_group = Group()
    walls = [
        Block((size[0], 2), Vector2(size[0] // 2, 1), BORDER_COLOR, wall_group)  # TOP
        , Block((size[0], 32), Vector2(size[0] // 2, size[1] - 16), BORDER_COLOR, wall_group)  # Bottom
        , Block((2, size[1]), Vector2(1, size[1] // 2), BORDER_COLOR, wall_group)  # Left
        , Block((2, size[1]), Vector2(size[0] - 1, size[1] // 2), BORDER_COLOR, wall_group)  # Right
    ]
    keep_tail = False
    while not is_lost:
        get_exit()
        direction = get_direction() or direction

        # Update
        snake.move(direction, keep_tail)
        if spritecollide(snake.head, snake.body, dokill=False) or spritecollide(snake.head, wall_group, dokill=False):
            is_lost = True
        if spritecollide(snake.head, apple_group, dokill=True):
            keep_tail = True
            score += 1
        else:
            keep_tail = False

        direction = None

        # Draw
        screen.fill(BLACK)
        wall_group.draw(screen)
        snake.draw(screen)
        apple_group.draw(screen)
        write_text("Score: {0}".format(score), (size[0] // 2, size[1] // 2), screen)
        pygame.display.flip()

        clock.tick(fps)

    write_text("You Lose", (size[0] // 2, size[1] // 2), screen)
    pygame.display.flip()
    while True:
        get_exit()


if __name__ == '__main__':
    main()
