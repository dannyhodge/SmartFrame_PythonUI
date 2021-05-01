import pygame
from pygame.locals import *
import sys
from urllib.request import urlopen
import io
import requests
import time

pygame.init()
WIDTH = 800
HEIGHT = 600
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

def getImages():
    r = requests.get('http://192.168.0.12:3002/images')
    print("Status: " + str(r.status_code))
    return r.json()

images = getImages()
imageCount = len(images)
print("There are " + str(imageCount) + " images")
counter = 0

while True:
   if counter == imageCount:
       counter = 0
       print(counter)

   currentImage = images[counter]['signedUrl'][0]
   image_str = urlopen(currentImage).read()
   image_file = io.BytesIO(image_str)
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   screen.fill((0, 0, 1))
   img = pygame.image.load(image_file)
   x, y = img.get_size()
   rx = WIDTH / x
   ry = HEIGHT / y
   ratio = rx if rx < ry else ry
   img = pygame.transform.scale(img, (int(x*rx), int(y*rx)))
   img_rect = img.get_rect()
   img_rect.centerx = WIDTH/2
   img_rect.centery = HEIGHT/2

   windowSurface.blit(img, img_rect)
   pygame.display.flip()

   counter += 1

   for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_x:  # PRESS X TO QUIT
                pygame.quit()
                sys.exit()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   time.sleep(1)
