import graphics
import random

#def test():
    #win = graphics.GraphWin("Graphics Window",500,500)
    #c = graphics.Circle(graphics.Point(50, 50), 10)
    #c.draw(win)
    #win.getMouse()  # Pause to view result
    #win.close()  # Close window when done

#test()

def main():
    win = graphics.GraphWin("Drawing Shapes",500,500)
    num = int(input("How many shapes do you want?"))

    shape = input("What shape do you want")
    let = shape[0]
    if let.lower() == "r":
        pass
    elif let.lower() == "o":
        pass
    elif let.lower() == "c":
        pass
    elif let.lower() == "l":
        pass
    elif let.lower() == "t":
        pass
    elif let.lower() == "p":
        pass
    else:
        print("I don't believe I know that shape.")


main()
