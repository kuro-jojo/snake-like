import time
import pygame, sys, os
from random import randint, randrange
from snake import Snake

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Config the snake 😅
Snake.WIDTH = WINDOW_WIDTH // 40
Snake.HEIGHT = WINDOW_HEIGHT // 40
Snake.SPEED = 10 

def generate_bonus(window, existant_bonus=None):
    # bonus_image = pygame.image.load('assets/egg.png')
    # bonus_image = pygame.transform.scale(bonus_image, (20, 20))
    # window.blit(bonus_image, (20, 100))
    
    if existant_bonus != None:
        return pygame.draw.rect(window, 'white', existant_bonus)
    else:
        bonus_position_left = randrange(0, WINDOW_WIDTH - 10, 20)
        bonus_position_top = randrange(0, WINDOW_HEIGHT - 10, 20)
        
        return pygame.draw.rect(window, 'white', 
                    pygame.Rect(bonus_position_left, bonus_position_top, Snake.WIDTH, Snake.HEIGHT))
    

def main():
    """Runs the whole game
    """
    
    # INITIALIZATION OF THE GAME 
    pygame.init()
    
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # window.fill(pygame.Color('white'))
    
    # load the grass image
    bg_image = pygame.image.load('assets/bg.jpg')
    window.blit(bg_image, (0, 0))
    
    # create the head of the snake   
    current_direction = Snake.UP
    
    snake = Snake(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, window, current_direction)
    
    bonus = generate_bonus(window)
    is_bonus_taken = False
    
    # Game loop
    while True:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
    
            # Snake movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and current_direction != Snake.UP:
                    snake.move(Snake.UP, window) 
                    current_direction = Snake.UP
                      
                elif event.key == pygame.K_DOWN and current_direction != Snake.DOWN:
                    snake.move(Snake.DOWN, window)
                    current_direction = Snake.DOWN
                    
                elif event.key == pygame.K_LEFT and current_direction != Snake.LEFT:
                    snake.move(Snake.LEFT, window)
                    current_direction = Snake.LEFT
                    
                elif event.key == pygame.K_RIGHT and current_direction != Snake.RIGHT:
                    snake.move(Snake.RIGHT, window)
                    current_direction = Snake.RIGHT
        
        # add the grass background to the window 
        window.blit(bg_image, (0, 0))
        # continuous movement
        snake.move(current_direction, window)
        
        bonus = generate_bonus(window, bonus)
        # if pygame.Rect.colliderect(bonus, snake.get_part(0)[0]):
        if bonus.__eq__(snake.get_part(0).get('position')):
            snake.add_part(window)
            bonus = generate_bonus(window)

        # update only some region of the window 
        
        # pygame.display.update([snake.get_part(0)[0], snake.get_part(-1)[0]])
        pygame.display.flip()
        # wait a while to more smoothy
        time.sleep(0.2)
        
        
if __name__ == '__main__':
    main()