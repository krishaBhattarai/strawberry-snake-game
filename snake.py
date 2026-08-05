import pygame

from settings import *



class Snake:


    def __init__(self):

        self.reset()



    def reset(self):

        self.body = [

            [300,360],
            [270,360],
            [240,360]

        ]

        self.direction="RIGHT"




    def move(self):

        head=self.body[0].copy()



        if self.direction=="RIGHT":

            head[0]+=BLOCK_SIZE


        elif self.direction=="LEFT":

            head[0]-=BLOCK_SIZE


        elif self.direction=="UP":

            head[1]-=BLOCK_SIZE


        elif self.direction=="DOWN":

            head[1]+=BLOCK_SIZE



        self.body.insert(0,head)

        self.body.pop()




    def grow(self):

        self.body.append(
            self.body[-1].copy()
        )




    def collision(self):

        head=self.body[0]


        # wall collision

        if (

            head[0]<30 or
            head[0]>=WIDTH-30 or
            head[1]<100 or
            head[1]>=HEIGHT-30

        ):

            return True



        # self collision

        if head in self.body[1:]:

            return True



        return False





    def draw(self,screen):


        for i,part in enumerate(self.body):


            color = (
                SNAKE_HEAD
                if i==0
                else SNAKE_BLUE
            )


            pygame.draw.rect(

                screen,

                color,

                (
                part[0],
                part[1],
                BLOCK_SIZE,
                BLOCK_SIZE
                ),

                border_radius=12

            )



        # eyes

        head=self.body[0]


        pygame.draw.circle(

            screen,

            WHITE,

            (
            head[0]+10,
            head[1]+10
            ),

            5

        )


        pygame.draw.circle(

            screen,

            WHITE,

            (
            head[0]+22,
            head[1]+10
            ),

            5

        )