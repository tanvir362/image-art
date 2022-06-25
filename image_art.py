import cv2
from grid_mapper import GridMapper
from my_turtle import MyTurtle


def get_segments(ls):
    pc = ls[0]

    i = 0
    segments = []
    while i<len(ls):
        while ls[i] == pc:
            i += 1

            if i>=len(ls):
                break

        segments.append((pc, i-1))

        if i<len(ls):
            pc =  ls[i]
        else:
            break

        i+=1

    return segments

class ImageArt:
    
    def __init__(self, path, width=500, height=500):
        self.orginal = cv2.imread(path)
        self.max_width = width
        self.max_height = height

    def set_orginal(self, path):
        self.orginal = cv2.imread(path)

    def adjust_size(self):
        w, h = self.orginal.shape[1], self.orginal.shape[0]
        wh_ratio = w / h

        is_adjusted = False
        if w>self.max_width:
            w = self.max_width
            h = int(w / wh_ratio)

            is_adjusted = True

        if h>self.max_height:
            h = self.max_height
            w = int(h*wh_ratio)

            is_adjusted = True

        if is_adjusted:
            return cv2.resize(self.orginal, (w, h))

        return self.orginal

    def prepare_image(self):
        resized = self.adjust_size()
        # resized = cv2.medianBlur(resized, 7)


        gray = cv2.cvtColor(resized, cv2.COLOR_RGBA2GRAY)
        # _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)

        # cv2.imshow('img', binary)
        # cv2.waitKey(3000)
        # cv2.destroyAllWindows()

        return binary

    def draw(self):
        img = self.prepare_image()
        
        width = img.shape[1]
        height = img.shape[0]

        gm = GridMapper(width, height)

        tl = MyTurtle(self.max_width, self.max_height)

        # turtle.shape('arrow')
        tl.right(135)
        tl.penup()
        # turtle.colormode(255)
        tl.speed(10)
        
        x, y = gm.map_coordinate(0, len(img)-1)
        tl.goto(x, y)
        for i in range(len(img)-1, -1, -2):
            segments = get_segments(img[i])
            for v, indx in segments:
                if v == 0:
                    tl.pendown()
                else:
                    tl.penup()

                x, y = gm.map_coordinate(indx, i)
                tl.goto(x, y)

            tl.penup()
            x, y = gm.map_coordinate(0, i-2)
            tl.goto(x, y)

        tl.exit_on_click()


if __name__ == '__main__':

    art = ImageArt('images/tanvir.png')
    art.draw()

    # print(get_segments([1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]))