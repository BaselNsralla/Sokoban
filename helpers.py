
def exists(index, array):
    if index < len(array):
        return True
    else:
        return False

def slice_unwanted(arr):
    if '\n' in arr:
        idx = arr.index('\n')
        arr.pop()