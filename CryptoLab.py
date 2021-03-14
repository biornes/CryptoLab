import random
import os
import json

class Lab:
  sBoxValues = []
  def __init__(self):
    # pass
    pathToSbox = os.path.join(os.getcwd(), 'sbox.txt')
    if os.path.exists(pathToSbox):
      with open (pathToSbox, 'r') as file:
        self.sBoxValues = json.load(file)
        print (self.sBoxValues)
        coordFunctions = [0, 0, 0, 0, 0, 0]
        for i in range(len(self.sBoxValues)):
          print (bin(self.sBox(i)), self.hammingWeight(self.sBox(i)))
          coordFunctions[0] = (coordFunctions[0] << 1) | self.sBox(i) & 2**5
          coordFunctions[1] = (coordFunctions[1] << 1) | self.sBox(i) & 2**4
          coordFunctions[2] = (coordFunctions[2] << 1) | self.sBox(i) & 2**3
          coordFunctions[3] = (coordFunctions[3] << 1) | self.sBox(i) & 2**2
          coordFunctions[4] = (coordFunctions[4] << 1) | self.sBox(i) & 2**1
          coordFunctions[5] = (coordFunctions[5] << 1) | self.sBox(i) & 2**0
        for i in coordFunctions:
          print (bin(i))
    else:
      self.generateSbox()
  def generateSbox(self):
    self.sBoxValues = list(range(0, 64))
    print (random.shuffle(self.sBoxValues))
    print (self.sBoxValues)

    with open(os.path.join(os.getcwd(), 'sbox.txt'), 'w') as file:
      json.dump(delf.sBoxValues, file)

  def sBox(self, num):
    return self.sBoxValues[num]
  def hammingWeight(self, num):
    return bin(num).count('1')


def main():
 lab = Lab()


if __name__ == '__main__':
  main()