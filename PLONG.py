import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Plong")
doExit = False
clock = pygame.time.Clock()

#points
Red = 0
Blue = 1

#pattle Left
p1x = 20
p1y = 200

#pattle Right
p2x = 660
p2y = 200

#balz
bx = 350
by = 250
bVx = 5
bVy = 5


#Lop-----

while not doExit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    


    #logic----------------

    #move
    bx += bVx
    by += bVy

    #reflect

    #sides
    if bx < 0 or bx > 700:
        bVx *= -1

    #top and Bottom
    if by < 0 + 10 or by + 10 > 500:
        bVy *= -1

    #pat 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    if p1y + 100 == 500:
        p1y+=0

    #pat 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p2y-=5
    if keys[pygame.K_DOWN]:
        p2y+=5

    #Pat ball
    if bx < 50 and by < p1y + 100 and by > p1y:
        bVx *= -1


    #score

    if bx > 700:
        Red+=1
        

    if bx < 0:
        Blue+=1



    print("Blue: ")
    print(Blue)
    print()
    print("Red: ")
    print(Red)


    #render-------------------
    screen.fill((0,0,0))

    pygame.draw.line(screen,(255, 20, 255), [350, 0], [350,500], 5)
    pygame.draw.circle(screen,(255, 20, 255),(350,250),100, 5)

    #ball
    pygame.draw.circle(screen,(255, 255, 255),(bx,by),10)

    #pattle 1
    pygame.draw.rect(screen, (255, 20, 20), (p1x, p1y, 20, 100))

    #pattle 2
    pygame.draw.rect(screen, (20, 20, 255), (p2x, p2y, 20, 100))

    pygame.display.flip()
    #------------



#quit
pygame.quit()
