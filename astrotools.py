class AstroTools():
    def transition(direction,R2,G2,B2,speed):#swaps background colour to another in a certain direction
        """
        The transition function transitions from one background colour to another in a certain direction.
        eg if RIGHT was the chosen direction the function would start by setting all pixels to the old background colour,
        the program then draws a gradient starting on line 'Start' going RIGHT, line by line. Because 'Start' is set to 8
        the program will only display one line of the gradient on the first frame. Each frame start is decreased by
        1, meaning the gradient will slowly go left. The length of the gradient is 'TL' which is set to ten lines.
        Start will eventually become negative meaning the gradient will start part way through on the display.
        When the end of the gradient is reached while drawing a frame, it will set the other lines to the new background
        colour. The transition ends when 'Start<-TL'
        """

        #### Checking if the values are in range ####
        if(R2>255):
            R2=255
        if(R2<0):
            R2=0
        if(G2>255):
            G2=255
        if(G2<0):
            G2=0
        if(B2>255):
            B2=255
        if(B2<0):
            B2=0
        ####static variables####
        # current background colours
        global CR
        global CG
        global CB
        TL=10#the length of the gradient in lines
        #the difference between the old and new colours is R2 - CR , G2 - CG ,B2 - CB
        #these are the increse amounts for each colour per line in the gradient
        Rin=(R2-CR)/TL
        Gin=(G2-CG)/TL
        Bin=(B2-CB)/TL
        x=0#x position for drawing pixel by pixel
        y=0#y position for drawing pixel by pixel

        #these are updated every line and are set to the desired colour for that line
        r=CR
        g=CG
        b=CB
        Line=0#the line relative to the start of the gradient
        Start=8#the line from where it starts drawing the gradient, decreases by one each time
        while(not Start<-TL):#each loop of this draws a gradient on the screen
            while(x<8):#each loop of this draws a line
                if(Start<x):#has it reached the line where it should start drawing the gradient?
                    Line=Line+1
                    if(Line<TL):#if this line is part of the gradient
                        r=CR+(Rin*Line)#set the colour of the line
                        g=CG+(Gin*Line)
                        b=CB+(Bin*Line)
                    else:#draw the new background colour for this line
                        r=R2
                        g=G2
                        b=B2
                else:#draw the old background colour for this line
                    r=CR
                    g=CG
                    b=CB
                while(y<8):#each loop of this sets the colour of one pixel in the current line
                    #### if the values generated are out of range, make them safe:
                    if(r>255):
                        r=225
                    if(r<0):
                        r=0
                    if(g>255):
                        g=225
                    if(g<0):
                        g=0
                    if(b>255):
                        b=225
                    if(b<0):
                        b=0
                    ####
                    #set the pixel to the desired colour
                    if(direction=="UP"):
                        sense.set_pixel(y,7-x,r,g,b)
                    elif(direction=="DOWN"):
                        sense.set_pixel(y,x,r,g,b)
                    elif(direction=="LEFT"):
                        sense.set_pixel(7-x,y,r,g,b)
                    else:
                        sense.set_pixel(x,y,r,g,b)
                    y=y+1
                x=x+1
                y=0
            Start=Start-1
            x=0
            if(Line>7):
                Line=Line-7
            else:
                Line=0
            time.sleep(1-speed)
        # sets the new background colour
        CR=R2
        CG=G2
        CB=B2
