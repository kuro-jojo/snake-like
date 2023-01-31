import pygame
class Snake:
    WIDTH = 0
    HEIGHT = 0
    SPEED = 0
    
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    
    HEAD_COLOR = 'red'
    TAIL_COLOR = 'blue'
    
    def __init__(self, start_row, start_col, window:pygame.Surface):
        
        # tuple of rect and color 
        self.body_parts = [] 
        self.body_parts.append([pygame.draw.rect(window, Snake.HEAD_COLOR, 
                                pygame.Rect(start_col, start_row, Snake.WIDTH, Snake.HEIGHT)), Snake.HEAD_COLOR])
        
    
    def get_part(self, index:int):
        return self.body_parts[index]
    
    def set_part(self, index:int, new_part:tuple):
        self.body_parts[index] = new_part
        
    def add_part(self, window:pygame.Surface, direction:str = 'up'):
        """create new rectangle as the snake tail and draw it

        Args:
            window (pygame.Surface): window frame
            direction (str) : direction in which the snake moves
        """
        
        last_part = self.body_parts[-1][0]
            
        # the starting position depends on the moving direction
        new_rect = None
        
        if direction is Snake.UP:
            new_rect = pygame.Rect(last_part.left, last_part.top + Snake.HEIGHT, Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.DOWN:
            new_rect = pygame.Rect(last_part.left, last_part.top - Snake.HEIGHT, Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.LEFT:
            new_rect = pygame.Rect(last_part.left + Snake.WIDTH, last_part.top, Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.RIGHT:
            new_rect = pygame.Rect(last_part.left - Snake.WIDTH, last_part.top, Snake.WIDTH, Snake.HEIGHT)
        else:
            raise NotImplementedError('Direction not defined')
        
        if last_part != self.body_parts[0]:
            self.body_parts[-1][1] = 'black'
            
        self.body_parts.append([new_rect, Snake.TAIL_COLOR])
        # pygame.draw.rect(window, Snake.TAIL_COLOR, new_rect)
        self.update(window)
        
    def move(self, direction:str, window:pygame.Surface):
        """move the snake to a specific direction

        Args:
            direction (str): direction in which the snake moves
            window (pygame.Surface): window frame
        """
        
        # just add a new rect as head and delete the tailù
        new_head = None
        previous_head = self.body_parts[-1][0]

        if direction is Snake.UP:
            new_head = pygame.Rect(previous_head.left, previous_head.top - Snake.SPEED, Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.DOWN:
            new_head = pygame.Rect(previous_head.left, previous_head.top + Snake.SPEED, Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.LEFT:
            new_head = pygame.Rect(previous_head.left - Snake.SPEED, previous_head.top, Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.RIGHT:
            new_head = pygame.Rect(previous_head.left + Snake.SPEED, previous_head.top, Snake.WIDTH, Snake.HEIGHT)
        else:
            raise NotImplementedError('Direction not defined')
        
        self.body_parts.insert(0, [new_head, Snake.HEAD_COLOR])
        self.body_parts.pop() 
        
        # pygame.draw.rect(window, Snake.HEAD_COLOR, new_head)
        # pygame.display.flip()

        print(self.body_parts)
        self.update(window)
    
    def update(self, window):
        
        for part in self.body_parts:
            pygame.draw.rect(window, part[1], part[0])