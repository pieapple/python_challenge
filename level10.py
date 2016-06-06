def cal_a(a):
  a = list(a)
  result = ""
  count = 1
  for i in range(0, len(a)):
    if i < len(a) - 1 and a[i] == a[i+1]:
      count += 1
    else:
      result += str(count)
      result += a[i]
      count = 1
    if i == len(a) - 1:
      return result

def solve():
  a = "1"
  for i in range(0,30):
    a = cal_a(a)
    print "list:", a
  print len(a)

if __name__ == "__main__":
  solve()
