import Image

def fillMatrix(src_pix, dst_pix):
  src_pos = 0
  for n in reversed(range(1, 51)):
    dst_x = dst_y = 50 - n
    for i in range(n*2):
      dst_pix[dst_x+i, dst_y] = src_pix[src_pos, 0]
      src_pos += 1
    for j in range(n*2-1):
      dst_pix[dst_x+n*2-1, dst_y+j+1] = src_pix[src_pos, 0]
      src_pos += 1
    for i in range(n*2-1):
      dst_pix[dst_x+n*2-2-i, dst_y+n*2-1] = src_pix[src_pos, 0]
      src_pos += 1
    for j in range(n*2-2):
      dst_pix[dst_x, dst_y+n*2-2-j] = src_pix[src_pos, 0]
      src_pos += 1
  print src_pos, dst_x, dst_y

def solve():
  im = Image.open("wire.png")
  im_pix = im.load()
  new = Image.new(im.mode, (100,100))
  new_pix = new.load()
  fillMatrix(im_pix, new_pix)
  new.save("14.jpg")

if __name__ == "__main__":
  solve()
