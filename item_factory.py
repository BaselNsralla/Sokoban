def create_item(symbol, position):
    switcher = {
        "@": create_worker(position),
        "o": create_box(position),
        "#": create_wall(position),
        ".": create_store(position),
        " ": create_floor(position),
        "*": create_box(position, in_store = True),
        "+": create_worker(position, in_store = True)
    }
    obj = switcher[symbol]
    return obj

def create_wall(position, in_store = False):
    obj = {
        "type": "wall",
        "symbol": "#",
        "position": position,
        "movable": False,
        "inStore": False,
        "stepable": False
    }
    return obj

def create_box(position, in_store = False):
    obj = {
        "type": "box",
        "symbol": "o",
        "position": position,
        "movable": True,
        "inStore": in_store,
        "stepable": False
    }
    return obj

def create_store(position,  in_store = False):
    obj = {
        "type": "store",
        "symbol": ".",
        "position": position,
        "movable": False,
        "inStore": False,
        "stepable": True
    }
    return obj

def create_worker(position, in_store = False):
    obj = {
        "type": "worker",
        "symbol": "@",
        "position": position,
        "movable": True,
        "inStore": in_store,
        "stepable": False
    }
    return obj

def create_floor(position,  in_store = False):
    obj = {
       "type": "floor",
       "symbol": " ",
       "position": position, 
       "stepable": True,
       "inStore": False,
       "movable": False
    }
    return obj

