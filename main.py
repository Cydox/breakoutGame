import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

ball = pygame.image.load("ball.gif")
ball_rect = ball.get_rect()

ballPositionX = 50.0
ballPositionY = 200.0
ballVelocityX = 400.0
ballVelocityY = 300.0

brickRectLst = []
nbricks = 0
nextX = 0

paddle_rect = pygame.Rect(0, 0, 75, 16)
paddleX = width / 2
paddle_rect.center = (int(paddleX), int(height) - 20)
paddle_speed = 0.0


for j in range(4):
	i = 0
	nextX = 0
	while nextX < width:
			print i
			brickRectLst.append(pygame.Rect(53 * i, (19 * j) + (19 * 3), 50, 16))
			nbricks += 1
			i += 1
			nextX = 53 * i
	print j
print brickRectLst

brickColorLst = []
i = 0

for i in range(len(brickRectLst)):
	brickColorLst.append((255, 255, 255))

while True:

	dt = float(clock.tick(60)) / 1000
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: pygame.quit()
			if event.key == pygame.K_RIGHT: paddle_speed = 500.0
			if event.key == pygame.K_LEFT: paddle_speed = -500.0
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT: paddle_speed = 0.0
			if event.key == pygame.K_LEFT: paddle_speed = 0.0

	
	ballPositionX += ballVelocityX * dt
	ballPositionY += ballVelocityY * dt

	paddleX += paddle_speed *dt
	paddle_rect.center = (int(paddleX), int(height) - 20)
	
	ball_rect.center = (int(ballPositionX), int(ballPositionY))

	if ball_rect.left < 0 or ball_rect.right > width:
		ballVelocityX *= (-1)

	if ball_rect.top < 0 or ball_rect.bottom > height:
		ballVelocityY *= (-1)
	if ball_rect.bottom >= height:
		pygame.quit()
	
	for brick in brickRectLst:
		if brick.colliderect(ball_rect):
			ballVelocityY *= (-1)
			brick.center = (1000, 1000)
			nbricks -= 1
			break
	if paddle_rect.colliderect(ball_rect):
		ballVelocityY *= (-1)
	
	if nbricks <= 0:
		pygame.quit()
	screen.fill((0, 0, 0))

	for i in range(len(brickRectLst)):
		pygame.draw.rect(screen, brickColorLst[i], brickRectLst[i])

	#screen.blit(ball, (int(ballPositionX), int(ballPositionY)))
	screen.blit(ball, ball_rect)
	pygame.draw.rect(screen, (255, 255, 255),paddle_rect)
	pygame.display.flip()
