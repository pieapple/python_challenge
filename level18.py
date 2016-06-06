import Image
import difflib

def solve():
  left = []
  right = []
  lines = open("delta.txt").read()
  for line in lines.splitlines():
    left.append(line[:53])
    right.append(line[56:])

  diff = difflib.Differ()
  png = ['', '', '']
  for row in list(diff.compare(left,right)):
    bytes = [chr(int(byte,16)) for byte in row[2:].split()]
    if row[0]=='-': png[0]+=''.join(bytes)
    elif row[0]=='+': png[1]+=''.join(bytes)
    elif row[0]==' ': png[2]+=''.join(bytes)

  for i in range(3):
    open('18_%d.png' %i,'wb').write(png[i])

if __name__ == "__main__":
  solve()
