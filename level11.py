from PIL import Image

def solve():
  src = Image.open("cave.jpg")
  w,h = src.size[0], src.size[1]
  new = Image.new(src.mode,(w, h))
  src_pix = src.load()
  new_pix = new.load()
  
  print 3//2, 3/2

  for x in range(w):
    for y in range(h):
      p = src_pix[x,y]
      i = x/2
      j = y/2
      if x%2==0 and y%2==0:
        new_pix[i,j] = p
      elif x%2==0 and y%2==1:
        new_pix[i,j+h//2] = p
      elif x%2==1 and y%2==0:
        new_pix[i+w//2,j] = p
      elif x%2==1 and y%2==1:
        new_pix[i+w//2,j+h//2] = p
  new.save('new.jpg')
  new.show()

if __name__ == "__main__":
  solve()
