import time
import pygame, sys
from random import randrange
from snake import Snake

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Config the snake 😅
Snake.WIDTH = WINDOW_WIDTH // 40
Snake.HEIGHT = WINDOW_HEIGHT // 40
# Snake.SPEED = 10 # problem that one; might be the same as a part size
Snake.SPEED = Snake.WIDTH

# create a rect for the game window
window_borders = {
    "top": pygame.Rect(0, 0, WINDOW_WIDTH, -20),  # TOP
    "bottom": pygame.Rect(0, WINDOW_HEIGHT, WINDOW_WIDTH, 20),  # BOTTOM
    "left": pygame.Rect(0, 0, -20, WINDOW_HEIGHT),  # LEFT
    "right": pygame.Rect(WINDOW_WIDTH, 0, 20, WINDOW_HEIGHT),  # RIGHT
}


def generate_bonus(window, existant_bonus=None):
    # bonus_image = pygame.image.load('assets/egg.png')
    # bonus_image = pygame.transform.scale(bonus_image, (20, 20))
    # window.blit(bonus_image, (20, 100))

    if existant_bonus != None:
        return pygame.draw.rect(window, "white", existant_bonus)
    else:
        bonus_position_left = randrange(0, WINDOW_WIDTH - Snake.WIDTH, Snake.WIDTH)
        bonus_position_top = randrange(0, WINDOW_HEIGHT - Snake.WIDTH, Snake.WIDTH)

        return pygame.draw.rect(
            window,
            "white",
            pygame.Rect(
                bonus_position_left, bonus_position_top, Snake.WIDTH, Snake.HEIGHT
            ),
        )


def handle_collision_with_borders(snake_parts: list):
    """handle the collision with the borders

    Args:
        snake_part (pygame.Rect): a part of snake
    """
    # depending on the border, recalculate the position of the part
    for i in range(len(snake_parts)):
        part = snake_parts[i].get("position")
        if part.top < 0:
            part.top = WINDOW_HEIGHT
        elif part.top > WINDOW_HEIGHT:
            part.top = -Snake.HEIGHT
        elif part.left < 0:
            part.left = WINDOW_WIDTH
        elif part.left > WINDOW_WIDTH:
            part.left = -Snake.WIDTH
        else:
            continue  # not really useful

        snake_parts[i]["position"] = part


def lost(snake: Snake) -> bool:
    """check if the snake beat itself

    Args:
        snake (Snake): snake object

    Returns:
        bool: the result
    """

    snake_head = snake.get_part(0).get("position")
    for part in snake.body_parts[1::]:
        if part.get("position").colliderect(snake_head):
            return True
    return False


def main():
    """Runs the whole game"""

    # INITIALIZATION OF THE GAME
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # load the grass image
    bg_image = pygame.image.load("assets/bg.jpg")
    bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_WIDTH))
    window.blit(bg_image, (0, 0))

    # create the head of the snake
    current_direction = Snake.UP

    snake = Snake(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, window, current_direction)

    bonus = generate_bonus(window)

    score = 0
    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Snake movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (
                    current_direction != Snake.UP
                    and (current_direction != Snake.DOWN or len(snake.body_parts) == 1)
                ):
                    snake.move(Snake.UP, window)
                    current_direction = Snake.UP

                elif event.key == pygame.K_DOWN and (
                    current_direction != Snake.DOWN
                    and (current_direction != Snake.UP or len(snake.body_parts) == 1)
                ):
                    snake.move(Snake.DOWN, window)
                    current_direction = Snake.DOWN

                elif event.key == pygame.K_LEFT and (
                    current_direction != Snake.LEFT
                    and (current_direction != Snake.RIGHT or len(snake.body_parts) == 1)
                ):
                    snake.move(Snake.LEFT, window)
                    current_direction = Snake.LEFT

                elif event.key == pygame.K_RIGHT and (
                    current_direction != Snake.RIGHT
                    and (current_direction != Snake.LEFT or len(snake.body_parts) == 1)
                ):
                    snake.move(Snake.RIGHT, window)
                    current_direction = Snake.RIGHT

        # add the grass background to the window
        window.blit(bg_image, (0, 0))
        # made the move unless it's an forbidden move

        snake.move(current_direction, window)

        bonus = generate_bonus(window, bonus)

        # TODO : Try to fix why sometimes the bonus cannot be taken, eventhough it's clear that the snake ate it
        if equal_rect(bonus, snake.get_part(0).get("position")):
            snake.add_part(window)
            bonus = generate_bonus(window)
            score += 10

        if lost(snake):
            print("YOU LOSE!!!!!!!!!!!!!", score)
            pygame.quit()

        # borders collision problem
        handle_collision_with_borders(snake.body_parts)

        # TODO : fix the disappearance of some rect (just visualy) (randomly)

        pygame.display.flip()
        # wait a while to more smoothy
        time.sleep(0.2)


def equal_rect(rect1: pygame.Rect, rect2: pygame.Rect):
    if rect1.top == rect2.top and rect1.left == rect2.left:
        return True
    return False


if __name__ == "__main__":
    main()
