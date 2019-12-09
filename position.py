
def create_position(x, y):
    return {"x": x, "y": y}

def x(pos):
    return pos["x"]

def y(pos):
    return pos["y"]

def moveUp(position):
    pos = create_position(x(position), y(position)-1)
    return pos

def moveLeft(position):
    pos = create_position(x(position)-1, y(position))
    return pos

def moveDown(position):
    pos = create_position(x(position), y(position)+1)
    return pos

def moveRight(position):
    pos = create_position(x(position)+1, y(position))
    return pos
