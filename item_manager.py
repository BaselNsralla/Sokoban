
def is_movable(obj):
    return obj["movable"]

def is_stepable(obj):
    return obj["stepable"]

def was_in_store(obj):
    return obj["inStore"]

def is_in_store(obj):
    return obj["inStore"]

def type_of(obj):
    return obj["type"]

def position_of(obj):
    return obj["position"]

def move_if_possible(obj, new_position):
    if is_movable(obj):
        obj["position"] = new_position
    return obj

def draw_object(obj):
    symbol = obj["symbol"]
    if symbol == "@" and was_in_store(obj):
        return "+"
    elif symbol == "o" and was_in_store(obj):
        return "*"
    return symbol

def set_in_store(obj):
    obj["inStore"] = True
    return obj

def remove_from_store(obj):
    obj["inStore"] = False
    return obj
