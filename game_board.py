import pygame

class main_board:
    def __init__(self, height, width, caption):
        self._running = True
        self._display_surf = None
        self._height = height
        self._width = width
        self._caption = caption
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self._width, self._height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(self._caption)
        self._running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def draw_title(self, title):
        font = pygame.font.SysFont("inconsolata, consolas, monospace", 30, bold=False, italic=False)
        text_surf = font.render(title, True, (255, 255, 255))
        rect_surf = pygame.Surface((200, 40))
        white_surf = pygame.Surface((210, 50))
        white_surf.fill((255, 255, 255))
        rect_surf.blit(text_surf, text_surf.get_rect(center = rect_surf.get_rect().center))
        white_surf.blit(rect_surf, rect_surf.get_rect(center = white_surf.get_rect().center))
        self._display_surf.blit(white_surf, white_surf.get_rect(center = (self._width//2, 30)))
    def draw_next_piece_box(self):
        font = pygame.font.SysFont("inconsolata, consolas, monospace", 30, bold=False, italic=False)
        text_surf = font.render("Next Piece", True, (255, 255, 255))
        rect_surf = pygame.Surface((190, 190))
        white_surf = pygame.Surface((200, 200))
        white_surf.fill((255, 255, 255))
        rect_surf.blit(text_surf, text_surf.get_rect(center = (rect_surf.get_width()//2, 20)))
        white_surf.blit(rect_surf, rect_surf.get_rect(center = white_surf.get_rect().center))
        self._display_surf.blit(white_surf, white_surf.get_rect(center = (430, 200)))
    
    def draw_score_board(self):
        title_font = pygame.font.SysFont("inconsolata, consolas, monospace", 30, bold=False, italic=False)
        title_surf = title_font.render("Scores", True, (255, 255, 255))
        player_font = pygame.font.SysFont("inconsolata, consolas, monospace", 20, italic=False)
        player1_surf = player_font.render("Player:", True, (255, 255, 255))
        player2_surf = player_font.render("AI:", True, (255, 255, 255))
        rect_surf = pygame.Surface((190, 90))
        surf_width_center = rect_surf.get_width()//2
        surf_List = (
            (title_surf, title_surf.get_rect(center = (surf_width_center, 20))),
            (player1_surf, player1_surf.get_rect(center = (surf_width_center-50, 50))),
            (player2_surf, player2_surf.get_rect(center = (surf_width_center-30, 80)))
        )
        rect_surf.blits(surf_List)
        white_surf = pygame.Surface((200, 100))
        white_surf.fill((255, 255, 255))
        white_surf.blit(rect_surf, rect_surf.get_rect(center = white_surf.get_rect().center))
        self._display_surf.blit(white_surf, white_surf.get_rect(center = (430, 360)))
   
    def draw_control_instrcutions(self):
        title_font = pygame.font.SysFont("inconsolata, consolas, monospace", 30, bold=False, italic=False)
        title_surf = title_font.render("Controls", True, (255, 255, 255))
        instr_font = pygame.font.SysFont("inconsolata, consolas, monospace", 11, italic=False)
        up_surf = instr_font.render("up key : rotate piece", True, (255, 255, 255))
        down_surf = instr_font.render("down key : move piece down", True, (255, 255, 255))
        left_surf = instr_font.render("left key : move piece left", True, (255, 255, 255))
        right_surf = instr_font.render("right key : move piece right", True, (255, 255, 255))
        rect_surf = pygame.Surface((190, 170))
        surf_width_center = rect_surf.get_width()//2
        surf_List = (
            (title_surf, title_surf.get_rect(center = (surf_width_center, 20))),
            (up_surf, up_surf.get_rect(center = (surf_width_center-25, 50))),
            (down_surf, down_surf.get_rect(center = (surf_width_center-10, 80))),
            (left_surf, left_surf.get_rect(center = (surf_width_center-13, 110))),
            (right_surf, right_surf.get_rect(center = (surf_width_center-4, 140)))
        )
        rect_surf.blits(surf_List)
        white_surf = pygame.Surface((200, 180))
        white_surf.fill((255, 255, 255))
        white_surf.blit(rect_surf, rect_surf.get_rect(center = white_surf.get_rect().center))
        self._display_surf.blit(white_surf, white_surf.get_rect(center = (430, 510)))

    def draw_turn_box(self):
        title_font = pygame.font.SysFont("inconsolata, consolas, monospace", 20, bold=False, italic=False)
        title_surf = title_font.render("Turn : Player", True, (255, 255, 255))
        rect_surf = pygame.Surface((190, 30))
        rect_surf.blit(title_surf, title_surf.get_rect(center=(rect_surf.get_rect().center)))
        white_surf = pygame.Surface((200, 40))
        white_surf.fill((255, 255, 255))
        white_surf.blit(rect_surf, rect_surf.get_rect(center = white_surf.get_rect().center))
        self._display_surf.blit(white_surf, white_surf.get_rect(center = (430, 630)))
    def on_loop(self):
        pass
    def on_render(self, title):
        self.draw_title(title)
        self.draw_next_piece_box()
        self.draw_score_board()
        self.draw_control_instrcutions()
        self.draw_turn_box()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            # self.on_loop()
            self.on_render("Tetris")
        self.on_cleanup()