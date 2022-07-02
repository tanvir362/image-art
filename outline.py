import cv2
import numpy as np

mp = []

class Cell:
    def __init__(self, val):
        self.is_black = val==0
        self.is_changed = False
        self.is_visited = False

def check_on_border(mp, i, j):
    for adj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
        r, c = adj
        h = len(mp)
        w = len(mp[0])

        if r<0 or r>=h or c<0 or c>=w:
            return True

        if (not mp[r][c].is_black) and (not mp[r][c].is_changed):
            return True
    
    return False

def is_valid_coord(mp, R, C):
    h = len(mp)
    w = len(mp[0])

    if R<0 or R>=h or C<0 or C>=w:
        return False

    return True


def flood_fill(mp, R, C):
    q = []

    mp[R][C].is_visited = True
    q.append((R, C))

    while q:
        r,c = q.pop(0)

        for adj in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
            a, b = adj

            if is_valid_coord(mp, a, b) and (not check_on_border(mp, a, b)):
                if not mp[a][b].is_visited:
                    mp[a][b].is_black = False
                    mp[a][b].is_changed = True

                    q.append((a, b))

                mp[a][b].is_visited = True



def outline(img):
    mp = []

    for rw in img:
        mp.append([*map(Cell, rw)])

    for i, rw in enumerate(mp):
        for j, cell in enumerate(rw):
            if cell.is_black and cell.is_visited==False:
                flood_fill(mp, i, j)

    return np.asarray(
        [[*map(lambda cell: 0 if cell.is_black else 255, rw)] for rw in mp], dtype=np.uint8
    )


        






if __name__ == '__main__':
    from image_art import ImageArt

    file_path = 'images/rabbit_keep.png'
    art = ImageArt(file_path, 400, 400)

    binary = art.prepare_image()
    outlined = outline(binary)


    cv2.imshow('Binary', binary)
    cv2.imshow('Outlined', outlined)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()