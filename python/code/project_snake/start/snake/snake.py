from typing import Tuple

import pygame

pygame.init()


def create_screen(size: Tuple[int, int] = (640, 480)):
    return pygame.display.set_mode(size)


class Block(pygame.sprite.Sprite):
    def __init__(self, size: Tuple[int, int], center: Tuple[int, int], *groups):
        super().__init__(*groups)

        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = center

    @property
    def center(self):
        return self.rect.center

    @center.setter
    def center(self, center: Tuple[int, int]):
        self.rect.center = center

    def move(self, delta: Tuple[int, int]):
        self.rect.center = (self.rect.center[0] + delta[0], self.rect.center[1] + delta[1])


def handle_inputs(block):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                block.move((0, -4))
            if pressed_keys[pygame.K_DOWN]:
                block.move((0, 4))
            if pressed_keys[pygame.K_LEFT]:
                block.move((-4, 0))
            if pressed_keys[pygame.K_RIGHT]:
                block.move((4, 0))


def main():
    # Pygame needs to be initialized befor anything
    size = (640, 480)
    fps = 60
    block_size = (20, 20)
    # Ensure that the key entry will be repeated if held down
    pygame.key.set_repeat(100, 100)

    screen = create_screen(size)
    clock = pygame.time.Clock()

    block = Block(block_size, (100, 100))
    sprite_group = pygame.sprite.Group()
    sprite_group.add(block)
    while True:
        handle_inputs(block)

        # Update
        sprite_group.update()

        # Draw
        screen.fill((0, 0, 0))
        sprite_group.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
