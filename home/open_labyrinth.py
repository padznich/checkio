

def checkio(lab):
    s = (1, 1)
    f = (10, 10)

def maze_controller(mr):

    if mr.found():
        return None
    else:
        mr.turn_left()
        if mr.go():
            depth = 0
            maze_controller(mr)
        else:
            mr.turn_right()

            if mr.go():
                depth = 1
                maze_controller(mr)
            else:
                mr.turn_right()

                if mr.go():
                    depth = 2
                    maze_controller(mr)
                else:
                    mr.turn_right()
                    if mr.go():
                        depth = 3
                        maze_controller(mr)
                    else:
                        return None

if __name__ == '__main__':
    checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
