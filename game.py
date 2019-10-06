import pygame
import random
from card import Card

pygame.init()
pygame.font.init()

gameDisplay = pygame.display.set_mode((785,785))
pygame.display.set_caption('A Game of Memory')

clock = pygame.time.Clock()

GRID_SIZE = 6
NUM_IMGS = int((GRID_SIZE**2)/2)
CARD_SIZE = 125

card_back = pygame.image.load('imgs/card_back.png').convert_alpha()
card_back = pygame.transform.scale(card_back, (CARD_SIZE, CARD_SIZE))

img_arr = []
card_arr = []

def setup():
	for i in range(NUM_IMGS):
		file_name = 'imgs/card_'+str(i)+'.png'
		img_arr.append(pygame.image.load(file_name).convert_alpha())
		img_arr[-1] = pygame.transform.scale(img_arr[-1], (CARD_SIZE, CARD_SIZE))


	for i in range(GRID_SIZE**2):
		if i < NUM_IMGS:
			card_arr.append(Card(i, CARD_SIZE))
		else:
			card_arr.append(Card(i-NUM_IMGS, CARD_SIZE))

	random.shuffle(card_arr)

	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			curr_pos = GRID_SIZE*(i)+j
			x = ((CARD_SIZE*i)+5*(i+1))
			y = ((CARD_SIZE*j)+5*(j+1))
			card_arr[curr_pos].rect.x = x
			card_arr[curr_pos].rect.y = y

def show_grid(grid_size):
	curr = 0
	for i in range(0,grid_size):
		for j in range(0,grid_size):
			if card_arr[curr].face_up or card_arr[curr].solved:
				gameDisplay.blit(img_arr[card_arr[curr].img_id], ((CARD_SIZE*i)+5*(i+1),(CARD_SIZE*j)+5*(j+1)))
			else:
				gameDisplay.blit(card_back, ((CARD_SIZE*i)+5*(i+1),(CARD_SIZE*j)+5*(j+1)))
			curr += 1

def endGame():
	gameDisplay.fill(pygame.Color(255,255,255))
	pygame.display.flip()

	msg = pygame.image.load('imgs/end_game.png').convert_alpha()
	msg = pygame.transform.scale(msg, (725,200))
	gameDisplay.blit(msg, (10, 300))

	pygame.display.flip()

	pygame.time.wait(3000)
	pygame.quit()

def main():
	playGame = True
	num_flipped = 0
	total_solved = 0
	player_points = 0
	first_card = None
	second_card = None

	setup()

	while playGame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playGame = False
		if total_solved == GRID_SIZE**2:
			endGame()
		for card in card_arr:
			card.detectMouse()
			if card.face_up and not(card.solved):
				if (first_card == None):
					first_card = card
					num_flipped += 1
				elif (first_card != card and second_card == None):
					second_card = card
					num_flipped += 1
			if num_flipped == 2:
				if first_card.img_id == second_card.img_id:
					pygame.time.wait(500)
					player_points += 1
					first_card.solved = True
					second_card.solved = True
					total_solved+=2
				else:
					pygame.time.wait(500)
					first_card.flip()
					second_card.flip()
				first_card = None
				second_card = None
				num_flipped = 0

		show_grid(GRID_SIZE)
		pygame.display.update()
		clock.tick(30)
	pygame.quit()

main()
	
