import pygame
import sys
import random
import time
from data.vocabulary import vocabulary_sets

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)
GREEN = (100, 200, 100)
RED = (200, 100, 100)
YELLOW = (255, 255, 0)

# Game settings
DIFFICULTY_LEVELS = ["Easy (4 pairs)", "Medium (8 pairs)", "Hard (12 pairs)"]
VOCABULARY_THEMES = ["General", "Business", "Science", "Travel"]

class Card:
    def __init__(self, x, y, width, height, content, card_type):
        self.rect = pygame.Rect(x, y, width, height)
        self.content = content
        self.card_type = card_type  # "word" or "definition"
        self.is_flipped = False
        self.is_matched = False
        self.font = pygame.font.SysFont('Arial', 16)
    
    def draw(self, screen):
        if self.is_matched:
            color = GREEN
        elif self.is_flipped:
            color = WHITE
        else:
            color = BLUE
            
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        
        if self.is_flipped or self.is_matched:
            # Wrap text to fit in card
            words = self.content.split()
            lines = []
            current_line = ""
            
            for word in words:
                test_line = current_line + word + " "
                if self.font.size(test_line)[0] < self.rect.width - 20:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word + " "
            
            if current_line:
                lines.append(current_line)
            
            # Render each line
            y_offset = 10
            for line in lines:
                text_surface = self.font.render(line, True, BLACK)
                screen.blit(text_surface, (self.rect.x + 10, self.rect.y + y_offset))
                y_offset += self.font.get_height()
        else:
            # Draw card back
            text = self.font.render("?", True, BLACK)
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)
    
    def flip(self):
        if not self.is_matched:
            self.is_flipped = not self.is_flipped
            return True
        return False

class VocabularyGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Vocabulary Flashcards Game")
        self.clock = pygame.time.Clock()
        
        # Load fonts
        self.font_small = pygame.font.SysFont('Arial', 16)
        self.font_medium = pygame.font.SysFont('Arial', 24)
        self.font_large = pygame.font.SysFont('Arial', 36)
        
        # Game state
        self.state = "menu"  # menu, game, review, settings
        self.difficulty_level = DIFFICULTY_LEVELS[0]
        self.vocabulary_theme = VOCABULARY_THEMES[0]
        self.new_words_per_game = 2
        self.show_examples = True
        
        # Game variables
        self.cards = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.total_pairs = 0
        self.incorrect_matches = []
        self.score = 0
        self.start_time = 0
        self.elapsed_time = 0
        
        # Load sounds
        try:
            self.correct_sound = pygame.mixer.Sound('assets/sounds/correct.wav')
            self.incorrect_sound = pygame.mixer.Sound('assets/sounds/incorrect.wav')
            self.win_sound = pygame.mixer.Sound('assets/sounds/win.wav')
            self.sound_enabled = True
        except:
            print("Warning: Sound files not found. Playing without sound.")
            self.sound_enabled = False
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
            
            # Update game logic
            if self.state == "game":
                if self.matched_pairs == self.total_pairs and self.total_pairs > 0:
                    self.elapsed_time = time.time() - self.start_time
                    if self.sound_enabled:
                        self.win_sound.play()
                    self.state = "game_over"
            
            # Draw everything
            if self.state == "menu":
                self.draw_menu()
            elif self.state == "settings":
                self.draw_settings()
            elif self.state == "game":
                self.draw_game()
            elif self.state == "game_over":
                self.draw_game_over()
            elif self.state == "review":
                self.draw_review()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()
    
    def draw_menu(self):
        self.screen.fill(WHITE)
        
        # Title
        title = self.font_large.render("Vocabulary Flashcards Game", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        # Start Game button
        start_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 200, 200, 50)
        pygame.draw.rect(self.screen, BLUE, start_button)
        pygame.draw.rect(self.screen, BLACK, start_button, 2)
        
        start_text = self.font_medium.render("Start Game", True, BLACK)
        start_text_rect = start_text.get_rect(center=start_button.center)
        self.screen.blit(start_text, start_text_rect)
        
        # Settings button
        settings_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 280, 200, 50)
        pygame.draw.rect(self.screen, GRAY, settings_button)
        pygame.draw.rect(self.screen, BLACK, settings_button, 2)
        
        settings_text = self.font_medium.render("Settings", True, BLACK)
        settings_text_rect = settings_text.get_rect(center=settings_button.center)
        self.screen.blit(settings_text, settings_text_rect)
        
        # Quit button
        quit_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 360, 200, 50)
        pygame.draw.rect(self.screen, RED, quit_button)
        pygame.draw.rect(self.screen, BLACK, quit_button, 2)
        
        quit_text = self.font_medium.render("Quit", True, BLACK)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        self.screen.blit(quit_text, quit_text_rect)
        
        # Current settings display
        settings_y = 450
        settings_text = self.font_small.render(f"Current Settings: {self.difficulty_level}, {self.vocabulary_theme} vocabulary", True, BLACK)
        settings_rect = settings_text.get_rect(center=(SCREEN_WIDTH//2, settings_y))
        self.screen.blit(settings_text, settings_rect)
    
    def draw_settings(self):
        self.screen.fill(WHITE)
        
        # Title
        title = self.font_large.render("Settings", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 80))
        self.screen.blit(title, title_rect)
        
        # Difficulty level selection
        diff_y = 150
        diff_text = self.font_medium.render("Difficulty Level:", True, BLACK)
        self.screen.blit(diff_text, (SCREEN_WIDTH//2 - 200, diff_y))
        
        for i, level in enumerate(DIFFICULTY_LEVELS):
            button_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, diff_y + 40 + i*50, 200, 40)
            color = BLUE if self.difficulty_level == level else GRAY
            pygame.draw.rect(self.screen, color, button_rect)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2)
            
            text = self.font_small.render(level, True, BLACK)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)
        
        # Vocabulary theme selection
        theme_y = 350
        theme_text = self.font_medium.render("Vocabulary Theme:", True, BLACK)
        self.screen.blit(theme_text, (SCREEN_WIDTH//2 - 200, theme_y))
        
        for i, theme in enumerate(VOCABULARY_THEMES):
            button_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, theme_y + 40 + i*50, 200, 40)
            color = BLUE if self.vocabulary_theme == theme else GRAY
            pygame.draw.rect(self.screen, color, button_rect)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2)
            
            text = self.font_small.render(theme, True, BLACK)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)
        
        # Back button
        back_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT - 80, 200, 50)
        pygame.draw.rect(self.screen, GRAY, back_button)
        pygame.draw.rect(self.screen, BLACK, back_button, 2)
        
        back_text = self.font_medium.render("Back to Menu", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button.center)
        self.screen.blit(back_text, back_text_rect)
    
    def draw_game(self):
        self.screen.fill(WHITE)
        
        # Draw cards
        for card in self.cards:
            card.draw(self.screen)
        
        # Draw score and timer
        score_text = self.font_medium.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (20, 20))
        
        elapsed = time.time() - self.start_time
        timer_text = self.font_medium.render(f"Time: {int(elapsed)}s", True, BLACK)
        self.screen.blit(timer_text, (SCREEN_WIDTH - 150, 20))
        
        # Draw matched pairs counter
        pairs_text = self.font_medium.render(f"Pairs: {self.matched_pairs}/{self.total_pairs}", True, BLACK)
        self.screen.blit(pairs_text, (SCREEN_WIDTH//2 - 60, 20))
    
    def draw_game_over(self):
        self.screen.fill(WHITE)
        
        # Game over message
        title = self.font_large.render("Game Complete!", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 100))
        self.screen.blit(title, title_rect)
        
        # Score and time
        score_text = self.font_medium.render(f"Final Score: {self.score}", True, BLACK)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 180))
        self.screen.blit(score_text, score_rect)
        
        time_text = self.font_medium.render(f"Time: {int(self.elapsed_time)} seconds", True, BLACK)
        time_rect = time_text.get_rect(center=(SCREEN_WIDTH//2, 220))
        self.screen.blit(time_text, time_rect)
        
        # Review incorrect matches button (if any)
        if self.incorrect_matches:
            review_button = pygame.Rect(SCREEN_WIDTH//2 - 150, 280, 300, 50)
            pygame.draw.rect(self.screen, YELLOW, review_button)
            pygame.draw.rect(self.screen, BLACK, review_button, 2)
            
            review_text = self.font_medium.render("Review Incorrect Matches", True, BLACK)
            review_text_rect = review_text.get_rect(center=review_button.center)
            self.screen.blit(review_text, review_text_rect)
        
        # Back to menu button
        menu_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 360, 200, 50)
        pygame.draw.rect(self.screen, BLUE, menu_button)
        pygame.draw.rect(self.screen, BLACK, menu_button, 2)
        
        menu_text = self.font_medium.render("Back to Menu", True, BLACK)
        menu_text_rect = menu_text.get_rect(center=menu_button.center)
        self.screen.blit(menu_text, menu_text_rect)
        
        # Play again button
        play_again_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 440, 200, 50)
        pygame.draw.rect(self.screen, GREEN, play_again_button)
        pygame.draw.rect(self.screen, BLACK, play_again_button, 2)
        
        play_again_text = self.font_medium.render("Play Again", True, BLACK)
        play_again_text_rect = play_again_text.get_rect(center=play_again_button.center)
        self.screen.blit(play_again_text, play_again_text_rect)
    
    def draw_review(self):
        self.screen.fill(WHITE)
        
        # Title
        title = self.font_large.render("Review Incorrect Matches", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 60))
        self.screen.blit(title, title_rect)
        
        # Display incorrect matches
        y_pos = 120
        for i, (word, definition) in enumerate(self.incorrect_matches):
            word_text = self.font_medium.render(f"Word: {word}", True, BLACK)
            self.screen.blit(word_text, (100, y_pos))
            
            # Wrap definition text
            def_words = definition.split()
            def_lines = []
            current_line = ""
            
            for word in def_words:
                test_line = current_line + word + " "
                if self.font_small.size(test_line)[0] < SCREEN_WIDTH - 200:
                    current_line = test_line
                else:
                    def_lines.append(current_line)
                    current_line = word + " "
            
            if current_line:
                def_lines.append(current_line)
            
            # Render definition lines
            def_y = y_pos + 30
            for line in def_lines:
                def_text = self.font_small.render(line, True, BLACK)
                self.screen.blit(def_text, (120, def_y))
                def_y += 20
            
            y_pos = def_y + 20
            
            # Add separator line
            pygame.draw.line(self.screen, GRAY, (100, y_pos - 10), (SCREEN_WIDTH - 100, y_pos - 10), 1)
            
            # Check if we need to paginate
            if y_pos > SCREEN_HEIGHT - 100:
                break
        
        # Back button
        back_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT - 80, 200, 50)
        pygame.draw.rect(self.screen, GRAY, back_button)
        pygame.draw.rect(self.screen, BLACK, back_button, 2)
        
        back_text = self.font_medium.render("Back", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button.center)
        self.screen.blit(back_text, back_text_rect)
    
    def handle_click(self, pos):
        if self.state == "menu":
            # Start Game button
            start_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 200, 200, 50)
            if start_button.collidepoint(pos):
                self.start_game()
            
            # Settings button
            settings_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 280, 200, 50)
            if settings_button.collidepoint(pos):
                self.state = "settings"
            
            # Quit button
            quit_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 360, 200, 50)
            if quit_button.collidepoint(pos):
                pygame.quit()
                sys.exit()
        
        elif self.state == "settings":
            # Difficulty level buttons
            diff_y = 150
            for i, level in enumerate(DIFFICULTY_LEVELS):
                button_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, diff_y + 40 + i*50, 200, 40)
                if button_rect.collidepoint(pos):
                    self.difficulty_level = level
            
            # Vocabulary theme buttons
            theme_y = 350
            for i, theme in enumerate(VOCABULARY_THEMES):
                button_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, theme_y + 40 + i*50, 200, 40)
                if button_rect.collidepoint(pos):
                    self.vocabulary_theme = theme
            
            # Back button
            back_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT - 80, 200, 50)
            if back_button.collidepoint(pos):
                self.state = "menu"
        
        elif self.state == "game":
            # Check if a card was clicked
            for card in self.cards:
                if card.rect.collidepoint(pos):
                    if len(self.flipped_cards) < 2 and card.flip():
                        self.flipped_cards.append(card)
                        
                        # If two cards are flipped, check for a match
                        if len(self.flipped_cards) == 2:
                            pygame.time.delay(500)  # Brief delay to show the cards
                            self.check_match()
        
        elif self.state == "game_over":
            # Review incorrect matches button
            if self.incorrect_matches:
                review_button = pygame.Rect(SCREEN_WIDTH//2 - 150, 280, 300, 50)
                if review_button.collidepoint(pos):
                    self.state = "review"
            
            # Back to menu button
            menu_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 360, 200, 50)
            if menu_button.collidepoint(pos):
                self.state = "menu"
            
            # Play again button
            play_again_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 440, 200, 50)
            if play_again_button.collidepoint(pos):
                self.start_game()
        
        elif self.state == "review":
            # Back button
            back_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT - 80, 200, 50)
            if back_button.collidepoint(pos):
                self.state = "game_over"
    
    def start_game(self):
        # Reset game variables
        self.cards = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.score = 0
        self.incorrect_matches = []
        
        # Determine number of pairs based on difficulty
        if self.difficulty_level == DIFFICULTY_LEVELS[0]:  # Easy
            self.total_pairs = 4
        elif self.difficulty_level == DIFFICULTY_LEVELS[1]:  # Medium
            self.total_pairs = 8
        else:  # Hard
            self.total_pairs = 12
        
        # Get vocabulary for the selected theme
        vocab_list = vocabulary_sets.get(self.vocabulary_theme.lower(), vocabulary_sets["general"])
        
        # Select random word pairs
        selected_pairs = random.sample(vocab_list, self.total_pairs)
        
        # Create cards
        card_width = 150
        card_height = 100
        margin = 20
        cards_per_row = 4
        
        all_cards = []
        
        for i, (word, definition) in enumerate(selected_pairs):
            # Create word card
            row = i // cards_per_row
            col = i % cards_per_row
            x = margin + col * (card_width + margin)
            y = 80 + row * (card_height + margin)
            word_card = Card(x, y, card_width, card_height, word, "word")
            all_cards.append(word_card)
            
            # Create definition card
            def_card = Card(x, y, card_width, card_height, definition, "definition")
            all_cards.append(def_card)
        
        # Shuffle cards
        random.shuffle(all_cards)
        
        # Position cards in grid
        for i, card in enumerate(all_cards):
            row = i // cards_per_row
            col = i % cards_per_row
            card.rect.x = margin + col * (card_width + margin)
            card.rect.y = 80 + row * (card_height + margin)
        
        self.cards = all_cards
        
        # Show all cards briefly at the start
        self.state = "game"
        self.draw_game()
        pygame.display.flip()
        
        for card in self.cards:
            card.is_flipped = True
        
        self.draw_game()
        pygame.display.flip()
        pygame.time.delay(5000)  # Show cards for 5 seconds
        
        for card in self.cards:
            card.is_flipped = False
        
        # Start the game timer
        self.start_time = time.time()
    
    def check_match(self):
        card1, card2 = self.flipped_cards
        
        # Find the word-definition pair
        word_card = None
        def_card = None
        
        if card1.card_type == "word" and card2.card_type == "definition":
            word_card = card1
            def_card = card2
        elif card1.card_type == "definition" and card2.card_type == "word":
            word_card = card2
            def_card = card1
        
        # Check if the cards match
        if word_card and def_card:
            # Find if this is a correct pair in our vocabulary
            is_match = False
            for word, definition in vocabulary_sets.get(self.vocabulary_theme.lower(), vocabulary_sets["general"]):
                if word_card.content == word and def_card.content == definition:
                    is_match = True
                    break
            
            if is_match:
                # Correct match
                word_card.is_matched = True
                def_card.is_matched = True
                self.matched_pairs += 1
                self.score += 10
                if self.sound_enabled:
                    self.correct_sound.play()
            else:
                # Incorrect match
                word_card.is_flipped = False
                def_card.is_flipped = False
                self.score = max(0, self.score - 2)  # Subtract points but don't go below 0
                self.incorrect_matches.append((word_card.content, def_card.content))
                if self.sound_enabled:
                    self.incorrect_sound.play()
        else:
            # Two words or two definitions - not a match
            card1.is_flipped = False
            card2.is_flipped = False
            self.score = max(0, self.score - 2)
            if self.sound_enabled:
                self.incorrect_sound.play()
        
        # Reset flipped cards
        self.flipped_cards = []

if __name__ == "__main__":
    game = VocabularyGame()
    game.run()
