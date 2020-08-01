def bottleform(n):
  if n == 0:
    return "no more bottles"
  elif n == 1:
    return str(n) + " bottle"
  else:
    return str(n) + " bottles"


def printLyrics(n=99):
  if(n==0):
    return bottleform(n) + "water on the wall, " + bottleform(n) + " of water\nGo to the store" + bottleform(99) + " of water on the wall"
  else:
    return bottleform(n) + "water on the wall " + bottleform(n) + " of water\nTake on down pass it around, " + printLyrics(n-1)


print(printLyrics(99))