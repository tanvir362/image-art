class GridMapper:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.width_adj = width//2
        self.height_adj = height//2

    def map_coordinate(self, x, y):

        return (x-self.width_adj, -(y-self.height_adj))