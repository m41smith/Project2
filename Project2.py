import graphics
import random


def main():
    win = graphics.GraphWin("Drawing Shapes", 720, 480)
    cList = ['red', 'blue', 'azure', 'brown', 'cyan', 'DarkGray', 'DeepPink', 'gold', 'LimeGreen', 'orange']
    num = int(input("How many shapes do you want?"))
    tShape = 0
    while tShape < num:
        shape = input("What shape do you want")
        let = shape[0]
        if let.lower() == "r":
            fx = int(input("Give the first X coordinate of the Rectangle."))
            lx = int(input("Now give the second X coordinate of the Rectangle."))
            fy = int(input("Give the first Y coordinate of the Rectangle."))
            ly = int(input("Now give the second Y coordinate of the Rectangle."))
            r = graphics.Rectangle(graphics.Point(fx, fy), graphics.Point(lx, ly))
            r.setFill(cList[random.randint(0,9)])
            r.draw(win)
            tShape = tShape + 1

        elif let.lower() == "o":
            fx = int(input("Give the first X coordinate of the Oval."))
            lx = int(input("Now give the second X coordinate of the Oval."))
            fy = int(input("Give the first Y coordinate of the Oval."))
            ly = int(input("Now give the second Y coordinate of the Oval."))
            o = graphics.Oval(graphics.Point(fx, fy), graphics.Point(lx, ly))
            o.setFill(cList[random.randint(0,9)])
            o.draw(win)
            tShape = tShape + 1

        elif let.lower() == "c":
            cx = int(input("Give the center X coordinate for the Circle."))
            cy = int(input("Give the center Y coordinate for the Circle."))
            radius = int(input("Now Give the Radius of the Circle."))
            c = graphics.Circle(graphics.Point(cx, cy), radius)
            c.setFill(cList[random.randint(0,9)])
            c.draw(win)
            tShape = tShape + 1

        elif let.lower() == "l":
            fx = int(input("Give the first X coordinate of the Line."))
            lx = int(input("Now give the second X coordinate of the Line."))
            fy = int(input("Give the first Y coordinate of the Line."))
            ly = int(input("Now give the second Y coordinate of the Line."))
            l = graphics.Line(graphics.Point(fx, fy), graphics.Point(lx, ly))
            l.setWidth(2)
            l.setOutline(cList[random.randint(0,9)])
            l.draw(win)
            tShape = tShape + 1

        elif let.lower() == "t":
            x = int(input("Give the X coordinate of the text."))
            y = int(input("Now give the Y coordinate of the text."))
            text = input("Input the text you want shown.")
            t = graphics.Text(graphics.Point(x, y), text)
            t.draw(win)
            tShape = tShape + 1

        elif let.lower() == "p":
            x = int(input("Give the X coordinate of the Point."))
            y = int(input("Now give the Y coordinate of the Point."))
            p = graphics.Point(x, y)
            p.setOutline(cList[random.randint(0,9)])
            p.draw(win)
            tShape = tShape + 1

        else:
            print("I don't believe I know that shape.")
    win.getMouse()
    win.close()


main()
