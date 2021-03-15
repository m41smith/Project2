import graphics
import random


def main():
    win = graphics.GraphWin("Drawing Shapes", 720, 480)
    cList = ['red', 'blue', 'azure', 'brown', 'cyan', 'DarkGray', 'DeepPink', 'gold', 'LimeGreen', 'orange']
    num = int(input("How many shapes do you want? "))
    tShape = 0
    while tShape < num:
        shape = input("What shape do you want? ")
        let = shape[0]
        if let.lower() == "r":
            f = win.getMouse()
            l = win.getMouse()
            r = graphics.Rectangle(f, l)
            r.setFill(cList[random.randint(0, 9)])
            r.draw(win)
            tShape = tShape + 1

        elif let.lower() == "o":
            f = win.getMouse()
            l = win.getMouse()
            o = graphics.Oval(f, l)
            o.setFill(cList[random.randint(0, 9)])
            o.draw(win)
            tShape = tShape + 1

        elif let.lower() == "c":
            radius = int(input("Now Give the Radius of the Circle."))
            center = win.getMouse()
            c = graphics.Circle(center, radius)
            c.setFill(cList[random.randint(0, 9)])
            c.draw(win)
            tShape = tShape + 1

        elif let.lower() == "l":
            f = win.getMouse()
            l = win.getMouse()
            l = graphics.Line(f, l)
            l.setWidth(2)
            l.setOutline(cList[random.randint(0, 9)])
            l.draw(win)
            tShape = tShape + 1

        elif let.lower() == "t":
            text = input("Input the text you want shown.")
            l = win.getMouse()
            t = graphics.Text(l, text)
            t.draw(win)
            tShape = tShape + 1

        elif let.lower() == "p":
            l = win.getMouse()
            p = l
            p.setOutline(cList[random.randint(0, 9)])
            p.draw(win)
            tShape = tShape + 1

        else:
            print("I don't believe I know that shape.")
    win.getMouse()
    win.close()


main()
