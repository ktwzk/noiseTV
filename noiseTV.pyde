defaults = '''0 #BPM, float. Can be 0 (actually, means 3600)
10 #sides' of square length, int (px)
rainbow #color palette: 'b/w' for black and white, 'rainbow' for all colors, 'mouse' for mouse-control of palette or '%x %y' (int,int) for color in HSB: color will be: Rand(0,x)/255, Rand(0,y)/255, Rand(255)/255
no # cursor type: cross, arrow or no'''

try:
    config_file = open('config', 'r')
except Exception:
    config_file = open('config', 'w')
    config_file.write(defaults)
    config_file.close()
    config_file = open('config', 'r')
config = []
for lin in config_file:
    config.append(lin)
global config


def setup():
    size(displayWidth, displayHeight)
    cursor_type = config[3].split()[0]
    if cursor_type.lower() == 'no':
        noCursor()
    elif cursor_type.lower() == 'cross':
        cursor(CROSS)
    else:
        cursor(ARROW)
    if (frame is not None):
        frame.setResizable(True)
    global config
    bpm = float(config[0].split()[0])
    if bpm != 0:
        frameRate(bpm / 60.0)
    else:
        pass
    colorMode(HSB, width, height, 255)
    noStroke()
    background(0)


def draw():
    global config
    side = int(config[1].split()[0])
    palette = config[2].split()[0]
    if palette.lower() == 'b/w':
        color_of_x = 0
        color_of_y = 0
    elif palette.lower() == 'rainbow':
        color_of_x = width
        color_of_y = height
    elif palette.lower() == 'mouse':
        color_of_x = mouseX
        color_of_y = mouseY
    else:
        tmp = config[2].split()
        color_of_x = int(tmp[0]) * (width / 255.0)
        color_of_y = int(tmp[1]) * (height / 255.0)
    for i in xrange(0, width, side):
        for j in xrange(0, height, side):
            fill(random(color_of_x), random(color_of_y), random(255))
            rect(i, j, side, side)
