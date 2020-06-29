#!/usr/bin/env python3'
# -*- coding: utf-8 -*-

import osmium as o
import sys
import json
from shapely import geometry

'''
общее отношение
boundary = yes
relation=multipolygon
name=Пограничная зона Республики Беларусь
relation 5606909

1.  достать все линии и точки
2.  сгрупировать точки во много полигонов, что бы не одиним,
    а полинов 30-50 было
https://docs.osmcode.org/pyosmium/v2.15.2/ref_osm.html#osmium.osm.WayNodeList

'''


class BroderRelation(o.SimpleHandler):
    def __init__(self):
        super(BroderRelation, self).__init__()
        self.nodes = set()
        self.ways = set()

    def relation(self, r):
        # print(r.id)
        if r.id == 5606909:
            for m in r.members:
                # print (m.type)
                # print (m.ref)
                if m.type == 'w':
                    self.ways.add(m.ref)
                    # print(self.ways)


class WayFilter(o.SimpleHandler):
    def __init__(self, ways):
        super(WayFilter, self).__init__()
        self.ways = ways
        self.borders = []
        # print (len(self.ways))

    def way(self, w):
        # print(self.ways)
        if w.id in self.ways:

            nodes = []
            for n in w.nodes:
                nodes.append(n.ref)

            tempPoly = {}
            tempPoly['id'] = w.id
            tempPoly['nodes'] = nodes
            tempPoly['name'] = w.tags['name']
            print(w.tags['name'])
            tempPoly["type"] = "polygon"
            tempPoly["coordinates"] = []
            tempPoly["nodesList"] = []
        
            self.borders.append(tempPoly)
        


class NodesDetail(o.SimpleHandler):
    def __init__(self, borders):
        super(NodesDetail, self).__init__()
        self.borders = borders
    
    def node(self, n):   
        for b in self.borders:
            if n.id in b['nodes']:
                #b["coordinates"].append([n.location.lat, n.location.lon])
                b["nodesList"].append({n.id: [n.location.lat, n.location.lon]})
                if n.location.lat == 0 or n.location.lon == 0:
                    print ('bad {}'.format(n.id))
            # print(n)
            # print(len(self.nDetail))



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python filter_coastlines.py <infile> <outfile>")
        sys.exit(-1)

    # go through the ways to find all relevant nodes
    rels = BroderRelation()
    rels.apply_file(sys.argv[1])

    print('ways  in rel {}'.format(len(rels.ways)))
    print('nodes in rel {}'.format(len(rels.nodes))  )

    ways = WayFilter(rels.ways)
    ways.apply_file(sys.argv[1])

   

    nodaDetail = NodesDetail(ways.borders)
    nodaDetail.apply_file(sys.argv[1])

    for b in ways.borders:
        #b['nodes'] = []
        print('ways id {}, coordinates {}'.format(
            b['id'], len(b['coordinates'])))



    # bad = 0
    # for n in nodaDetail.nDetail:
    #     #print (n.location)

    #     coordinates.append(n.location)
    #     if n.location == '0.000000/0.000000':
    #         bad = bad + 1

   # print(nodaDetail.coordinates)
    # print ('bad = {}'.format(bad))


    with open('border.json', 'w') as borderFile:
        json.dump(nodaDetail.borders,borderFile )


'''
dd = {"id": 12,
      "name": "\u0417\u043e\u043d\u0430 12",
      "type": "polygon",
      "coordinates": [
          [53.93472222222222, 27.678888888888878],
          [53.92111111111111, 27.752500000000055],
          [53.88666666666666, 27.734166666666624],
          [53.900277777777774, 27.66055555555556],
          [53.93472222222222, 27.678888888888878]],
      "radius": 0, "created_at": "2018-05-17 04:28:13",
      "updated_at": "2018-05-17 04:28:13"
      }
  
'''
    # go through the file again and write out the data
    
    # writer = o.SimpleWriter(sys.argv[2])
    # CoastlineWriter(writer, ways.nodes).apply_file(sys.argv[1])

    # writer.close()
