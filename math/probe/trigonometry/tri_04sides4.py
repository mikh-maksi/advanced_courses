from tkinter import *
root = Tk()
points = [100,200,300,82.5,300,200] 
points2 = [100,200,200,141.5,200,200] 
c = Canvas(root, width=400, height=400, bg='white')
c.pack()
c.create_polygon(points, fill='red')
c.create_polygon(points, outline="#476042", 
            fill='yellow', width=3)
c.create_polygon(points2, fill='red')
c.create_polygon(points2, outline="#476042", 
            fill='yellow', width=3)
c.create_arc(40, 140, 160, 260, start=0, extent=30, fill='red')
# # c.create_arc(30, 130, 170, 270, start=0, extent=30, fill='red')

# c.create_arc(250, 32, 350, 132 , start=-90, extent=-60, fill='lightgreen')


c.create_arc(270, 170, 330, 230 , start=180, extent=-90, fill='lightblue')

c.create_arc(170, 170, 230, 230 , start=180, extent=-90, fill='lightblue')

# c.create_text(130, 215, text="A(100;200)", 
#                 justify=CENTER, font="Verdana 12")

# c.create_text(300, 70, text="C(300;82)", 
#                 justify=CENTER, font="Verdana 12")

# c.create_text(300, 215, text="B(300;200)", 
#                 justify=CENTER, font="Verdana 12")

c.create_text(240, 215, text="a = 200", 
                justify=CENTER, font="Verdana 8")

c.create_text(160, 215, text="a1 = 100", 
                justify=CENTER, font="Verdana 8")

c.create_text(190, 120, text="c = 231,2", 
                justify=CENTER, font="Verdana 8")

c.create_text(125, 160, text="c1 = 115,6", 
                justify=CENTER, font="Verdana 8")

c.create_text(235, 175, text="b1 = 58", 
                justify=CENTER, font="Verdana 8")

c.create_text(325, 145, text="b = 116", 
                justify=CENTER, font="Verdana 8")

c.create_text(138, 187, text="\u03b1", 
                justify=CENTER, font="Verdana 12")

# c.create_text(150, 185, text="30°", 
#                 justify=CENTER, font="Verdana 8")

# c.create_text(285, 105, text="60°", 
#                 justify=CENTER, font="Verdana 8")


c.create_text(289, 185, text="90°", 
                justify=CENTER, font="Verdana 8")

c.create_text(189, 185, text="90°", 
                justify=CENTER, font="Verdana 8")

root.mainloop()
