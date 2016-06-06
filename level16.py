import Image

def solve():
  im = Image.open("mozart.gif")
  pix = im.load()
  w = im.size[0]
  h = im.size[1]
  print w, h
  new_im = Image.new(im.mode, im.size)
  new_pix = new_im.load()
  for y in range(h):
    for x in range(w-5):
      if pix[x,y] == pix[x+1, y] and pix[x,y] == pix[x+2, y] and pix[x,y] == pix[x+3, y] and pix[x,y] == pix[x+4, y]:
        start = x
    x1 = 0
    for x in range(start+5, w):
      new_pix[x1, y] = pix[x,y]
      x1 += 1
    for x in range(start):
      new_pix[x1, y] = pix[x, y]
      x1 += 1
  new_im.save("16.gif")


if __name__ == "__main__":
  solve()
