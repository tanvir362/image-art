import sys
from image_art import ImageArt


if __name__ == "__main__":
    file_path = 'images/flower_keep.jpg'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    art = ImageArt(file_path)

    art.draw()








