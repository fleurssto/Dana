from PIL import Image

def main():
  ascii_char = ' .:-=+*#%@'
  
  with Image.open("lacaz.jpg") as image:
      image = image.resize((500, 500))
  
      for y in range(image.height):
          line = ""
          for x in range(image.width):
              rgb = image.getpixel((x, y))
              grey = sum(rgb) // len(rgb)
              index = grey * 9 // 255
              line += ascii_char[index] + "  "
          print(line)


if __name__ == '__main__':
    main()
