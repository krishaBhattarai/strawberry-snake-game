import pygame
import random

from settings import *



class Food:


    def __init__(self):

        self.random_position()



    def random_position(self):


        self.x=random.randrange(

            30,
            WIDTH-60,
            BLOCK_SIZE

        )


        # 🍓 only inside game area

        self.y=random.randrange(

            120,
            HEIGHT-60,
            BLOCK_SIZE

        )




    def draw(self,screen):


        # strawberry body

        pygame.draw.circle(

            screen,

            STRAWBERRY_RED,

            (
            self.x+15,
            self.y+18
            ),

            13

        )


        # seeds

        for x in range(3):

            pygame.draw.circle(

                screen,

                WHITE,

                (
                self.x+8+x*6,
                self.y+18
                ),

                2

            )


        # leaf

        pygame.draw.polygon(

            screen,

            LEAF_GREEN,

            [

            (self.x+15,self.y+5),

            (self.x+5,self.y+10),

            (self.x+25,self.y+10)

            ]

        )