import xmlrpclib
import urllib,re,bz2,urllib2

def solve1():
  url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
  seed="12345"
  info=''
  while 1:
    req = urllib.urlopen(url+seed)
    text=req.read()
    seed=''.join(re.findall(r"busynothing is (\d+)",text))
    cookies=req.info().getheaders('Set-Cookie')[0]
    ch = ''.join(re.findall(r"info=(.*?);", cookies))
    info += ch
    print ch
    if seed == "":
      break
  print info
  print urllib.unquote_plus(info)
  print bz2.decompress(urllib.unquote_plus(info))

def solve2():
  proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
  print proxy.phone('Leopold')

def solve3():
  info='the flowers are on their way'
  url='http://www.pythonchallenge.com/pc/stuff/violin.php'
  req = urllib2.Request(url, headers={'Cookie': 'info=' + urllib.quote_plus(info)})
  r = urllib2.urlopen(req)
  print r.read()

if __name__ == "__main__":
  solve3()
