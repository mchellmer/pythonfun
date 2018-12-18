import json
import re

class Mapper:
    def __init__(self,mapPath,word,regString):
        self.name = "Mapper Bot"
        self.mapperMapPath = mapPath
        self.mapperWord = word
        self.mapperRegString = regString
        self.mapperData = self.getExistingMap(mapPath)

    def map(self):
        if re.search(self.mapperRegString,self.mapperWord):
            if self.checkForMap() == 0:
                print (self.mapperWord + " is not mapped.")
                mapResult = input("What should this map to? ")
                self.mapperData[self.mapperWord] = mapResult
                self.saveNewMap(self.mapperMapPath)
                return mapResult
            else:
                return self.checkForMap()
        else:
            return self.mapperWord

    def checkForMap(self):            
        if self.mapperWord in self.mapperData:
            return self.mapperData[self.mapperWord]
        else:
            return 0

    def getExistingMap(self, path):
        with open(path) as f:
            return json.load(f)

    def saveNewMap(self, path):
        with open(path, 'w') as f:
            json.dump(self.mapperData,f)


