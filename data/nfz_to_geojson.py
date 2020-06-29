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

    with open('nfz_v2.csv') as nfzFile:
        nfzCSV = csv.reader(nfzFile, delimiter=',')

        for row in nfzCSV:
            id = int(row[0])
            coordianates = row[1]
            radius = 0
            if row[2] != "":
                radius = float(row[2])

            coordianates = re.sub('N', '', coordianates)
            coordianates = re.sub('E', '', coordianates)
            tempArray = re.findall("\d+\.\d+", coordianates)

            j = {}
            j['id'] = id

            if radius > 0:
                tempC = {}
                tempC['lat'] = float(tempArray[0])
                tempC['lng'] = float(tempArray[1])
                j['radius'] = radius
                j['coordinates'] = tempC
                circleArray.append(j)
            else:
                i = 0
                coordianatesArray = []
                while i < len(tempArray):
                    coordianatesArray.append(
                        makeArray(tempArray[i], tempArray[i+1]))
                    i+=2
                j['coordinates'] = coordianatesArray
                polyArray.append(j)                


        with open('../html/nfzCircle.json', 'w') as outfile:
            outfile.write("circles = ")
            # .encode('utf8')
            json.dump(circleArray, outfile, ensure_ascii=False)

        with open('../html/nfzPoly.json', 'w') as outfile:
            outfile.write("polys = ")
            # .encode('utf8')
            json.dump(polyArray, outfile, ensure_ascii=False)


if __name__ == "__main__":
    convert()
