import pygame
from pygame.locals import *
import map
from sprites import *
import os
import pyautogui

class Setup:
    """
    Starts the game according to specified setup.
    """
    def __init__(self):
        os.system("cls || clear")
        print('\ngame start:')
        pygame.init()
        # Game screen size
        self.screen_width, self.screen_height = pyautogui.size()

        # Adjustment on screen size
        self.screen_width = int(self.screen_width * 0.9)
        self.screen_height = int(self.screen_height * 0.9)

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
        self.lose_page = False
        self.win_page = False

        # Game background
        self.hell_bg = pygame.image.load('img\hell.jpg')
        self.hell_bg_resized = pygame.transform.scale(self.hell_bg, (self.screen_width, self.screen_height))

        # Define the margin
        self.margin = 15

        # Button parameters
        self.b_height = int(self.screen_height / 8)
        self.b_width = int(self.screen_width / 8)

        # X Position settings
        self.center_x = (self.screen_width - self.b_width) // 2
        self.left_x = ((self.screen_width - self.b_width) // 2) - 250
        self.right_x = ((self.screen_width - self.b_width) // 2) + 250
        self.upper_right_x = self.screen_width - self.margin

        # Y Position settings
        self.center_y = (self.screen_height - self.b_height) // 2
        self.upper_y = ((self.screen_height - self.b_height) // 2) - 50
        self.upper_2y = ((self.screen_height - self.b_height) // 2) - 200
        self.lower_y = ((self.screen_height - self.b_height) // 2) + 70
        self.lower_2y = ((self.screen_height - self.b_height) // 2) + 220

        # Quadrants
        self.quadrant1 = (0, 0)  # Upper left
        self.quadrant2 = (self.screen_width // 2, 0)  # Upper right
        self.quadrant3 = (0, self.screen_height // 2)  # Lower left
        self.quadrant4 = (self.screen_width // 2, self.screen_height // 2)  # Lower right

        # Quadrants' bottom-right coordinates
        self.quadrant1_end = (self.screen_width // 2 - 1, self.screen_height // 2 - 1)  # End of upper left
        self.quadrant2_end = (self.screen_width - 1, self.screen_height // 2 - 1)  # End of upper right
        self.quadrant3_end = (self.screen_width // 2 - 1, self.screen_height - 1)  # End of lower left
        self.quadrant4_end = (self.screen_width - 1, self.screen_height - 1)  # End of lower right

        # Tile size
        self.tile_size_easy = int((self.screen_width // 2 - 1) * .07)
        self.tile_size_medium = int((self.screen_width // 2 - 1)* .05)
        self.tile_size_hard = int((self.screen_width // 2 - 1)* .035)
        self.tile_size_god = int((self.screen_width // 2 - 1)* .027)
        print(self.tile_size_god)
        

        # Button positions and colors
        self.b_x_center = self.center_x
        self.b_x_left = self.left_x
        self.b_x_right = self.right_x
        self.b_color = (92, 64, 51)
        self.b_color_hover = (46, 32, 26)

        # Buttons and placement in screen
        self.start_button = button(x=self.b_x_center, y=self.upper_2y, width=self.b_width, height=self.b_height, color=self.b_color, name="Escape") # start button
        self.instruction_button = button(x=self.b_x_center, y=self.upper_y, width=self.b_width, height=self.b_height, color=self.b_color, name="Instruction") # instruction button

        self.start_inst_button = button(x=(self.upper_right_x - 190), y=self.margin, width=100, height=30, color=self.b_color, name="Escape") # start instruction button
        self.back_button = button(x=(self.upper_right_x - 75), y=self.margin, width=75, height=30, color=self.b_color, name="Back") # back button

        self.easy_button = button(x=self.b_x_left, y=self.upper_2y, width=self.b_width, height=self.b_height, color=self.b_color, name="easy") # easy button
        self.medium_button = button(x=self.b_x_right, y=self.upper_2y, width=self.b_width, height=self.b_height, color=self.b_color, name="medium") # medium button
        self.hard_button = button(x=self.b_x_left, y=self.upper_y, width=self.b_width, height=self.b_height, color=self.b_color, name="hard") # hard button
        self.god_button = button(x=self.b_x_right, y=self.upper_y, width=self.b_width, height=self.b_height, color=self.b_color, name="god") # god button
        self.custom_button = button(x=self.b_x_center, y=self.lower_y, width=self.b_width, height=self.b_height, color=self.b_color, name="custom") # custom button
        self.back_m_button = button(x=self.b_x_center, y=self.lower_2y, width=self.b_width, height=self.b_height, color=self.b_color, name="back") # back to main button

        self.quit_button = button(x=self.upper_right_x - 75, y=self.margin, width=75, height=30, color=self.b_color, name="quit") # quit button

        self.main_button = button(x=self.b_x_center, y=self.center_y, width=self.b_width, height=self.b_height, color=self.b_color, name="Main") # Go back to Main button
        
        # Texts
        self.lost = Font('WA HA HA Bonak', (self.screen_width / 2, 200))
        self.won = Font('Ano gusto mo congrats?', (self.screen_width / 2, 200))

        # Position of the player
        self.current_pos = None
        self.current_pos_a = None
        self.current_pos_dfs = None
        self.current_pos_bfs = None

        # Game mode
        self.mode = None

        # Maze positions
        self.pos = []

        # Print Debugging
        #print(self.quadrant1,self.quadrant2,self.quadrant3,self.quadrant4)
        #print(self.quadrant1_end,self.quadrant2_end,self.quadrant3_end,self.quadrant4_end)
        #print('screen size: ',self.screen_width, self.screen_height)

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
                    self.mode.a_agent.draw(self.screen, self.current_pos_a) # a agent
                    self.mode.dfs_agent.draw(self.screen, self.current_pos_dfs) # dfs agent
                    self.mode.bfs_agent.draw(self.screen, self.current_pos_bfs) # bfs agent

            elif self.main_page:
                self.start_button.draw(self.screen, (18, 1, 1), self.start_button.height // 2)
                self.instruction_button.draw(self.screen, (18, 1, 1), (self.instruction_button.height // 2) - 15)

                # Revert all the position to none
                self.current_pos = None
                self.current_pos_a = None
                self.current_pos_dfs = None
                self.current_pos_bfs = None

            elif self.instruction_page:
                self.start_inst_button.draw(self.screen, (18, 1, 1), self.start_inst_button.height // 2)
                self.back_button.draw(self.screen, (18, 1, 1), self.back_button.height // 2) 

            elif self.difficulty_page:
                self.easy_button.draw(self.screen, (18, 1, 1), self.easy_button.height // 2) 
                self.medium_button.draw(self.screen, (18, 1, 1), self.medium_button.height // 2) 
                self.hard_button.draw(self.screen, (18, 1, 1), self.hard_button.height // 2) 
                self.god_button.draw(self.screen, (18, 1, 1), self.god_button.height // 2) 
                self.custom_button.draw(self.screen, (18, 1, 1), self.custom_button.height // 2) 
                self.back_m_button.draw(self.screen, (18, 1, 1), self.back_m_button.height // 2) 
            elif self.win_page:
                self.won.draw(self.screen) 
                self.main_button.draw(self.screen, (18, 1, 1), self.main_button.height // 2)
            elif self.lose_page:
                self.lost.draw(self.screen) 
                self.main_button.draw(self.screen, (18, 1, 1), self.main_button.height // 2)

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
                        self.current_pos = None
                        self.game_page = False
                        self.main_page = True

                    # Check through all maam pathway
                    for block, type in self.mode.maze_maam.path_format:
                        # block[1][0] = x coord, block[1][1] = y coord, block[1][2] = block_width, block[1][3] = block_height,
                            if pos[0] > block[1][0] and pos[0] < block[1][0] + block[1][2]:
                                if pos[1] > block[1][1] and pos[1] < block[1][1] + block[1][3]:
                                    if self.mode.player.check_place((block[1][0],block[1][1]), self.mode.maze_maam.path_format[0][0][1][2]):
                                        self.update_move_and_map(block)

                                        # if red power found
                                        self.red_power(block)

                                        # if blue power found
                                        self.blue_power(block)

                                        # if violet power found
                                        self.violet_power(block)

                    for block, type in self.mode.maze_maam.portal_format:
                        if pos[0] > block[1][0] and pos[0] < block[1][0] + block[1][2]:
                                if pos[1] > block[1][1] and pos[1] < block[1][1] + block[1][3]:
                                    self.win_page = True
                                    self.game_page = False

                if event.type == pygame.MOUSEMOTION:
                    if self.quit_button.is_over(pos):
                        self.quit_button.color = self.b_color_hover
                    else:
                        self.quit_button.color = self.b_color

                # Check if the player already lost
                for block, type in self.mode.maze_a.portal_format: # maze A
                    if self.current_pos_a == (block[1][0],block[1][1]):
                        self.game_page = False
                        self.lose_page = True
                
                for block, type in self.mode.maze_dfs.portal_format: # maze DFS
                    if self.current_pos_dfs == (block[1][0],block[1][1]):
                        self.game_page = False
                        self.lose_page = True

                for block, type in self.mode.maze_bfs.portal_format: # maze DFS
                    if self.current_pos_bfs == (block[1][0],block[1][1]):
                        self.game_page = False
                        self.lose_page = True

            # Check the events in the main page
            elif self.main_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        self.main_page = False
                        self.difficulty_page = True
                    if self.instruction_button.is_over(pos):
                        self.main_page = False
                        self.instruction_page = True

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = self.b_color_hover
                    else:
                        self.start_button.color = self.b_color

                    if self.instruction_button.is_over(pos):
                        self.instruction_button.color = self.b_color_hover
                    else:
                        self.instruction_button.color = self.b_color

            # Check the events in the difficulty page
            elif self.difficulty_page:
                # If the mouse is click check through all possible difficulty level
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Go back to main page
                    if self.back_m_button.is_over(pos):
                        self.difficulty_page = False
                        self.main_page = True

                    # Set the mode of the game and switch to gamepage
                    if self.easy_button.is_over(pos):
                        font_list = [('BFS', (self.quadrant1_end[0] - int(self.quadrant1_end[0]*.3) ,self.quadrant1_end[1] - int(self.quadrant1_end[1]*.5))), 
                                     ('A*', (self.quadrant3_end[0] - int(self.quadrant1_end[0]*.3) ,self.quadrant3_end[1] - int(self.quadrant3_end[1]*.25))), 
                                     ('DFS', (self.quadrant4_end[0] - int(self.quadrant1_end[0]*.3) ,self.quadrant4_end[1] - int(self.quadrant4_end[1]*.25)))]
                        # UPPER LEFT, LOWER RIGHT, UPPER RIGHT, LOWER LEFT
                        maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+30,  map.easy), (self.quadrant4[0]+100, self.quadrant4[1]+30,  map.easy), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+30,  map.easy), (self.quadrant3[0]+100, self.quadrant3[1]+30,  map.easy)]
                        self.mode = mode(font_list, maze_list, 50, self.tile_size_easy)

                        self.difficulty_page = False
                        self.game_page = True

                    elif self.medium_button.is_over(pos):
                        font_list = [('BFS', (self.quadrant1_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant1_end[1] - int(self.quadrant1_end[1]*.5))), 
                                     ('A*', (self.quadrant3_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant3_end[1] - int(self.quadrant3_end[1]*.25))), 
                                     ('DFS', (self.quadrant4_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant4_end[1] - int(self.quadrant4_end[1]*.25)))]
                        maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+20,  map.medium), (self.quadrant4[0]+100, self.quadrant4[1]+20,  map.medium), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+20,  map.medium), (self.quadrant3[0]+100, self.quadrant3[1]+20,  map.medium)]
                        self.mode = mode(font_list, maze_list, 48, self.tile_size_medium)

                        self.difficulty_page = False
                        self.game_page = True

                    elif self.hard_button.is_over(pos):
                        font_list = [('BFS', (self.quadrant1_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant1_end[1] - int(self.quadrant1_end[1]*.5))), 
                                     ('A*', (self.quadrant3_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant3_end[1] - int(self.quadrant3_end[1]*.25))), 
                                     ('DFS', (self.quadrant4_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant4_end[1] - int(self.quadrant4_end[1]*.25)))]
                        maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+20,  map.hard), (self.quadrant4[0]+100, self.quadrant4[1]+20,  map.hard), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+20,  map.hard), (self.quadrant3[0]+100, self.quadrant3[1]+20,  map.hard)]
                        self.mode = mode(font_list, maze_list,34, self.tile_size_hard)

                        self.difficulty_page = False
                        self.game_page = True

                    elif self.god_button.is_over(pos):
                        font_list = [('BFS', (self.quadrant1_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant1_end[1] - int(self.quadrant1_end[1]*.5))), 
                                     ('A', (self.quadrant3_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant3_end[1] - int(self.quadrant3_end[1]*.25))), 
                                     ('DFS', (self.quadrant4_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant4_end[1] - int(self.quadrant4_end[1]*.25)))]
                        maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+10,  map.god), (self.quadrant4[0]+100, self.quadrant4[1]+10,  map.god), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+10,  map.god), (self.quadrant3[0]+100, self.quadrant3[1]+10,  map.god)]
                        self.mode = mode(font_list, maze_list, 20, self.tile_size_god)

                        self.difficulty_page = False
                        self.game_page = True
                    elif self.custom_button.is_over(pos):
                        font_list = [('BFS', (self.quadrant1_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant1_end[1] - int(self.quadrant1_end[1]*.5))), 
                                     ('A', (self.quadrant3_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant3_end[1] - int(self.quadrant3_end[1]*.25))), 
                                     ('DFS', (self.quadrant4_end[0] - int(self.quadrant1_end[0]*.20) ,self.quadrant4_end[1] - int(self.quadrant4_end[1]*.25)))]
                        size = map.calc_custom()
                        # Map sizes
                        if size == 6:
                            font_list = [('BFS', (self.quadrant1_end[0] - int(self.quadrant1_end[0]*.3) ,self.quadrant1_end[1] - int(self.quadrant1_end[1]*.5))), 
                                     ('A', (self.quadrant3_end[0] - int(self.quadrant1_end[0]*.3) ,self.quadrant3_end[1] - int(self.quadrant3_end[1]*.25))), 
                                     ('DFS', (self.quadrant4_end[0] - int(self.quadrant1_end[0]*.3) ,self.quadrant4_end[1] - int(self.quadrant4_end[1]*.25)))]
                            maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+30,  map.easy), (self.quadrant4[0]+100, self.quadrant4[1]+30,  map.easy), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+30,  map.easy), (self.quadrant3[0]+100, self.quadrant3[1]+30,  map.easy)]
                            fog = 50
                            tile = self.tile_size_easy
                        elif size == 10:
                            maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+20,  map.medium), (self.quadrant4[0]+100, self.quadrant4[1]+20,  map.medium), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+20,  map.medium), (self.quadrant3[0]+100, self.quadrant3[1]+20,  map.medium)]
                            fog = 48
                            tile = self.tile_size_medium
                        elif size == 14:
                            maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+20,  map.hard), (self.quadrant4[0]+100, self.quadrant4[1]+20,  map.hard), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+20,  map.hard), (self.quadrant3[0]+100, self.quadrant3[1]+20,  map.hard)]
                            fog = 34
                            tile = self.tile_size_hard
                        else:
                            maze_list = [(self.quadrant1[0]+100, self.quadrant1[1]+10,  map.god), (self.quadrant4[0]+100, self.quadrant4[1]+10,  map.god), 
                                     (self.quadrant2[0]+100, self.quadrant2[1]+10,  map.god), (self.quadrant3[0]+100, self.quadrant3[1]+10,  map.god)]
                            fog = 20
                            tile = self.tile_size_god

                        self.mode = mode(font_list, maze_list, fog, tile)

                        self.difficulty_page = False
                        self.game_page = True
                        
                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.easy_button.is_over(pos):
                        self.easy_button.color = self.b_color_hover
                    else:
                        self.easy_button.color = self.b_color

                    if self.medium_button.is_over(pos):
                        self.medium_button.color = self.b_color_hover
                    else:
                        self.medium_button.color = self.b_color
            
                    if self.hard_button.is_over(pos):
                        self.hard_button.color = self.b_color_hover
                    else:
                        self.hard_button.color = self.b_color
            
                    if self.god_button.is_over(pos):
                        self.god_button.color = self.b_color_hover
                    else:
                        self.god_button.color = self.b_color

                    if self.custom_button.is_over(pos):
                        self.custom_button.color = self.b_color_hover
                    else:
                        self.custom_button.color = self.b_color
            
                    if self.back_m_button.is_over(pos):
                        self.back_m_button.color = self.b_color_hover
                    else:
                        self.back_m_button.color = self.b_color
            
            # Check the events in the instruction page
            elif self.instruction_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_inst_button.is_over(pos):
                        self.instruction_page = False
                        self.difficulty_page = True
                    if self.back_button.is_over(pos):
                        self.instruction_page = False
                        self.main_page = True

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.start_inst_button.is_over(pos):
                        self.start_inst_button.color = self.b_color_hover
                    else:
                        self.start_inst_button.color = self.b_color

                    if self.back_button.is_over(pos):
                        self.back_button.color = self.b_color_hover
                    else:
                        self.back_button.color = self.b_color
            elif self.lose_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_button.is_over(pos):
                        self.main_page = True
                        self.lose_page = False

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.main_button.is_over(pos):
                        self.main_button.color = self.b_color_hover
                    else:
                        self.main_button.color = self.b_color
            elif self.win_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_button.is_over(pos):
                        self.main_page = True
                        self.win_page = False

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.main_button.is_over(pos):
                        self.main_button.color = self.b_color_hover
                    else:
                        self.main_button.color = self.b_color   

    def update_move_and_map(self, block):
        # Modify the position of Human Player and Remove adjacent clouds
        self.current_pos = (block[1][0],block[1][1])
        self.mode.player.update_path(self.current_pos, block[1][2])
        self.mode.fog_maam.remove_adjacent_smokes(self.current_pos, block[1][2])

        # Modify the position of the AI and Remove adjacent clouds
        self.current_pos_a = self.mode.a_agent.best_move() # A agent modified
        self.mode.a_agent.update_path(self.current_pos_a)
        self.mode.fog_a.remove_adjacent_smokes(self.current_pos_a, block[1][2])

        self.current_pos_dfs = self.mode.dfs_agent.move() # dfs agent modified
        self.mode.dfs_agent.update_path(self.current_pos_dfs)
        self.mode.fog_dfs.remove_adjacent_smokes(self.current_pos_dfs, block[1][2])

        self.current_pos_bfs = self.mode.bfs_agent.move() # bfs agent modified
        self.mode.bfs_agent.update_path(self.current_pos_bfs)
        self.mode.fog_bfs.remove_adjacent_smokes(self.current_pos_bfs, block[1][2])
    
    def red_power(self, block):
        if self.mode.red_power_a_img: # A agent
            if self.current_pos_a == self.mode.red_power_a.pos:
                # change current position of agent to a random place,can be explored or not explored
                self.current_pos_a = self.mode.red_power_a.random_add()

                # Update fog
                self.mode.fog_a.remove_adjacent_smokes(self.current_pos_a, block[1][2])
                self.mode.fog_a.remove_current_smoke(self.current_pos_a, block[1][2])

                # Update explored, unexplored, and can explore paths
                self.mode.a_agent.update_path(self.current_pos_a)

        if self.mode.red_power_dfs_img: # Dfs agent
            if self.current_pos_dfs == self.mode.red_power_dfs.pos:
                # change current position of agent to a random place,can be explored or not explored
                self.current_pos_dfs = self.mode.red_power_dfs.random_add()

                # Update fog
                self.mode.fog_dfs.remove_adjacent_smokes(self.current_pos_dfs, block[1][2])
                self.mode.fog_dfs.remove_current_smoke(self.current_pos_dfs, block[1][2])

                # Update explored, unexplored, and can explroe paths
                self.mode.dfs_agent.update_path(self.current_pos_dfs)

        if self.mode.red_power_bfs_img: # Dfs agent
            if self.current_pos_bfs == self.mode.red_power_bfs.pos:
                # change current position of agent to a random place,can be explored or not explored
                self.current_pos_bfs = self.mode.red_power_bfs.random_add()

                # Update fog
                self.mode.fog_bfs.remove_adjacent_smokes(self.current_pos_bfs, block[1][2])
                self.mode.fog_bfs.remove_current_smoke(self.current_pos_bfs, block[1][2])

                # Update explored, unexplored, and can explroe paths
                self.mode.bfs_agent.update_path(self.current_pos_bfs)    

        if self.mode.red_power_maam_img: # Player
            if self.current_pos == self.mode.red_power_maam.pos:
                # change current position of agent to a random place,can be explored or not explored
                self.current_pos = self.mode.red_power_maam.random_add()

                # Update fog
                self.mode.fog_maam.remove_adjacent_smokes(self.current_pos, block[1][2])
                self.mode.fog_maam.remove_current_smoke(self.current_pos, block[1][2])

                # Update explored, unexplored, and can explroe paths
                self.mode.player.update_path(self.current_pos, block[1][2])

    def blue_power(self, block):
        if self.mode.blue_power_maam_img: # Player
            if self.current_pos == self.mode.blue_power_maam.pos:
                # Move one point closer to the finish point
                self.current_pos = self.mode.blue_power_maam.move_closer(self.mode.player.can_explore)

                # Update fog
                self.mode.fog_maam.remove_adjacent_smokes(self.current_pos, block[1][2])
                self.mode.fog_maam.remove_current_smoke(self.current_pos, block[1][2])

                # Update explored, unexplored, and can explroe paths
                self.mode.player.update_path(self.current_pos, block[1][2])

        if self.mode.blue_power_a_img: # A agent
            if self.current_pos_a == self.mode.blue_power_a.pos:
                # Move one point closer to the finish point
                inner_tuples = [outer for outer in self.mode.a_agent.can_explore]
                innest_tuples = [tuples for tuples, value in inner_tuples]
                self.current_pos_a = self.mode.blue_power_a.move_closer(innest_tuples)

                # Update fog
                self.mode.fog_a.remove_adjacent_smokes(self.current_pos_a, block[1][2])
                self.mode.fog_a.remove_current_smoke(self.current_pos_a, block[1][2])

                # Update explored, unexplored, and can explore paths
                self.mode.a_agent.update_path(self.current_pos_a)

        if self.mode.blue_power_dfs_img: # Dfs agent
            if self.current_pos_dfs == self.mode.blue_power_dfs.pos:
                # Move one point closer to the finish point
                self.current_pos_dfs = self.mode.blue_power_dfs.move_closer(self.mode.dfs_agent.can_explore)

                # Update fog
                self.mode.fog_dfs.remove_adjacent_smokes(self.current_pos_dfs, block[1][2])
                self.mode.fog_dfs.remove_current_smoke(self.current_pos_dfs, block[1][2])

                # Update explored, unexplored, and can explroe paths
                self.mode.dfs_agent.update_path(self.current_pos_dfs)

        if self.mode.blue_power_bfs_img: # Bfs agent
            if self.current_pos_bfs == self.mode.blue_power_bfs.pos:
                # Move one point closer to the finish point
                self.current_pos_bfs = self.mode.blue_power_bfs.move_closer(self.mode.bfs_agent.can_explore)

                # Update fog
                self.mode.fog_bfs.remove_adjacent_smokes(self.current_pos_bfs, block[1][2])
                self.mode.fog_bfs.remove_current_smoke(self.current_pos_bfs, block[1][2])

                # Update explored, unexplored, and can explroe paths
                self.mode.bfs_agent.update_path(self.current_pos_bfs)   

    def violet_power(self, block):
        if self.mode.violet_power_a_img: # A agent
            if self.current_pos_a == self.mode.violet_power_a.pos:
                pass

        if self.mode.violet_power_dfs_img: # Dfs agent
            if self.current_pos_dfs == self.mode.violet_power_dfs.pos:
                pass

        if self.mode.violet_power_bfs_img: # Dfs agent
            if self.current_pos_bfs == self.mode.violet_power_bfs.pos:
               pass  

        if self.mode.violet_power_maam_img: # Player
            if self.current_pos == self.mode.violet_power_maam.pos:
                pass
            