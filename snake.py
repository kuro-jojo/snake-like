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
    PART_COLOR = 'black'
    
    def __init__(self, start_row, start_col, window:pygame.Surface, direction):
        
        # dict of rect and color and the direction of the part
        self.body_parts = [] 
        self.body_parts.append({'position' : pygame.draw.rect(window, Snake.HEAD_COLOR, 
                                pygame.Rect(start_col, start_row, Snake.WIDTH, Snake.HEIGHT)),
                                'color' : Snake.HEAD_COLOR, 
                                'current_direction' : direction,
                                'next_direction' : direction})
        
        self.has_turned = False

    def get_part(self, index:int) -> dict:
        return self.body_parts[index]
    
    def set_part(self, index:int, new_part:dict):
        self.body_parts[index] = new_part
    """    
    def add_part(self, window:pygame.Surface, direction:str = 'up'):
        ""create new rectangle as the snake tail and draw it

        Args:
            window (pygame.Surface): window frame
            direction (str) : direction in which the snake moves
        ""
        
        last_part = self.body_parts[-1][0]
            
        # the starting position depends on the moving direction
        new_rect = None
        
        if direction is Snake.UP:
            new_rect = pygame.Rect(last_part.left, last_part.top + Snake.HEIGHT, Snake.WIDTH, last_part.height+Snake.HEIGHT)
        elif direction is Snake.DOWN:
            new_rect = pygame.Rect(last_part.left, last_part.top - Snake.HEIGHT, Snake.WIDTH, last_part.height+Snake.HEIGHT)
        elif direction is Snake.LEFT:
            new_rect = pygame.Rect(last_part.left + Snake.WIDTH, last_part.top, last_part.width+Snake.WIDTH, Snake.HEIGHT)
        elif direction is Snake.RIGHT:
            new_rect = pygame.Rect(last_part.left - Snake.WIDTH, last_part.top, last_part.width+Snake.WIDTH, Snake.HEIGHT)
        else:
            raise NotImplementedError('Direction not defined')
        
        if last_part != self.body_parts[0]:
            self.body_parts[-1][1] = 'black'
            
        self.body_parts.append([new_rect, Snake.TAIL_COLOR])
        print(self.body_parts)
        # pygame.draw.rect(window, Snake.TAIL_COLOR, new_rect)
        self.update(window)
        """
    
    def add_part(self, window:pygame.Surface):
        """create new rectangle as the snake tail and draw it

        Args:
            window (pygame.Surface): window frame
        """
        
        last_part = self.body_parts[-1]
        last_part_direction = last_part.get('current_direction')
        # the starting position depends on the moving direction
        new_rect = dict()
        
        if last_part_direction is Snake.UP:
            new_rect['position'] = pygame.Rect(last_part.get('position').left, last_part.get('position').top + Snake.HEIGHT, Snake.WIDTH, Snake.HEIGHT)
            
        elif last_part_direction is Snake.DOWN:
            new_rect['position'] = pygame.Rect(last_part.get('position').left, last_part.get('position').top - Snake.HEIGHT, Snake.WIDTH, Snake.HEIGHT)
            
        elif last_part_direction is Snake.LEFT:
            new_rect['position'] = pygame.Rect(last_part.get('position').left + Snake.WIDTH, last_part.get('position').top, Snake.WIDTH, Snake.HEIGHT)
            
        elif last_part_direction is Snake.RIGHT:
            new_rect['position'] = pygame.Rect(last_part.get('position').left - Snake.WIDTH, last_part.get('position').top, Snake.WIDTH, Snake.HEIGHT)
        else:
            raise NotImplementedError('Direction not defined')
        
        # # change the color of the previous tail to black
        # if last_part != self.body_parts[0]:
        #     last_part['color'] = 'black'
            
        new_rect['color'] = Snake.TAIL_COLOR
        new_rect['current_direction'] = last_part_direction
        new_rect['next_direction'] = last_part_direction
        
        self.body_parts.append(new_rect)
        print(self.body_parts)
        # pygame.draw.rect(window, Snake.TAIL_COLOR, new_rect)
        self.update(window)
        
    def move(self, new_direction:str, window:pygame.Surface):
        """move the snake to a specific direction

        Args:
            new_direction (str): direction in which the snake moves
            window (pygame.Surface): window frame
        """
                
        for i in range(len(self.body_parts)):
            part = self.body_parts[i]
            if i != 0:
                front_part = self.body_parts[i-1]
                
                part['current_direction'] = part.get('next_direction')
                # will replace the part in front of him on next move
                part['next_direction'] = front_part.get('current_direction') 
                part['position'] = self.__move_part(part.get('position'), part.get('current_direction'))
                # part['position'] = self.__move_part(part.get('position'), part.get('current_direction'), front_part.get('current_direction'))
                
                if i == len(self.body_parts) - 1:
                    part['color'] = Snake.TAIL_COLOR
                else:
                    part['color'] = Snake.PART_COLOR
                print(front_part)
                print(part)
                print('*'*10)
            else:
                front_part = self.body_parts[0]
                if new_direction != front_part.get('current_direction'):
                    self.has_turned = True
                else:
                    self.has_turned = False
                    
                part['current_direction'] = new_direction
                part['next_direction'] = new_direction
                part['color'] = Snake.HEAD_COLOR
                part['position'] = self.__move_part(front_part.get('position'), new_direction)
                # part['position'] = self.__move_part(front_part.get('position'), new_direction, front_part.get('current_direction'))
                
                
            self.body_parts[i] = part
            
        # print(self.body_parts)
        self.update(window)
    
    def update(self, window):
        
        for part in self.body_parts:
            pygame.draw.rect(window, part.get('color'), part.get('position'))
            
    def __move_part(self, previous_part:pygame.Rect, direction:str)->pygame.Rect:
        
        new_part = None
        # TODO : with a speed different of the size of a part, what to do
        new_speed = Snake.SPEED
        # head_part = self.body_parts[0]
        # if self.has_turned:
        #     new_speed = Snake.WIDTH
        #     print(direction, next_part_direction)
        # else:
        #     new_speed = Snake.SPEED
            
        if direction is Snake.UP:
            new_part = pygame.Rect(previous_part.left, previous_part.top - new_speed, previous_part.width, previous_part.height)
        elif direction is Snake.DOWN:
            new_part = pygame.Rect(previous_part.left, previous_part.top + new_speed, previous_part.width, previous_part.height)
        elif direction is Snake.LEFT:
            new_part = pygame.Rect(previous_part.left - new_speed, previous_part.top, previous_part.width, previous_part.height)
        elif direction is Snake.RIGHT:
            new_part = pygame.Rect(previous_part.left + new_speed, previous_part.top, previous_part.width, previous_part.height)
        else:
            raise NotImplementedError('Direction not defined')
        
        return new_part