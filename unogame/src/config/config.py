# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def vw(width):
    return (width * SCREEN_WIDTH) / 100


def vh(height):
    return (height * SCREEN_HEIGHT) / 100


def vp(width, height):
    return vw(width), vh(height)

