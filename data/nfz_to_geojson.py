import csv
import sys
import json
import re



def makeArray(lat, lon):
    temp = []
    temp.append(float(lat))
    temp.append(float(lon))

    return temp


def convert():

    circleArray = []
    polyArray = []

    with open('nfz.csv') as nfzFile:
        nfzCSV = csv.reader(nfzFile, delimiter=',')

        for row in nfzCSV:
            id = int(row[0])
            coordianates = row[1]
            radius = 0
            if row[2] != "":
                radius = float(row[2])

            coordianates = re.sub('N', '', coordianates)
            coordianates = re.sub('E', '', coordianates)
            #print(str(id) + ' ' + str(coordianates) + ' ' + str(radius))


            coordianatesArray = []
            tempArray = re.findall("\d+\.\d+", coordianates)
            
            j = {}
            j['id'] = id
            
            tempC = []
            if radius > 0: 
                tempC = {}
                tempC['lat'] = float(tempArray[0])
                tempC['lng'] = float(tempArray[1])
                #coordianatesArray.append(tempC)
                j['radius'] = radius
                j['coordinates'] = tempC

                circleArray.append(j)
            else:
                i = 0
                while i < len(tempArray):                
                    coordianatesArray.append(
                        makeArray(tempArray[i], tempArray[i+1]))
                    i+=2
                j['coordinates'] = coordianatesArray
                polyArray.append(j)                


        with open('nfzCircle.json', 'w') as outfile:
            outfile.write("circles = ")
            # .encode('utf8')
            json.dump(circleArray, outfile, ensure_ascii=False)

        with open('nfzPoly.json', 'w') as outfile:
            outfile.write("polys = ")
            # .encode('utf8')
            json.dump(polyArray, outfile, ensure_ascii=False)


if __name__ == "__main__":
    convert()
