
from helpers import *
from item_factory import *
from item_manager import *
from position import *

def fill_ver(diff, field):
    for i in range(diff+1):
        field.append([])
    return field

def fill_hor(diff, field):
    for i in range(diff+1):
        field.append(None)
    return field

def add_to_field(obj, field = None):
    if field == None:
        field = []
    y = coordinate("y", obj)
    x = coordinate("x", obj)
    if not exists(y, field):
        diff  = 1 if y == 0 else y - len(field)
        field = fill_ver(diff, field)
  
    if not exists(x, field[y]):
        diff  = 1 if x == 0 else x - len(field[y])
        field[y] = fill_hor(diff, field[y])

    field[y][x] = obj
    return field


def draw(field):
    for row in field:
        for _obj in row:
            if _obj == None:
                print(" ", end = "")
            else:
                print(draw_object(_obj) ,end = "")
        print()

def item_at(position, field):
    _y = y(position)
    _x = x(position)
    if not exists(_y, field):
        return None
    elif not exists(_x, field[_y]):
        return None
    return field[_y][_x]

def player(field):
    for row in field:
        for obj in row:
            if obj["type"] == "worker":
                return obj

##Fix this
def coordinate(coord, item):
    pos = position_of(item)
    if coord == "x":
        return x(pos)
    elif coord == "y":
        return y(pos)
    else:
        raise RuntimeError('invalid coordinate axis')

def move_in_field(obj, new_position, game_field):
    _x = coordinate("x", obj)
    _y = coordinate("y", obj)
    new_x = x(new_position)
    new_y = y(new_position)
    new_obj = item_at(create_position(new_x,new_y), game_field)
    if is_movable(obj):
        game_field[_y][_x] = create_item(".", create_position(_x,_y)) if was_in_store(obj) else create_item(" ", create_position(_x,_y))
        if type_of(new_obj) == "store":
            if type_of(obj) == "worker" or type_of(obj) == "box":
                set_in_store(obj)
        else:
            remove_from_store(obj)
        obj = move_if_possible(obj, new_position)
        game_field[new_y][new_x] = obj
    return game_field

def number_of(item_type, game_field):
    num = 0
    for row in game_field:
        for item in row:
            if type_of(item) == item_type:
                num += 1
    return num

def number_of_in_store(item_type, game_field):
    num = 0
    for row in game_field:
        for item in row:
            if type_of(item) == item_type and is_in_store(item):
                num += 1
    return num

def symbolfield_to_objectfield(symbol_field):
    object_field = []
    for y in range(len(symbol_field)):
        for x in range(len(symbol_field[y])):
            object_field = add_to_field(create_item(symbol_field[y][x], create_position(x, y)), object_field)
    return object_field