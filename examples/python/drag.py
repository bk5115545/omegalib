from omegaToolkit import *

ui = UiModule.createAndInitialize().getUi()

# Dictionary storing widgets
widgets = {}

# Function that creates a draggable widgets
def makeWidget(id, x, y, width, height, color):
    global widgets
    w = Widget.create(ui)
    w.setDraggable(True)
    w.setSize(Vector2(width,height))
    w.setPosition(Vector2(x, y))
    w.setFillEnabled(True)
    w.setFillColor(color)
    widgets[id] = w
    w.setActivateCommand('setActiveWidget("{0}")'.format(id))
    
# Keep track of active widget
activeWidget = None
def setActiveWidget(id):
    print('asadad')
    global activeWidget
    if(activeWidget != None): activeWidget.setLayer(WidgetLayer.Middle)
    activeWidget = widgets[id]
    activeWidget.setLayer(WidgetLayer.Front)

makeWidget('blue', 0, 0, 100, 100, Color('blue')),
makeWidget('green', 200, 250, 100, 160, Color('green')),
makeWidget('red', 150, 200, 160, 100, Color('red')),