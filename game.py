import pygame
import random
from card import Card

pygame.init()

gameDisplay = pygame.display.set_mode((785,785))
pygame.display.set_caption('A Game of Memory')

clock = pygame.time.Clock()

GRID_SIZE = 6
NUM_IMGS = int((GRID_SIZE**2)/2)
CARD_SIZE = 125

card_back = pygame.image.load('imgs/card_back.png').convert_alpha()
card_back = pygame.transform.scale(card_back, (CARD_SIZE, CARD_SIZE))

img_arr = []
for i in range(NUM_IMGS):
	file_name = 'imgs/card_'+str(i)+'.png'
	img_arr.append(pygame.image.load(file_name).convert_alpha())
	img_arr[-1] = pygame.transform.scale(img_arr[-1], (CARD_SIZE, CARD_SIZE))

card_arr = []
'''
for i in range(GRID_SIZE):
	for j in range(GRID_SIZE):
		curr_pos = GRID_SIZE*(i)+j
		x = ((CARD_SIZE*i)+5*(i+1))
		y = ((CARD_SIZE*j)+5*(j+1))
		if curr_pos < NUM_IMGS:
			card_arr.append(Card(curr_pos, x, y, CARD_SIZE))
		else:
			card_arr.append(Card(curr_pos-NUM_IMGS, x, y, CARD_SIZE))
'''
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
			if card_arr[curr].face_up:
				gameDisplay.blit(img_arr[card_arr[curr].img_id], ((CARD_SIZE*i)+5*(i+1),(CARD_SIZE*j)+5*(j+1)))
			else:
				gameDisplay.blit(card_back, ((CARD_SIZE*i)+5*(i+1),(CARD_SIZE*j)+5*(j+1)))
			curr += 1

def main():
	playGame = True
	while playGame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playGame = False	
		for card in card_arr:
			card.detectMouse()
		show_grid(GRID_SIZE)
		pygame.display.update()
		clock.tick(30)
	pygame.quit()

main()
	
