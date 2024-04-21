from Rhythm import Rhythm
import random

class Transition(object):
    def __init__(self):
        self.size = 16   
        self.transitionNums = []
        self.Tom1Array = []
        self.Tom2Array = []
        self.snareArray = []
        self.floorArray = []
    
    def randTransition(self,index):
        for i in range(self.size):
           if(i < index):
                self.transitionNums.append(-1)
           else:
                self.transitionNums.append(random.randint(1,4))
        return

    def setTransition(self,index,Rhythm):            
        for i in range(self.size):
            if(i < index):
                self.Tom1Array.append(Rhythm.HHArray[i])
                self.Tom2Array.append("")
                self.snareArray.append(Rhythm.snareArray[i])
                self.floorArray.append(Rhythm.bassArray[i])
            else:
                 if(self.transitionNums[i] == 1):            
                        self.Tom1Array.append("TOM1")
                        self.Tom2Array.append("")
                        self.floorArray.append("")
                        self.snareArray.append("")
           
                 elif(self.transitionNums[i] == 2):
                       self.Tom1Array.append("")
                       self.Tom2Array.append("")
                       self.floorArray.append("")
                       self.snareArray.append("SNARE")

                 elif(self.transitionNums[i] == 3):
                      self.Tom1Array.append("")
                      self.Tom2Array.append("TOM2")
                      self.floorArray.append("")
                      self.snareArray.append("")

                 elif(self.transitionNums[i] == 4):
                      self.Tom1Array.append("")
                      self.Tom2Array.append("")
                      self.floorArray.append("FLOOR")
                      self.snareArray.append("")

                 else:
                      self.Tom1Array.append("")
                      self.Tom2Array.append("")
                      self.floorArray.append("") 
                      self.snareArray.append("")

        return

    def temp(self,buffer,arr):
        for i in range(self.size):
            buffer += arr[i]
            buffer += "\t"        
        buffer += "\n"
        return buffer

    def TransitionInfo(self):
        info = ""
        tom1 = self.temp(info,self.Tom1Array)
        tom2 = self.temp(info,self.Tom2Array)
        snare = self.temp(info,self.snareArray)
        floor = self.temp(info,self.floorArray)
        info = tom1+tom2+snare+floor
        return info

