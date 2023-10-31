from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

mainFont = "Ubuntu"
mainSize = 14
mainTitleSize = 32

def drawCheckboxItems(names, c, height):
    counter = 1
    form = c.acroForm
    for name in names:
        # draw the string starting from the top
        # and for each element move down 40 pixels
        c.drawString(40, height - 50 - counter * 40, name)

        # draw the checkbox at almost the same y direction
        # with the x direction based on the width of the string
        form.checkbox(name=('cb' + str(counter)), 
                      tooltip=('Field cb' + str(counter)),
                      x=(stringWidth(name, mainFont, mainSize) + 50), 
                      y=(height - 55 - counter * 40), 
                      buttonStyle='check',
                      borderColor=black, forceBorder=True)
        counter = counter + 1

def initCheckbox(title, c):
    # draw the title with a larger font then set
    # the font size to be constant for the whole document
    c.setFont(mainFont, mainTitleSize)
    c.drawString(50, height - 50, title)
    c.setFont(mainFont, mainSize)

def consoleInput():
    print("Title of checklist:")
    title = input()
    print("Number of elements:")
    num_elems = int(input())
    items = []
    for i in range(0, num_elems):
        print("Checklist item number " + str(i + 1) + ":")
        items.append(input())
    return title, items

def testInput():
    title = "How to fly a plane"
    items = ["Turn on the plane", "Press the gas pedal", "fly"]
    return title, items

if __name__ == '__main__':
    pdfmetrics.registerFont(TTFont(mainFont, mainFont + ".ttf"))

    # select consoleInput() or testInput()
    title, items = testInput()

    # capitalize all of the items input
    for i in range(0, len(items)):
        items[i] = items[i].capitalize()
    
    # set the filename as the title in lowercase
    # with the spaces replaced by underscores
    # and set to lowercase
    c = canvas.Canvas(title.replace(" ", "_").lower() + " checklist.pdf", pagesize=A4)
    width, height = A4
    
    # initialize the fonts and title
    initCheckbox(title, c)
    # draw the checkbox items
    drawCheckboxItems(items, c, height)
    c.save()
