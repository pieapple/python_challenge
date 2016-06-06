import xmlrpclib

def solve():
  proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
  print proxy.phone('Bert')
  print proxy.phone('Leopold')

if __name__ == "__main__":
  solve()
