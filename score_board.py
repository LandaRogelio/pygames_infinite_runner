import pygame


class Score:
    score_text = [] #list of list[score, name]
    font_render = []

    name = False
    score = -1
    pos = -1

    def __init__(self, screen):
        super().__init__()
        self.font = pygame.font.Font('fonts/manaspc.ttf', 20)
        self.sqr_curr_pos = 0
        self.letter_1 = '_'
        self.letter_2 = '_'
        self.letter_3 = '_'
        self.screen = screen
        self.collect_sound = pygame.mixer.Sound('sfx/collect.ogg')
        self.collect_sound.set_volume(.6)
        self.update()

    def update(self):
        file_in = open('scores.txt', 'r')
        for line in file_in:
            self.score_text.append(line.strip().split("_"))
        self.update_score_board()

    def check(self, score):
        index = 0
        for line in self.score_text:
            s = int(score)
            if s > int(line[0]):
                self.pos = index
                break
            index += 1
        if self.pos != -1:
            self.name = True
            self.score = s

    def write(self):
        file_out = open('scores.txt', 'w')
        count = 0
        for line in self.score_text:
            file_out.write(line[0] + '_' + line[1])
            if count != 4:
                file_out.write('\n')
            count += 1
        file_out.close()

    def add_new(self):
        if self.pos == 0:
            self.score_text[4] = self.score_text[3]
            self.score_text[3] = self.score_text[2]
            self.score_text[2] = self.score_text[1]
            self.score_text[1] = self.score_text[0]
            self.score_text[0] = [str(self.score), self.letter_1+self.letter_2+self.letter_3]
        if self.pos == 1:
            self.score_text[4] = self.score_text[3]
            self.score_text[3] = self.score_text[2]
            self.score_text[2] = self.score_text[1]
            self.score_text[1] = [str(self.score), self.letter_1+self.letter_2+self.letter_3]
        if self.pos == 2:
            self.score_text[4] = self.score_text[3]
            self.score_text[3] = self.score_text[2]
            self.score_text[2] = [str(self.score), self.letter_1+self.letter_2+self.letter_3]
        if self.pos == 3:
            self.score_text[4] = self.score_text[3]
            self.score_text[3] = [str(self.score), self.letter_1+self.letter_2+self.letter_3]
        if self.pos == 4:
            self.score_text[4] = [str(self.score), self.letter_1+self.letter_2+self.letter_3]

        self.letter_1 = '_'
        self.letter_2 = '_'
        self.letter_3 = '_'
        self.update_score_board()
        self.write()

    def update_score_board(self):
        self.font_render = []
        for line in self.score_text:
            self.font_render.append(self.font.render(line[0] + " " + line[1], False, (255, 255, 255)))

    def draw(self, screen):
        yPos = 230
        screen.blit(self.font.render('HighScores', False, (255, 255, 255)), (340, 180))
        for line in self.font_render:
            screen.blit(line, (350, yPos))
            yPos += 50

    def input_name(self):
        new_render = self.font.render('New HighScore!', False, (255, 255, 255))
        self.screen.blit(new_render, (350, 150))
        name_render = self.font.render('Enter Name: ' + self.letter_1 + ' ' + self.letter_2 + ' ' + self.letter_3, False, (255, 255, 255))
        self.screen.blit(name_render, (325, 200))
        alphabet = ['A B C D E F G H I', 'J K L M N O P Q R', 'S T U V W X Y Z <', 'PRESS ENTER TO SELECT']
        alpha_render = []
        for line in alphabet:
            alpha_render.append(self.font.render(line, False, (255, 255, 255)))

        yPos = 220
        for line in alpha_render:
            self.screen.blit(line, (325, yPos))
            yPos += 20

        sqr_pos = [[322, 218], [348, 218], [374, 218], [400, 218], [426, 218], [452, 218], [478, 218], [504, 218], [530, 218],
                   [322, 238], [348, 238], [374, 238], [400, 238], [426, 238], [452, 238], [478, 238], [504, 238], [530, 238],
                   [322, 258], [348, 258], [374, 258], [400, 258], [426, 258], [452, 258], [478, 258], [504, 258], [530, 258]]
        pygame.draw.rect(self.screen, [255, 255, 255], (sqr_pos[self.sqr_curr_pos][0], sqr_pos[self.sqr_curr_pos][1], 20, 20), 1)

    def enter_letter(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if self.sqr_curr_pos in range(0, 26):
            if self.letter_1 == '_':
                self.letter_1 = alphabet[self.sqr_curr_pos]
            elif self.letter_2 == '_':
                self.letter_2 = alphabet[self.sqr_curr_pos]
            elif self.letter_3 == '_':
                self.letter_3 = alphabet[self.sqr_curr_pos]
            else:
                self.name = False
                self.add_new()
        else:
            if self.letter_3 != '_':
                self.letter_3 = '_'
            elif self.letter_2 != '_':
                self.letter_2 = '_'
            else:
                self.letter_1 = '_'
