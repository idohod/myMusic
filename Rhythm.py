import random

class Rhythm(object):
    def __init__(self):
        self.size = 16   
        self.rhythmNums = []
        self.HHArray = []
        self.bassArray = []
        self.snareArray = []
    
    def randArray(self):

        for i in range(self.size):
            if(i == 0 or i == 8):
                  self.rhythmNums.append(1)
            elif(i == 4 or i == 12):
                  self.rhythmNums.append(2)
            else:
                  self.rhythmNusms.append(random.randint(0,2))
        return 

    def checkRandom(self):
        stackNums = [4,8,12]
        for i in range(self.size - 2):
           if(self.rhythmNums[i] == self.rhythmNums[i + 1] and self.rhythmNums[i + 1] == self.rhythmNums[i + 2]):
              if(i + 2 in stackNums):
                  self.rhythmNums[i] = 0
              else:
                  self.rhythmNums[i + 2] = 0
           
           if(self.rhythmNums[self.size - 2] == self.rhythmNums[self.size - 1] and self.rhythmNums[self.size - 2] == self.rhythmNums[0]):
              self.rhythmNums[self.size - 1] = 0
        return

    def putHH(self):
         for i in range(self.size):
            if(i % 2 == 0):
                 self.HHArray.append("HH")
            else:
                 self.HHArray.append(" ")
         return

    def setRhythm(self):
       
       for i in self.rhythmNums:      
            if(i == 1):
               self.bassArray.append("BASS")
               self.snareArray.append(" ")
            elif(i == 2):
                self.snareArray.append("SNARE") 
                self.bassArray.append(" ")
            else:
                self.bassArray.append(" ")
                self.snareArray.append(" ")
       return

    def randAndSetRhythm(self):
        self.randArray()
        self.checkRandom()
        self.putHH()
        self.setRhythm()
        return

    def temp(self,buffer,arr):
        for i in range(self.size):
            buffer += arr[i]
            buffer += "\t"        
        buffer += "\n"
        return buffer

    def rhythmInfo(self):
        info = ""
        hh = self.temp(info,self.HHArray)
        snare = self.temp(info,self.snareArray)
        bass = self.temp(info,self.bassArray)
        info = hh+"\n"+snare+bass
        return info 