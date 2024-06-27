import pygame
from pygame.locals import *
import map
from sprites import *

class Setup:
    """
    Starts the game according to specified setup.
    """
    def __init__(self):
        pygame.init()
        
        # Game screen size
        self.screen_width = 1760
        self.screen_height = 990

        # Number of FPS
        self.clock = pygame.time.Clock()

        # Set screen size
        self.screen = pygame.display.set_mode((self.screen_width,self.
                                               screen_height))
        pygame.display.set_caption('Maze Runner')

        # Variables that stops the game when set to false
        self.running = True

        # Default variables to what page should be running
        self.main_page = True
        self.instruction_page = False
        self.game_page = False
        self.difficulty_page = False

        # Game background
        self.hell_bg = pygame.image.load('img\hell.jpg')
        self.hell_bg_resized = pygame.transform.scale(self.hell_bg, (self.screen_width, self.screen_height))

        # Button parameters
        self.b_height = 120
        self.b_width = 220
        self.b_x = (self.screen_width - self.b_width) // 2
        self.b_color = (79, 6, 6)

        # Buttons and placement in screen
        self.start_button = button(x=self.b_x, y=200, width=self.b_width, height=self.b_height, color=self.b_color, name="Escape") # start button
        self.instruction_button = button(x=self.b_x, y=350, width=self.b_width, height=self.b_height, color=self.b_color, name="Instruction") # instruction button
        self.back_button = button(x=self.b_x, y=350, width=self.b_width, height=self.b_height, color=self.b_color, name="Back") # back button
        self.easy_button = button(x=500, y=250, width=self.b_width, height=self.b_height, color=self.b_color, name="easy") # easy button
        self.medium_button = button(x=1040, y=250, width=self.b_width, height=self.b_height, color=self.b_color, name="medium") # medium button
        self.hard_button = button(x=500, y=400, width=self.b_width, height=self.b_height, color=self.b_color, name="hard") # hard button
        self.god_button = button(x=1040, y=400, width=self.b_width, height=self.b_height, color=self.b_color, name="god") # god button
        self.custom_button = button(x=self.b_x, y=550, width=self.b_width, height=self.b_height, color=self.b_color, name="custom") # custom button
        self.back_m_button = button(x=self.b_x, y=700, width=self.b_width, height=self.b_height, color=self.b_color, name="back") # back to main button
        self.quit_button = button(x=1650, y=15, width=75, height=30, color=self.b_color, name="quit") # quit button

        # Position of the player
        self.current_pos = None
        self.current_pos_a = None

        # Game mode
        self.mode = None

        # Maze positions
        self.pos = []

    def run(self):
        while self.running:
            # Show the background and design (Take note that the order matters to show all images)
            self.screen.blit(self.hell_bg_resized, (0,0))

            # show the elements depending on the page
            if self.game_page:
                # Draw the mode
                self.mode.draw(self.screen)

                # Draw quit button
                self.quit_button.draw(self.screen, (18, 1, 1), 30)

                # Draw player if there is a valid position
                if self.current_pos != None:
                    self.mode.player.draw(self.screen, self.current_pos)

                    # Draw agent position
                    self.mode.a_agent.draw(self.screen, self.current_pos_a)

            elif self.main_page:
                self.start_button.draw(self.screen, (18, 1, 1), 60)
                self.instruction_button.draw(self.screen, (18, 1, 1),42)

            elif self.instruction_page:
                self.start_button.draw(self.screen, (18, 1, 1), 60)
                self.back_button.draw(self.screen, (18, 1, 1), 60) 

            elif self.difficulty_page:
                self.easy_button.draw(self.screen, (18, 1, 1), 60) 
                self.medium_button.draw(self.screen, (18, 1, 1), 60) 
                self.hard_button.draw(self.screen, (18, 1, 1), 60) 
                self.god_button.draw(self.screen, (18, 1, 1), 60) 
                self.custom_button.draw(self.screen, (18, 1, 1), 60) 
                self.back_m_button.draw(self.screen, (18, 1, 1), 60) 

            # Handle all events
            self.event_handler()

            # Limit fps to 60
            self.clock.tick(60)

            # Update the frame at each iteration
            pygame.display.update()

        pygame.quit()

    def event_handler(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # If the game is closed
            if event.type == pygame.QUIT:
                self.running = False

            # Check the events in the game page            
            if self.game_page:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button.is_over(pos):
                        #print('quit button clicked')
                        self.current_pos = None
                        self.game_page = False
                        self.main_page = True

                    # Check through all pathway
                    for block, type in self.mode.maze_maam.path_format:
                        # block[1][0] = x coord, block[1][1] = y coord, block[1][2] = block_width, block[1][3] = block_height,
                            if pos[0] > block[1][0] and pos[0] < block[1][0] + block[1][2]:
                                if pos[1] > block[1][1] and pos[1] < block[1][1] + block[1][3]:
                                    if self.mode.player.check_place((block[1][0],block[1][1]), self.mode.maze_maam.path_format[0][0][1][2]):
                                        # Modify the position of Human Player and Remove adjacent clouds
                                        self.current_pos = (block[1][0],block[1][1])
                                        self.mode.fog_maam.remove_adjacent_smokes(self.current_pos, block[1][2])

                                        # Modify the agent position
                                        self.current_pos_a = self.mode.a_agent.best_move()
                                        self.mode.fog_a.remove_adjacent_smokes(self.current_pos_a, block[1][2])

                if event.type == pygame.MOUSEMOTION:
                    if self.quit_button.is_over(pos):
                        self.quit_button.color = (38, 3, 3)
                    else:
                        self.quit_button.color = self.b_color

            # Check the events in the main page
            elif self.main_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        #print('start button clicked')
                        self.main_page = False
                        self.difficulty_page = True
                    if self.instruction_button.is_over(pos):
                        #print('instruction button clicked')
                        self.main_page = False
                        self.instruction_page = True

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = (38, 3, 3)
                    else:
                        self.start_button.color = self.b_color

                    if self.instruction_button.is_over(pos):
                        self.instruction_button.color = (38, 3, 3)
                    else:
                        self.instruction_button.color = self.b_color

            # Check the events in the difficulty page
            elif self.difficulty_page:
                # If the mouse is click check through all possible difficulty level
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Go back to main page
                    if self.back_m_button.is_over(pos):
                        #print('back button clicked')
                        self.difficulty_page = False
                        self.main_page = True

                    # Set the mode of the game and switch to gamepage
                    if self.easy_button.is_over(pos):
                        font_list = [('BFS', (520,300)), ('DFS', (520,770)), ('A', (1320,770))]
                        maze_list = [(150, 150,  map.easy), (1450, 600,  map.easy), (1450, 150,  map.easy), (150, 600,  map.easy)]
                        self.mode = mode(font_list, maze_list, 50)

                        self.difficulty_page = False
                        self.game_page = True

                    elif self.medium_button.is_over(pos):
                        font_list = [('BFS', (720,250)), ('DFS', (720,770)), ('A', (1070,770))]
                        maze_list = [(150, 50, map.medium), (1200, 550,  map.medium), (1200, 50,  map.medium), (150, 550,  map.medium)]
                        self.mode = mode(font_list, maze_list, 48)

                        self.difficulty_page = False
                        self.game_page = True

                    elif self.hard_button.is_over(pos):
                        font_list = [('BFS', (720,250)), ('DFS', (720,770)), ('A', (1085,770))]
                        maze_list = [(150, 50, map.hard), (1200, 500,  map.hard), (1200, 50,  map.hard), (150, 500,  map.hard)]
                        self.mode = mode(font_list, maze_list,34)

                        self.difficulty_page = False
                        self.game_page = True

                    elif self.god_button.is_over(pos):
                        font_list = [('BFS', (670,250)), ('DFS', (670,755)), ('A', (1100,755))]
                        maze_list = [(125, 20, map.god), (1200, 500,  map.god), (1200, 20,  map.god), (125, 500,  map.god)]
                        self.mode = mode(font_list, maze_list, 20)

                        self.difficulty_page = False
                        self.game_page = True
                    elif self.custom_button.is_over(pos):
                        font_list = [('BFS', (670,30)), ('DFS', (670,950)), ('A', (1070,950))]
                        maze_list = [(100, 150, map.custom), (1000, 600,  map.custom), (1000, 150,  map.custom), (100, 600,  map.custom)]
                        fog, map_size = map.calc_custom()
                        self.mode = mode(font_list, maze_list, fog, map_size)

                        self.difficulty_page = False
                        self.game_page = True
                        
                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.easy_button.is_over(pos):
                        self.easy_button.color = (38, 3, 3)
                    else:
                        self.easy_button.color = self.b_color

                    if self.medium_button.is_over(pos):
                        self.medium_button.color = (38, 3, 3)
                    else:
                        self.medium_button.color = self.b_color
            
                    if self.hard_button.is_over(pos):
                        self.hard_button.color = (38, 3, 3)
                    else:
                        self.hard_button.color = self.b_color
            
                    if self.god_button.is_over(pos):
                        self.god_button.color = (38, 3, 3)
                    else:
                        self.god_button.color = self.b_color

                    if self.custom_button.is_over(pos):
                        self.custom_button.color = (38, 3, 3)
                    else:
                        self.custom_button.color = self.b_color
            
                    if self.back_m_button.is_over(pos):
                        self.back_m_button.color = (38, 3, 3)
                    else:
                        self.back_m_button.color = self.b_color
            
            # Check the events in the instruction page
            elif self.instruction_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        #print('start button clicked')
                        self.instruction_page = False
                        self.difficulty_page = True
                    if self.back_button.is_over(pos):
                        #print('back button clicked')
                        self.instruction_page = False
                        self.main_page = True

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = (38, 3, 3)
                    else:
                        self.start_button.color = self.b_color

                    if self.instruction_button.is_over(pos):
                        self.instruction_button.color = (38, 3, 3)
                    else:
                        self.instruction_button.color = self.b_color