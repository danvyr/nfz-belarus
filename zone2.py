#!/usr/bin/python3

import pickle
import os
import json

circles = {

    'circle1': {
        'coordinates': {'lat': 52.618055, 'lng': 25.080000},
        'radius': 2.5
    },

    'circle2': {
        'coordinates': {'lat': 54.681666, 'lng': 28.501388},
        'radius': 2.5
    },

    'circle3': {
        'coordinates': {'lat': 55.516666, 'lng': 29.948055},
        'radius': 5
    },

    'circle4': {
        'coordinates': {'lat': 52.403333, 'lng': 30.748333},
        'radius': 2.5
    },

    'circle5': {
        'coordinates': {'lat': 52.453333, 'lng': 31.535000},
        'radius': 2.5
    },

    'circle6': {
        'coordinates': {'lat': 53.311388, 'lng': 28.798333},
        'radius': 2.5
    },

    'circle7': {
        'coordinates': {'lat': 53.171388, 'lng': 27.628333
                        },
        'radius': 3
    },

    'circle8': {
        'coordinates': {'lat': 53.709166, 'lng': 27.343888
                        },
        'radius': 1.5
    },

    'circle9': {
        'coordinates': {'lat': 53.864444, 'lng': 27.077777
                        },
        'radius': 2.5
    },

    'circle10': {
        'coordinates': {'lat': 54.046666, 'lng': 27.136388
                        },
        'radius': 1.5
    },

    'circle11': {
        'coordinates': {'lat': 53.619722, 'lng': 27.116944
                        },
        'radius': 1.5
    },

    'circle12': {
        'coordinates': {'lat': 54.017222, 'lng': 27.604166
                        },
        'radius': 2.5
    },

    'circle13': {
        'coordinates': {'lat': 54.192500, 'lng': 27.761944
                        },
        'radius': 1.5
    },

    'circle14': {
        'coordinates': {'lat': 53.728055, 'lng': 23.863888
                        },
        'radius': 1.5
    },

    'circle15': {
        'coordinates': {'lat': 52.070000, 'lng': 29.176944
                        },
        'radius': 1.2
    },

    'circle16': {
        'coordinates': {'lat': 52.475555, 'lng': 30.779722
                        },
        'radius': 1
    },

    'circle16n': {
        'coordinates': {'lat': 52.566379, 'lng': 24.919980
                        },
        'radius': 0.2
    },

    'circle17': {
        'coordinates': {'lat': 52.556687, 'lng': 24.926871
                        },
        'radius': 0.4
    },

    'circle18': {
        'coordinates': {'lat': 52.545555, 'lng': 23.810000
                        },
        'radius': 0.9
    },

    'circle19': {
        'coordinates': {'lat': 53.977575, 'lng': 26.907472
                        },
        'radius': 1.5
    },

    'circle20': {
        'coordinates': {'lat': 53.307500, 'lng': 24.375000
                        },
        'radius': 3
    },

    'circle21': {
        'coordinates': {'lat': 52.933611, 'lng': 24.324166
                        },
        'radius': 1
    },

    'circle22': {
        'coordinates': {'lat': 55.499166, 'lng': 28.898611
                        },
        'radius': 1.8
    },

    'circle23': {
        'coordinates': {'lat': 55.114166, 'lng': 26.770555
                        },
        'radius': 1.5
    },

    'circle24': {
        'coordinates': {'lat': 54.573611, 'lng': 30.477777
                        },
        'radius': 3
    },

    'circle25': {
        'coordinates': {'lat': 54.148888, 'lng': 25.892222
                        },
        'radius': 1.5
    },

    'circle26': {
        'coordinates': {'lat': 54.711361, 'lng': 26.069107
                        },
        'radius': 2
    },

    'circle27': {
        'coordinates': {'lat': 53.126040, 'lng': 26.035700
                        },
        'radius': 0.1
    },

    'circle27n': {
        'coordinates': {'lat': 53.893888, 'lng': 27.582222
                        },
        'radius': 0.4
    },

    'circle28': {
        'coordinates': {'lat': 53.904444, 'lng': 27.530277
                        },
        'radius': 0.2
    },

    'circle29': {
        'coordinates': {'lat': 53.844444, 'lng': 27.628611
                        },
        'radius': 0.3
    },

    'circle30': {
        'coordinates': {'lat': 54.078055, 'lng': 27.678888
                        },
        'radius': 3.5
    },

    'circle31': {
        'coordinates': {'lat': 54.884444, 'lng': 26.825833
                        },
        'radius': 1
    },

    'circle32': {
        'coordinates': {'lat': 52.117500, 'lng': 28.189444
                        },
        'radius': 2
    },

    'circle33': {
        'coordinates': {'lat': 55.732777, 'lng': 27.116944
                        },
        'radius': 3
    },

    'circle34': {
        'coordinates': {'lat': 53.946666, 'lng': 27.501944
                        },
        'radius': 0.8
    },

    'circle35': {
        'coordinates': {'lat': 55.410555, 'lng': 28.566111
                        },
        'radius': 1
    },

    'circle36': {
        'coordinates': {'lat': 55.534166, 'lng': 26.819722
                        },
        'radius': 1
    },

    'circle37': {
        'coordinates': {'lat': 55.491111, 'lng': 28.782777
                        },
        'radius': 1
    },

    'circle38': {
        'coordinates': {'lat': 54.502500, 'lng': 26.296944
                        },
        'radius': 1
    },

    'circle39': {
        'coordinates': {'lat': 55.120833, 'lng': 26.882777
                        },
        'radius': 1
    },

    'circle40': {
        'coordinates': {'lat': 54.867500, 'lng': 26.315833
                        },
        'radius': 1
    },

    'circle41': {
        'coordinates': {'lat': 54.418333, 'lng': 25.879444
                        },
        'radius': 1
    },

    'circle42': {
        'coordinates': {'lat': 54.317222, 'lng': 26.836666
                        },
        'radius': 2
    },

    'circle43': {
        'coordinates': {'lat': 53.893055, 'lng': 25.267500
                        },
        'radius': 1
    },

    'circle44': {
        'coordinates': {'lat': 54.141944, 'lng': 25.320000
                        },
        'radius': 1
    },

    'circle45': {
        'coordinates': {'lat': 53.015555, 'lng': 24.075277
                        },
        'radius': 1
    },

    'circle46': {
        'coordinates': {'lat': 51.802500, 'lng': 24.076666
                        },
        'radius': 1
    },

    'circle47': {
        'coordinates': {'lat': 52.209722, 'lng': 31.417777
                        },
        'radius': 1
    },

    'circle48': {
        'coordinates': {'lat': 52.213888, 'lng': 31.100555
                        },
        'radius': 1
    },

    'circle49': {
        'coordinates': {'lat': 53.673055, 'lng': 27.121388
                        },
        'radius': 1
    },

    'circle50': {

        'coordinates': {'lat': 52.073333, 'lng': 29.112222
                        },
        'radius': 1
    },

    'circle51': {
        'coordinates': {'lat': 52.424444, 'lng': 30.923611
                        },
        'radius': 1
    },

    'circle52': {
        'coordinates': {'lat': 53.837500, 'lng': 27.752777
                        },
        'radius': 1
    },

    'circle53': {
        'coordinates': {'lat': 52.328333, 'lng': 30.371666
                        },
        'radius': 3
    },
    'circle54': {
        'coordinates':
        {'lat': 55.510277, 'lng': 28.564722},
        'radius': 4},

    'circle55': {
        'coordinates':
        {'lat': 51.888611, 'lng': 29.324444},
        'radius': 2.6
    },

    'circle56': {
        'coordinates': {'lat': 53.820833, 'lng': 30.336111
                        },
        'radius': 2
    },

    'circle57': {
        'coordinates': {'lat': 52.319444, 'lng': 30.888333
                        },
        'radius': 1
    },

    'circle58': {
        'coordinates': {'lat': 52.183888, 'lng': 29.885000
                        },
        'radius': 1
    },

    'circle59': {
        'coordinates': {'lat': 51.923611, 'lng': 29.264166
                        },
        'radius': 1
    },

    'circle60': {
        'coordinates': {'lat': 52.077222, 'lng': 27.622777
                        },
        'radius': 1
    },

    'circle61': {
        'coordinates': {'lat': 52.286944, 'lng': 24.487777
                        },
        'radius': 1
    },

    'circle62': {
        'coordinates': {'lat': 52.426388, 'lng': 30.857777
                        },
        'radius': 2
    },

    'circle63': {
        'coordinates': {'lat': 55.461111, 'lng': 28.721666
                        },
        'radius': 0.8
    },

    'circle64': {
        'coordinates': {'lat': 53.908333, 'lng': 25.320555
                        },
        'radius': 0.6
    },

    'circle65': {
        'coordinates': {'lat': 53.640555, 'lng': 27.915555
                        },
        'radius': 0.3
    },

    'circle66': {
        'coordinates': {'lat': 53.492222, 'lng': 28.159444
                        },
        'radius': 0.2
    },

    'circle67': {
        'coordinates': {'lat': 55.153055, 'lng': 30.153888
                        },
        'radius': 0.5
    },

    'circle68': {
        'coordinates': {'lat': 54.835555, 'lng': 29.150277
                        },
        'radius': 0.3
    },

    'circle69': {
        'coordinates': {'lat': 55.040833, 'lng': 27.788333
                        },
        'radius': 0.5
    },

    'circle70': {
        'coordinates': {'lat': 53.864444, 'lng': 30.238888
                        },
        'radius': 0.3
    },

    'circle71': {
        'coordinates': {'lat': 53.143333, 'lng': 29.189722
                        },
        'radius': 0.3
    },

    'circle72': {
        'coordinates': {'lat': 53.745833, 'lng': 31.675555
                        },
        'radius': 0.4
    },

    'circle73': {
        'coordinates': {'lat': 53.379444, 'lng': 32.061388
                        },
        'radius': 0.2
    },

    'circle74': {
        'coordinates': {'lat': 53.875555, 'lng': 25.314722
                        },
        'radius': 0.2
    },

    'circle75': {
        'coordinates': {'lat': 53.743333, 'lng': 27.348611
                        },
        'radius': 0.4
    },

    'circle76': {
        'coordinates': {'lat': 54.204444, 'lng': 28.501944
                        },
        'radius': 0.2
    },

    'circle77': {
        'coordinates': {'lat': 54.306944, 'lng': 26.861388
                        },
        'radius': 0.15
    },

    'circle78': {
        'coordinates': {'lat': 52.991944, 'lng': 27.599444
                        },
        'radius': 0.3
    },

    'circle79': {
        'coordinates': {'lat': 52.220833, 'lng': 24.307222
                        },
        'radius': 0.1
    },

    'circle80': {
        'coordinates': {'lat': 52.221388, 'lng': 24.328333
                        },
        'radius': 0.2
    },

    'circle81': {
        'coordinates': {'lat': 52.129444, 'lng': 26.126388
                        },
        'radius': 0.2
    },

    'circle82': {
        'coordinates': {'lat': 53.708333, 'lng': 23.836111
                        },
        'radius': 0.3
    },

    'circle83': {
        'coordinates': {'lat': 53.118055, 'lng': 24.406111
                        },
        'radius': 0.4
    },

    'circle84': {
        'coordinates': {'lat': 53.098888, 'lng': 25.341111
                        },
        'radius': 0.3
    },

    'circle85': {
        'coordinates': {'lat': 54.503055, 'lng': 26.222500
                        },
        'radius': 0.3
    },

    'circle86': {
        'coordinates': {'lat': 52.212500, 'lng': 29.386388
                        },
        'radius': 0.5
    },

    'circle87': {
        'coordinates': {'lat': 51.908055, 'lng': 29.999166
                        },
        'radius': 0.3
    },

    'circle88': {
        'coordinates': {'lat': 52.304444, 'lng': 30.235000
                        },
        'radius': 3
    },

    'circle89': {
        'coordinates': {'lat': 53.010833, 'lng': 24.043333
                        },
        'radius': 1
    },

    'circle90': {
        'coordinates': {'lat': 52.288333, 'lng': 30.261111
                        },
        'radius': 0.8
    },

    'circle91': {
        'coordinates': {'lat': 52.413611, 'lng': 29.857777
                        },
        'radius': 0.5
    },

    'circle92': {
        'coordinates': {'lat': 52.514444, 'lng': 29.541944
                        },
        'radius': 0.5
    },

    'circle93': {
        'coordinates': {'lat': 52.617500, 'lng': 29.151388
                        },
        'radius': 0.4
    },

    'circle94': {
        'coordinates': {'lat': 52.356944, 'lng': 30.311666
                        },
        'radius': 0.7
    },

    'circle95': {
        'coordinates': {'lat': 54.761111, 'lng': 26.095833
                        },
        'radius': 6
    },

    'circle96': {
        'coordinates': {'lat': 52.451944, 'lng': 25.195555
                        },
        'radius': 1.5
    },

    'circle97': {
        'coordinates': {'lat': 53.142500, 'lng': 26.011111
                        },
        'radius': 0.6
    },

    'circle98': {
        'coordinates': {'lat': 52.567500, 'lng': 24.477222
                        },
        'radius': 0.6
    },

    'circle99': {
        'coordinates': {'lat': 55.169166, 'lng': 30.135833
                        },
        'radius': 0.6
    },

    'circle100': {
        'coordinates': {'lat': 54.694722, 'lng': 30.492500
                        },
        'radius': 0.5
    },

    'circle101': {
        'coordinates': {'lat': 55.432777, 'lng': 28.946666
                        },
        'radius': 0.5
    },

    'circle102': {
        'coordinates': {'lat': 54.679722, 'lng': 29.135000
                        },
        'radius': 1.5
    },

    'circle103': {
        'coordinates': {'lat': 55.250555, 'lng': 30.160555
                        },
        'radius': 0.6
    },

    'circle104': {
        'coordinates': {'lat': 52.448888, 'lng': 30.816388
                        },
        'radius': 1
    },

    'circle105': {
        'coordinates': {'lat': 53.901111, 'lng': 25.290277
                        },
        'radius': 0.3
    },

    'circle106': {
        'coordinates': {'lat': 53.608055, 'lng': 25.773611
                        },
        'radius': 1
    },

    'circle107': {
        'coordinates': {'lat': 53.877222, 'lng': 27.652500
                        },
        'radius': 0.6
    },

    'circle108': {
        'coordinates': {'lat': 53.872222, 'lng': 27.399444
                        },
        'radius': 1.5
    },

    'circle109': {
        'coordinates': {'lat': 53.882500, 'lng': 27.578055
                        },
        'radius': 0.44
    },

    'circle110': {
        'coordinates': {'lat': 53.611111, 'lng': 27.947222
                        },
        'radius': 0.65
    },

    'circle111': {
        'coordinates': {'lat': 54.093055, 'lng': 28.350833
                        },
        'radius': 0.41
    },

    'circle112': {
        'coordinates': {'lat': 54.227777, 'lng': 28.504722
                        },
        'radius': 0.31
    },

    'circle113': {
        'coordinates': {'lat': 53.886944, 'lng': 30.296111
                        },
        'radius': 0.35
    },

    'circle114': {
        'coordinates': {'lat': 53.960555, 'lng': 30.347222
                        },
        'radius': 0.2
    },

    'circle115': {
        'coordinates': {'lat': 53.166388, 'lng': 29.224722
                        },
        'radius': 0.3
    },

    'circle116': {
        'coordinates': {'lat': 54.166111, 'lng': 29.779722
                        },
        'radius': 0.1
    },

    'circle117': {
        'coordinates': {'lat': 53.357222, 'lng': 28.679444
                        },
        'radius': 0.1
    },

    'circle118': {
        'coordinates': {'lat': 53.426666, 'lng': 29.858055
                        },
        'radius': 0.6
    },

    'circle119': {
        'coordinates': {'lat': 52.206388, 'lng': 23.960000
                        },
        'radius': 1
    },

    'circle120': {
        'coordinates': {'lat': 53.182222, 'lng': 25.982777
                        },
        'radius': 1
    },

    'circle121': {
        'coordinates': {'lat': 52.253611, 'lng': 27.401388
                        },
        'radius': 1
    },

    'circle122': {
        'coordinates': {'lat': 53.162500, 'lng': 25.993055
                        },
        'radius': 1
    },

    'circle124': {
        'coordinates': {'lat': 52.742222, 'lng': 25.349722
                        },
        'radius': 1
    },

    'circle125': {
        'coordinates': {'lat': 52.189722, 'lng': 26.082222
                        },
        'radius': 1
    },

    'circle126': {
        'coordinates': {'lat': 54.563888, 'lng': 30.175833
                        },
        'radius': 0.2
    },

    'circle127': {
        'coordinates': {'lat': 55.046111, 'lng': 30.300833
                        },
        'radius': 0.32
    },

    'circle128': {
        'coordinates': {'lat': 55.422222, 'lng': 28.503888
                        },
        'radius': 0.3
    },

    'circle129': {
        'coordinates': {'lat': 52.376666, 'lng': 31.332222
                        },
        'radius': 1
    },

    'circle130': {
        'coordinates': {'lat': 52.457500, 'lng': 30.897777
                        },
        'radius': 1
    },

    'circle131': {
        'coordinates': {'lat': 52.913611, 'lng': 30.379166
                        },
        'radius': 1
    },

    'circle132': {
        'coordinates': {'lat': 52.016666, 'lng': 29.166666
                        },
        'radius': 0.6
    },

    'circle133': {
        'coordinates': {'lat': 52.406111, 'lng': 30.946666
                        },
        'radius': 0.4
    },

    'circle134': {
        'coordinates': {'lat': 53.825833, 'lng': 23.864166
                        },
        'radius': 1
    },

    'circle135': {
        'coordinates': {'lat': 53.629722, 'lng': 23.867222
                        },
        'radius': 1
    },

    'circle136': {
        'coordinates': {'lat': 53.228611, 'lng': 24.454444
                        },
        'radius': 1
    },

    'circle137': {
        'coordinates': {'lat': 53.552500, 'lng': 26.387222
                        },
        'radius': 1
    },

    'circle138': {
        'coordinates': {'lat': 53.116944, 'lng': 28.350833
                        },
        'radius': 0.35
    },

    'circle139': {
        'coordinates': {'lat': 54.400000, 'lng': 27.907500
                        },
        'radius': 0.27
    },

    'circle140': {
        'coordinates': {'lat': 53.995555, 'lng': 27.529722
                        },
        'radius': 0.18
    },

    'circle141': {

        'coordinates': {'lat': 54.302777, 'lng': 26.750555
                        },
        'radius': 0.25
    },

    'circle142': {
        'coordinates': {'lat': 53.018611, 'lng': 27.375833
                        },
        'radius': 0.15
    },

    'circle143': {
        'coordinates': {'lat': 52.728888, 'lng': 27.644166
                        },
        'radius': 0.15
    },

    'circle144': {
        'coordinates': {'lat': 54.145555, 'lng': 28.377777
                        },
        'radius': 0.20
    },

    'circle145': {
        'coordinates': {'lat': 53.686388, 'lng': 27.699444
                        },
        'radius': 0.17
    },

    'circle146': {
        'coordinates': {'lat': 53.611111, 'lng': 27.947222
                        },
        'radius': 0.15
    },

    'circle147': {
        'coordinates': {'lat': 53.172222, 'lng': 29.062777
                        },
        'radius': 0.35
    },

    'circle148': {
        'coordinates': {'lat': 53.856666, 'lng': 30.509444
                        },
        'radius': 0.25
    },

    'circle149': {
        'coordinates': {'lat': 54.019722, 'lng': 30.330555
                        },
        'radius': 0.15
    },

    'circle150': {
        'coordinates': {'lat': 53.691388, 'lng': 31.601111
                        },
        'radius': 0.13
    },

    'circle151': {
        'coordinates': {'lat': 53.321111, 'lng': 28.669722
                        },
        'radius': 0.11
    },

    'circle152': {
        'coordinates': {'lat': 53.396388, 'lng': 28.528611
                        },
        'radius': 0.11
    },

    'circle153': {
        'coordinates': {'lat': 53.888888, 'lng': 27.633333
                        },
        'radius': 0.5
    },

    'circle154': {
        'coordinates': {'lat': 51.919722, 'lng': 29.314722
                        },
        'radius': 0.7
    },

    'circle155': {
        'coordinates': {'lat': 52.719722, 'lng': 25.341111
                        },
        'radius': 0.7
    },

    'circle156': {
        'coordinates': {'lat': 52.853055, 'lng': 25.363055
                        },
        'radius': 0.7
    },


    'circle157': {
        'coordinates': {'lat': 52.057777, 'lng': 29.239444
                        },
        'radius': 0.7
    },
    'circle158': {
        'coordinates': {'lat': 52.625555, 'lng': 29.715277
                        },
        'radius': 0.7
    },

    'circle159': {
        'coordinates': {'lat': 52.363611, 'lng': 30.429444
                        },
        'radius': 0.7
    },

    'circle160': {
        'coordinates': {'lat': 52.464166, 'lng': 30.973333
                        },
        'radius': 0.7
    },

    'circle161': {
        'coordinates': {'lat': 52.458333, 'lng': 30.073333
                        },
        'radius': 0.7
    },

    'circle162': {
        'coordinates': {'lat': 55.172222, 'lng': 30.196388
                        },
        'radius': 0.7
    },

    'circle163': {
        'coordinates': {'lat': 55.507777, 'lng': 28.778888
                        },
        'radius': 0.7
    },

    'circle164': {
        'coordinates': {'lat': 54.531944, 'lng': 30.448333
                        },
        'radius': 0.7
    },

    'circle165': {
        'coordinates': {'lat': 55.164444, 'lng': 27.671111
                        },
        'radius': 0.7
    },

    'circle166': {
        'coordinates': {'lat': 55.248333, 'lng': 30.318055
                        },
        'radius': 0.7
    },

    'circle167': {
        'coordinates': {'lat': 53.146944, 'lng': 24.480555
                        },
        'radius': 0.9
    },

    'circle168': {
        'coordinates': {'lat': 53.868611, 'lng': 27.575833
                        },
        'radius': 0.4
    },

    'circle169': {
        'coordinates': {'lat': 53.883333, 'lng': 27.493611
                        },
        'radius': 0.4
    },

    'circle170': {
        'coordinates': {'lat': 53.681388, 'lng': 23.848333
                        },
        'radius': 0.4
    },

    'circle171': {
        'coordinates': {'lat': 53.894166, 'lng': 30.320833
                        },
        'radius': 0.4
    },

    'circle172': {
        'coordinates': {'lat': 53.145000, 'lng': 29.162777
                        },
        'radius': 0.4
    },

    'circle173': {
        'coordinates': {'lat': 53.835833, 'lng': 30.394444
                        },
        'radius': 0.7
    },

    'circle174': {
        'coordinates': {'lat': 54.180000, 'lng': 30.284722
                        },
        'radius': 0.7
    },

    'circle175': {
        'coordinates': {'lat': 54.040833, 'lng': 27.778611
                        },
        'radius': 0.7
    },

    'circle176': {
        'coordinates': {'lat': 53.113055, 'lng': 25.965277
                        },
        'radius': 0.3
    },

    'circle177': {
        'coordinates': {'lat': 52.084444, 'lng': 23.689444
                        },
        'radius': 0.15
    },

    'circle178': {
        'coordinates': {'lat': 55.205000, 'lng': 30.213611
                        },
        'radius': 0.2
    },

    'circle179': {
        'coordinates': {'lat': 55.238888, 'lng': 30.270555
                        },
        'radius': 0.3
    },

    'circle180': {
        'coordinates': {'lat': 55.212222, 'lng': 30.223888
                        },
        'radius': 0.3
    },

    'circle181': {
        'coordinates': {'lat': 52.613055, 'lng': 31.151666
                        },
        'radius': 0.5
    },

    'circle182': {
        'coordinates': {'lat': 52.437777, 'lng': 31.007777
                        },
        'radius': 0.2
    },

    'circle183': {
        'coordinates': {'lat': 53.678888, 'lng': 23.832222
                        },
        'radius': 0.1
    },

    'circle184': {
        'coordinates': {'lat': 53.595833, 'lng': 25.464166
                        },
        'radius': 0.7
    },

    'circle185': {
        'coordinates': {'lat': 53.811111, 'lng': 25.764722
                        },
        'radius': 0.5
    },

    'circle186': {
        'coordinates': {'lat': 54.253055, 'lng': 28.715555
                        },
        'radius': 0.3
    },

    'circle187': {
        'coordinates': {'lat': 54.111388, 'lng': 28.369444
                        },
        'radius': 0.3
    },

    'circle188': {
        'coordinates': {'lat': 53.241111, 'lng': 27.713611
                        },
        'radius': 0.3
    },

    'circle189': {
        'coordinates': {'lat': 53.688611, 'lng': 27.155277
                        },
        'radius': 0.2
    },

    'circle190': {
        'coordinates': {'lat': 54.257500, 'lng': 30.987777
                        },
        'radius': 1.5
    },

    'circle191': {
        'coordinates': {'lat': 54.291111, 'lng': 30.980555
                        },
        'radius': 0.1
    },

    'circle192': {
        'coordinates': {'lat': 53.180277, 'lng': 30.285277
                        },
        'radius': 0.5
    },

    'circle193': {
        'coordinates': {'lat': 54.395000, 'lng': 31.162777
                        },
        'radius': 0.3
    },

    'circle194': {
        'coordinates': {'lat': 53.854444, 'lng': 30.410277
                        },
        'radius': 0.4
    },

    'circle195': {
        'coordinates': {'lat': 53.128888, 'lng': 29.238888
                        },
        'radius': 0.11
    },

    'circle196': {
        'coordinates': {'lat': 53.941944, 'lng': 30.357500
                        },
        'radius': 0.5
    },

    'circle197': {
        'coordinates': {'lat': 53.914166, 'lng': 27.558055
                        },
        'radius': 0.05
    },

    'circle198': {
        'coordinates': {'lat': 53.913055, 'lng': 27.558611
                        },
        'radius': 0.07
    },

    'circle199': {
        'coordinates': {'lat': 53.912500, 'lng': 27.567777
                        },
        'radius': 0.07
    },

    'circle200': {
        'coordinates': {'lat': 53.910833, 'lng': 27.570000
                        },
        'radius': 0.07
    },

    'circle201': {
        'coordinates': {'lat': 53.909444, 'lng': 27.571944
                        },
        'radius': 0.07
    },

    'circle202': {
        'coordinates': {'lat': 53.906944, 'lng': 27.576666
                        },
        'radius': 0.05
    },

    'circle203': {
        'coordinates': {'lat': 53.910000, 'lng': 27.586111
                        },
        'radius': 0.05
    },

    'circle204': {
        'coordinates': {'lat': 53.910555, 'lng': 27.591666
                        },
        'radius': 0.07
    },

    'circle205': {
        'coordinates': {'lat': 53.896944, 'lng': 27.586388
                        },
        'radius': 0.08
    },

    'circle206': {
        'coordinates': {'lat': 53.897056, 'lng': 27.589139
                        },
        'radius': 0.05
    },

    'circle207': {
        'coordinates': {'lat': 53.904444, 'lng': 27.621111
                        },
        'radius': 0.05
    },

    'circle208': {
        'coordinates': {'lat': 53.918888, 'lng': 27.587500
                        },
        'radius': 0.05
    },

    'circle209': {
        'coordinates': {'lat': 53.927222, 'lng': 27.598888
                        },
        'radius': 0.05
    },

    'circle210': {
        'coordinates': {'lat': 53.936111, 'lng': 27.617777
                        },
        'radius': 0.05
    },

    'circle211': {
        'coordinates': {'lat': 53.944722, 'lng': 27.586388
                        },
        'radius': 0.05
    },

    'circle212': {
        'coordinates': {'lat': 53.943611, 'lng': 27.581666
                        },
        'radius': 0.05
    },

    'circle213': {
        'coordinates': {'lat': 53.940277, 'lng': 27.584722
                        },
        'radius': 0.05
    },

    'circle214': {
        'coordinates': {'lat': 53.926111, 'lng': 27.543333
                        },
        'radius': 0.1
    },

    'circle215': {
        'coordinates': {'lat': 53.923333, 'lng': 27.629444
                        },
        'radius': 0.12
    },

    'circle216': {
        'coordinates': {'lat': 53.905277, 'lng': 27.548888
                        },
        'radius': 0.05
    },

    'circle217': {
        'coordinates': {'lat': 53.915833, 'lng': 27.559444
                        },
        'radius': 0.05
    },

    'circle218': {
        'coordinates': {'lat': 53.950833, 'lng': 27.439166
                        },
        'radius': 0.05
    },

    'circle219': {
        'coordinates': {'lat': 53.941666, 'lng': 27.484166
                        },
        'radius': 0.05
    },
}


poly200 = [
    {'lat': 53.911944, 'lng': 27.565833
     },
    {'lat': 53.910277, 'lng': 27.563888
     },
    {'lat': 53.908888, 'lng': 27.566944
     },
    {'lat': 53.910277, 'lng': 27.569166
     },
    {'lat': 53.911944, 'lng': 27.565833
     }
]


poly201 = [
    {'lat': 53.900833, 'lng': 27.581388
     },
    {'lat': 53.900000, 'lng': 27.579722
     },
    {'lat': 53.898611, 'lng': 27.581111
     },
    {'lat': 53.899444, 'lng': 27.583055
     },
    {'lat': 53.900000, 'lng': 27.582500
     },
    {'lat': 53.900833, 'lng': 27.581388
     }
]


poly202 = [
    {'lat': 53.871852, 'lng': 27.638873
     },
    {'lat': 53.869233, 'lng': 27.646555
     },
    {'lat': 53.862558, 'lng': 27.641148
     },
    {'lat': 53.866401, 'lng': 27.632222
     },
    {'lat': 53.871852, 'lng': 27.638873
     }
]

poly203 = [
    {'lat': 53.918418, 'lng': 27.566065
     },
    {'lat': 53.916771, 'lng': 27.565706
     },
    {'lat': 53.916263, 'lng': 27.571631
     },
    {'lat': 53.918205, 'lng': 27.573710
     },
    {'lat': 53.918502, 'lng': 27.572266
     },
    {'lat': 53.918041, 'lng': 27.571893
     },
    {'lat': 53.918424, 'lng': 27.566065
     }
]

poly204 = [
    {'lat': 53.195357, 'lng': 26.166169
     },
    {'lat': 53.112303, 'lng': 26.306731
     },
    {'lat': 52.935351, 'lng': 26.022570
     },
    {'lat': 53.018683, 'lng': 25.882565
     },
    {'lat': 53.195357, 'lng': 26.166169
     }
]

poly205 = [
    {'lat': 53.842888, 'lng': 27.358092
     },
    {'lat': 53.880392, 'lng': 27.549481
     },
    {'lat': 53.793724, 'lng': 27.600041
     },
    {'lat': 53.812615, 'lng': 27.704208
     },
    {'lat': 53.775671, 'lng': 27.730599
     },
    {'lat': 53.739557, 'lng': 27.631433
     },
    {'lat': 53.662613, 'lng': 27.675882
     },
    {'lat': 53.623165, 'lng': 27.486994
     },
    {'lat': 53.842888, 'lng': 27.358092
     }
]

poly207 = [
    {'lat': 53.979796, 'lng': 25.268622
     },
    {'lat': 54.018966, 'lng': 25.457788
     },
    {'lat': 53.793411, 'lng': 25.594746
     },
    {'lat': 53.750629, 'lng': 25.409191
     },
    {'lat': 53.979796, 'lng': 25.268622
     },
]

poly206 = [
    {'lat': 53.103184, 'lng': 28.998146
     },
    {'lat': 53.135136, 'lng': 29.401204
     },
    {'lat': 53.018746, 'lng': 29.427877
     },
    {'lat': 52.986239, 'lng': 29.025930
     },
    {'lat': 53.103184, 'lng': 28.998146
     }
]

poly207 = [
    {'lat': 52.336464, 'lng': 26.601215
     },
    {'lat': 52.251470, 'lng': 26.969000
     },
    {'lat': 52.140911, 'lng': 26.899005
     },
    {'lat': 52.225351, 'lng': 26.534553
     },
    {'lat': 52.336464, 'lng': 26.601215
     },
]

poly210 = [
    {'lat': 53.947678, 'lng': 27.663603
     },
    {'lat': 53.965381, 'lng': 27.645245
     },
    {'lat': 53.963592, 'lng': 27.643931
     },
    {'lat': 53.961282, 'lng': 27.638980
     },
    {'lat': 53.958905, 'lng': 27.631823
     },
    {'lat': 53.947678, 'lng': 27.663603
     },
]

poly209 = [
    {'lat': 53.928635, 'lng': 27.608856
     },
    {'lat': 53.930707, 'lng': 27.596589
     },
    {'lat': 53.935877, 'lng': 27.600817
     },
    {'lat': 53.933162, 'lng': 27.612005
     },
    {'lat': 53.928635, 'lng': 27.608856
     },
]

poly208 = [
    {'lat': 55.736824, 'lng': 28.519946
     },
    {'lat': 55.672108, 'lng': 28.929398
     },
    {'lat': 55.557384, 'lng': 28.872182
     },
    {'lat': 55.622655, 'lng': 28.463007
     },
    {'lat': 55.736824, 'lng': 28.519946
     },
]

poly213 = [
    {'lat': 52.800883, 'lng': 24.827846
     },
    {'lat': 52.793939, 'lng': 24.860623
     },
    {'lat': 52.774773, 'lng': 24.914235
     },
    {'lat': 52.753106, 'lng': 24.927014
     },
    {'lat': 52.730606, 'lng': 24.931182
     },
    {'lat': 52.678938, 'lng': 24.910073
     },
    {'lat': 52.681715, 'lng': 24.860073
     },
    {'lat': 52.732270, 'lng': 24.794236
     },
    {'lat': 52.796716, 'lng': 24.797567
     },
    {'lat': 52.800883, 'lng': 24.827846
     },
]

poly212 = [
    {'lat': 53.669227, 'lng': 25.500078
     },
    {'lat': 53.621740, 'lng': 25.501698
     },
    {'lat': 53.623409, 'lng': 25.637810
     },
    {'lat': 53.680909, 'lng': 25.635862
     },
    {'lat': 53.695908, 'lng': 25.544472
     },
    {'lat': 53.669227, 'lng': 25.500078
     },
]

poly211 = [
    {'lat': 52.716449, 'lng': 25.473131
     },
    {'lat': 52.774785, 'lng': 25.598130
     },
    {'lat': 52.799789, 'lng': 25.798131
     },
    {'lat': 52.716457, 'lng': 25.939802
     },
    {'lat': 52.591452, 'lng': 25.739807
     },
    {'lat': 52.599783, 'lng': 25.606473
     },
    {'lat': 52.683115, 'lng': 25.481466
     },
    {'lat': 52.716449, 'lng': 25.473131
     },
]


poly216 = [
    {'lat': 52.040833, 'lng': 23.727777
     },
    {'lat': 52.026954, 'lng': 23.724419
     },
    {'lat': 51.994624, 'lng': 23.736431
     },
    {'lat': 51.950857, 'lng': 23.702686
     },
    {'lat': 51.922500, 'lng': 23.718611
     },
    {'lat': 51.930000, 'lng': 23.810000
     },
    {'lat': 51.970833, 'lng': 23.803333
     },
    {'lat': 51.975000, 'lng': 23.826388
     },
    {'lat': 52.007222, 'lng': 23.808333
     },
    {'lat': 52.014444, 'lng': 23.808055
     },
    {'lat': 52.026666, 'lng': 23.794444
     },
    {'lat': 52.024444, 'lng': 23.785277
     },
    {'lat': 52.032500, 'lng': 23.777777
     },
    {'lat': 52.042222, 'lng': 23.749444
     },
    {'lat': 52.040833, 'lng': 23.727777
     },
]


poly214 = [
    {'lat': 52.060341, 'lng': 23.738888
     },
    {'lat': 52.059145, 'lng': 23.738820
     },
    {'lat': 52.056804, 'lng': 23.741512
     },
    {'lat': 52.055705, 'lng': 23.741199
     },
    {'lat': 52.054604, 'lng': 23.748541
     },
    {'lat': 52.056944, 'lng': 23.748888
     },
    {'lat': 52.057222, 'lng': 23.746388
     },
    {'lat': 52.060000, 'lng': 23.746944
     },
    {'lat': 52.060277, 'lng': 23.738888
     },
]


poly215 = [
    {'lat': 52.061883, 'lng': 23.707148
     },
    {'lat': 52.060064, 'lng': 23.708740
     },
    {'lat': 52.058830, 'lng': 23.714235
     },
    {'lat': 52.055646, 'lng': 23.721354
     },
    {'lat': 52.059043, 'lng': 23.727739
     },
    {'lat': 52.060246, 'lng': 23.725652
     },
    {'lat': 52.059454, 'lng': 23.724155
     },
    {'lat': 52.063616, 'lng': 23.717822
     },
    {'lat': 52.062171, 'lng': 23.715117
     },
    {'lat': 52.064022, 'lng': 23.712124
     },
    {'lat': 52.061883, 'lng': 23.707148
     },
]


poly220 = [
    {'lat': 53.516666, 'lng': 28.172222
     },
    {'lat': 53.504166, 'lng': 28.172222
     },
    {'lat': 53.504166, 'lng': 28.177777
     },
    {'lat': 53.494444, 'lng': 28.177777
     },
    {'lat': 53.494444, 'lng': 28.208333
     },
    {'lat': 53.516666, 'lng': 28.208333
     },
    {'lat': 53.516666, 'lng': 28.172222
     },
]

poly219 = [
    {'lat': 55.366666, 'lng': 29.998055
     },
    {'lat': 55.366666, 'lng': 29.914722
     },
    {'lat': 55.300000, 'lng': 29.914722
     },
    {'lat': 55.300000, 'lng': 30.014722
     },
    {'lat': 55.366666, 'lng': 29.998055
     },
]


poly218 = [
    {'lat': 55.225773, 'lng': 30.251130
     },
    {'lat': 55.228368, 'lng': 30.249192
     },
    {'lat': 55.226924, 'lng': 30.239877
     },
    {'lat': 55.225351, 'lng': 30.240579
     },
    {'lat': 55.225754, 'lng': 30.243276
     },
    {'lat': 55.224553, 'lng': 30.243928
     },
    {'lat': 55.225773, 'lng': 30.251130
     },
]


poly217 = [
    {'lat': 55.187384, 'lng': 30.222933
     },
    {'lat': 55.188725, 'lng': 30.221210
     },
    {'lat': 55.190711, 'lng': 30.222672
     },
    {'lat': 55.191764, 'lng': 30.229179
     },
    {'lat': 55.191794, 'lng': 30.231667
     },
    {'lat': 55.189122, 'lng': 30.231841
     },
    {'lat': 55.188914, 'lng': 30.232485
     },
    {'lat': 55.186212, 'lng': 30.231458
     },
    {'lat': 55.186234, 'lng': 30.230334
     },
    {'lat': 55.187751, 'lng': 30.228795
     },
    {'lat': 55.188097, 'lng': 30.223975
     },
    {'lat': 55.187384, 'lng': 30.222933
     },
]


poly221 = [
    {'lat': 52.176111, 'lng': 26.126111
     },
    {'lat': 52.142500, 'lng': 26.104722
     },
    {'lat': 52.136111, 'lng': 26.132222
     },
    {'lat': 52.169722, 'lng': 26.153333
     },
    {'lat': 52.176111, 'lng': 26.126111
     },
]

poly222 = [
    {'lat': 55.150555, 'lng': 26.798055
     },
    {'lat': 55.123333, 'lng': 26.839722
     },
    {'lat': 55.135277, 'lng': 26.863333
     },
    {'lat': 55.162500, 'lng': 26.821666
     },
    {'lat': 55.150555, 'lng': 26.798055
     },
]

poly223 = [
    {'lat': 53.934722, 'lng': 27.678888
     },
    {'lat': 53.900277, 'lng': 27.660555
     },
    {'lat': 53.886666, 'lng': 27.734166
     },
    {'lat': 53.921111, 'lng': 27.752500
     },
    {'lat': 53.934722, 'lng': 27.678888
     },
]


poly224 = [
    {'lat': 53.940865, 'lng': 27.778599
     },
    {'lat': 53.942043, 'lng': 27.779452
     },
    {'lat': 53.943446, 'lng': 27.784967
     },
    {'lat': 53.942954, 'lng': 27.786428
     },
    {'lat': 53.937045, 'lng': 27.791544
     },
    {'lat': 53.935416, 'lng': 27.782688
     },
    {'lat': 53.940865, 'lng': 27.778599
     },
]

poly225 = [
    {'lat': 53.898611, 'lng': 27.602500
     },
    {'lat': 53.899444, 'lng': 27.601666
     },
    {'lat': 53.899166, 'lng': 27.600555
     },
    {'lat': 53.898333, 'lng': 27.601388
     },
    {'lat': 53.898611, 'lng': 27.602500
     },
]


poly226 = [
    {'lat': 53.171686, 'lng': 29.177448
     },
    {'lat': 53.165110, 'lng': 29.179909
     },
    {'lat': 53.165543, 'lng': 29.183136
     },
    {'lat': 53.172809, 'lng': 29.181353
     },
    {'lat': 53.171686, 'lng': 29.177448
     },
]


poly227 = [
    {'lat': 53.330734, 'lng': 28.582805
     },
    {'lat': 53.326386, 'lng': 28.576711
     },
    {'lat': 53.319567, 'lng': 28.590348
     },
    {'lat': 53.323915, 'lng': 28.596442
     },
    {'lat': 53.330734, 'lng': 28.582805
     },
]


poly228 = [
    {'lat': 53.096944, 'lng': 26.681666
     },
    {'lat': 53.099444, 'lng': 26.688611
     },
    {'lat': 53.095555, 'lng': 26.693055
     },
    {'lat': 53.093333, 'lng': 26.683333
     },
    {'lat': 53.096944, 'lng': 26.681666
     },
]


poly229 = [
    {'lat': 53.872419, 'lng': 30.392488
     },
    {'lat': 53.875613, 'lng': 30.399305
     },
    {'lat': 53.877901, 'lng': 30.396980
     },
    {'lat': 53.874069, 'lng': 30.390186
     },
    {'lat': 53.872419, 'lng': 30.392488
     },
]


poly230 = [
    {'lat': 54.016388, 'lng': 28.189722
     },
    {'lat': 54.020555, 'lng': 28.201111
     },
    {'lat': 54.021666, 'lng': 28.201944
     },
    {'lat': 54.021944, 'lng': 28.199722
     },
    {'lat': 54.017777, 'lng': 28.188333
     },
    {'lat': 54.017222, 'lng': 28.188611
     },
    {'lat': 54.016388, 'lng': 28.189722
     },
]


poly231 = [
    {'lat': 51.992222, 'lng': 29.137500
     },
    {'lat': 51.961944, 'lng': 29.169166
     },
    {'lat': 51.971666, 'lng': 29.193611
     },
    {'lat': 52.001944, 'lng': 29.161944
     },
    {'lat': 51.992222, 'lng': 29.137500
     },
]


poly232 = [
    {'lat': 53.908333, 'lng': 27.582222
     },
    {'lat': 53.907500, 'lng': 27.580555
     },
    {'lat': 53.906388, 'lng': 27.582222
     },
    {'lat': 53.906944, 'lng': 27.583333
     },
    {'lat': 53.908333, 'lng': 27.582222
     },
]

poly233 = [
    {'lat': 55.199444, 'lng': 30.204444
     },
    {'lat': 55.199722, 'lng': 30.202222
     },
    {'lat': 55.198055, 'lng': 30.201944
     },
    {'lat': 55.198055, 'lng': 30.204166
     },
    {'lat': 55.199444, 'lng': 30.204444
     },
]

poly234 = [
    {'lat': 53.906666, 'lng': 30.345000
     },
    {'lat': 53.905277, 'lng': 30.344722
     },
    {'lat': 53.905277, 'lng': 30.346111
     },
    {'lat': 53.906388, 'lng': 30.346944
     },
    {'lat': 53.906666, 'lng': 30.345000
     },
]


poly235 = [
    {'lat': 52.426944, 'lng': 31.016666
     },
    {'lat': 52.426111, 'lng': 31.015555
     },
    {'lat': 52.425000, 'lng': 31.016388
     },
    {'lat': 52.425833, 'lng': 31.018888
     },
    {'lat': 52.426944, 'lng': 31.016666
     },
]


poly236 = [
    {'lat': 52.095555, 'lng': 23.682777
     },
    {'lat': 52.094722, 'lng': 23.681111
     },
    {'lat': 52.093611, 'lng': 23.681944
     },
    {'lat': 52.094722, 'lng': 23.684166
     },
    {'lat': 52.095555, 'lng': 23.682777
     },
]


poly237 = [
    {'lat': 53.683055, 'lng': 23.832500
     },
    {'lat': 53.681388, 'lng': 23.832222
     },
    {'lat': 53.681111, 'lng': 23.835277
     },
    {'lat': 53.683055, 'lng': 23.835277
     },
    {'lat': 53.683055, 'lng': 23.832500
     },
]


poly238 = [
    {'lat': 54.323333, 'lng': 26.872777
     },
    {'lat': 54.320277, 'lng': 26.871944
     },
    {'lat': 54.318888, 'lng': 26.888611
     },
    {'lat': 54.322222, 'lng': 26.889444
     },
    {'lat': 54.323333, 'lng': 26.872777
     },
]


poly239 = [
    {'lat': 53.920833, 'lng': 27.629722
     },
    {'lat': 53.921111, 'lng': 27.626944
     },
    {'lat': 53.920000, 'lng': 27.625555
     },
    {'lat': 53.919166, 'lng': 27.629166
     },
    {'lat': 53.920833, 'lng': 27.629722
     },
]


poly240 = [
    {'lat': 54.066388, 'lng': 28.028888
     },
    {'lat': 54.061666, 'lng': 28.028055
     },
    {'lat': 54.062222, 'lng': 28.038055
     },
    {'lat': 54.066666, 'lng': 28.036666
     },
    {'lat': 54.066388, 'lng': 28.028888
     },
]


poly241 = [
    {'lat': 53.965000, 'lng': 27.641388
     },
    {'lat': 53.981111, 'lng': 27.651388
     },
    {'lat': 53.986111, 'lng': 27.628055
     },
    {'lat': 53.970307, 'lng': 27.613096
     },
    {'lat': 53.965000, 'lng': 27.641388
     },
]

poly243 = [
    {'lat': 53.895000, 'lng': 27.534722
     },
    {'lat': 53.885555, 'lng': 27.551111
     },
    {'lat': 53.893333, 'lng': 27.571944
     },
    {'lat': 53.898611, 'lng': 27.574444
     },
    {'lat': 53.907777, 'lng': 27.561388
     },
    {'lat': 53.909166, 'lng': 27.557777
     },
    {'lat': 53.907500, 'lng': 27.556388
     },
    {'lat': 53.900277, 'lng': 27.546111
     },
    {'lat': 53.895000, 'lng': 27.534722
     },
]


poly244 = [
    {'lat': 53.911944, 'lng': 27.548055
     },
    {'lat': 53.909444, 'lng': 27.551111
     },
    {'lat': 53.910833, 'lng': 27.553611
     },
    {'lat': 53.912500, 'lng': 27.551944
     },
    {'lat': 53.911944, 'lng': 27.548055
     },
]


poly245 = [
    {'lat': 53.929444, 'lng': 27.516111
     },
    {'lat': 53.923055, 'lng': 27.528611
     },
    {'lat': 53.930000, 'lng': 27.530000
     },
    {'lat': 53.929444, 'lng': 27.516111
     },
]


poly246 = [
    {'lat': 53.936666, 'lng': 27.479444
     },
    {'lat': 53.933888, 'lng': 27.478333
     },
    {'lat': 53.933055, 'lng': 27.493333
     },
    {'lat': 53.936111, 'lng': 27.492500
     },
    {'lat': 53.936666, 'lng': 27.479444
     },
]


poly247 = [
    {'lat': 53.991111, 'lng': 27.422777
     },
    {'lat': 53.956111, 'lng': 27.428611
     },
    {'lat': 53.954444, 'lng': 27.440833
     },
    {'lat': 53.990833, 'lng': 27.464722
     },
    {'lat': 53.991111, 'lng': 27.422777
     },
]


poly248 = [
    {'lat': 54.256388, 'lng': 27.400277
     },
    {'lat': 54.178333, 'lng': 27.342500
     },
    {'lat': 54.163055, 'lng': 27.381666
     },
    {'lat': 54.221666, 'lng': 27.490555
     },
    {'lat': 54.256388, 'lng': 27.400277
     },
]


poly249 = [
    {'lat': 54.362222, 'lng': 30.287777
     },
    {'lat': 54.367222, 'lng': 30.270000
     },
    {'lat': 54.349166, 'lng': 30.245833
     },
    {'lat': 54.337222, 'lng': 30.283333
     },
    {'lat': 54.362222, 'lng': 30.287777
     },
]


poly250 = [
    {'lat': 53.905000, 'lng': 27.565555
     },
    {'lat': 53.903333, 'lng': 27.568055
     },
    {'lat': 53.910000, 'lng': 27.578611
     },
    {'lat': 53.913611, 'lng': 27.582500
     },
    {'lat': 53.916111, 'lng': 27.586111
     },
    {'lat': 53.921666, 'lng': 27.601388
     },
    {'lat': 53.922222, 'lng': 27.609166
     },
    {'lat': 53.938055, 'lng': 27.667500
     },
    {'lat': 53.955000, 'lng': 27.721388
     },
    {'lat': 53.968055, 'lng': 27.750277
     },
    {'lat': 53.983055, 'lng': 27.786388
     },
    {'lat': 53.988888, 'lng': 27.802500
     },
    {'lat': 54.007777, 'lng': 27.855000
     },
    {'lat': 54.013333, 'lng': 27.884722
     },
    {'lat': 54.011388, 'lng': 27.895833
     },
    {'lat': 53.986666, 'lng': 27.923333
     },
    {'lat': 53.976111, 'lng': 27.938888
     },
    {'lat': 53.977222, 'lng': 27.941111
     },
    {'lat': 53.988333, 'lng': 27.925555
     },
    {'lat': 54.003055, 'lng': 27.910833
     },
    {'lat': 54.018888, 'lng': 27.891944
     },
    {'lat': 54.009722, 'lng': 27.853888
     },
    {'lat': 53.984444, 'lng': 27.784444
     },
    {'lat': 53.969722, 'lng': 27.748055
     },
    {'lat': 53.956388, 'lng': 27.719444
     },
    {'lat': 53.939444, 'lng': 27.666111
     },
    {'lat': 53.923888, 'lng': 27.608333
     },
    {'lat': 53.923055, 'lng': 27.600833
     },
    {'lat': 53.922222, 'lng': 27.597222
     },
    {'lat': 53.917222, 'lng': 27.584444
     },
    {'lat': 53.914444, 'lng': 27.580000
     },
    {'lat': 53.910833, 'lng': 27.576388
     },
    {'lat': 53.905000, 'lng': 27.565555
     },
]


poly251 = [
    {'lat': 53.904722, 'lng': 27.552500
     },
    {'lat': 53.905979, 'lng': 27.554144
     },
    {'lat': 53.912777, 'lng': 27.547222
     },
    {'lat': 53.915000, 'lng': 27.540833
     },
    {'lat': 53.918333, 'lng': 27.536111
     },
    {'lat': 53.923888, 'lng': 27.526944
     },
    {'lat': 53.931666, 'lng': 27.511944
     },
    {'lat': 53.936388, 'lng': 27.498333
     },
    {'lat': 53.937777, 'lng': 27.493055
     },
    {'lat': 53.938611, 'lng': 27.480000
     },
    {'lat': 53.939444, 'lng': 27.475000
     },
    {'lat': 53.950555, 'lng': 27.449166
     },
    {'lat': 53.951666, 'lng': 27.444166
     },
    {'lat': 53.950277, 'lng': 27.443055
     },
    {'lat': 53.949166, 'lng': 27.447777
     },
    {'lat': 53.937777, 'lng': 27.473888
     },
    {'lat': 53.936666, 'lng': 27.479444
     },
    {'lat': 53.936111, 'lng': 27.492500
     },
    {'lat': 53.935000, 'lng': 27.496666
     },
    {'lat': 53.930277, 'lng': 27.510277
     },
    {'lat': 53.922777, 'lng': 27.525000
     },
    {'lat': 53.915833, 'lng': 27.534166
     },
    {'lat': 53.913611, 'lng': 27.538611
     },
    {'lat': 53.911666, 'lng': 27.545277
     },
    {'lat': 53.904722, 'lng': 27.552500
     },
]


poly252 = [
    {'lat': 53.951666, 'lng': 27.444166
     },
    {'lat': 53.950555, 'lng': 27.449166
     },
    {'lat': 53.963333, 'lng': 27.466111
     },
    {'lat': 53.966111, 'lng': 27.478333
     },
    {'lat': 53.970555, 'lng': 27.585833
     },
    {'lat': 53.968888, 'lng': 27.597500
     },
    {'lat': 53.944166, 'lng': 27.667500
     },
    {'lat': 53.940000, 'lng': 27.667777
     },
    {'lat': 53.942777, 'lng': 27.676944
     },
    {'lat': 53.945277, 'lng': 27.670277
     },
    {'lat': 53.970555, 'lng': 27.598888
     },
    {'lat': 53.972222, 'lng': 27.585833
     },
    {'lat': 53.967777, 'lng': 27.477777
     },
    {'lat': 53.965000, 'lng': 27.465000
     },
    {'lat': 53.961388, 'lng': 27.457500
     },
    {'lat': 53.951666, 'lng': 27.444166
     },
]


poly253 = [
    {'lat': 53.961944, 'lng': 27.623333
     },
    {'lat': 53.958888, 'lng': 27.631666
     },
    {'lat': 53.961388, 'lng': 27.639166
     },
    {'lat': 53.963611, 'lng': 27.643888
     },
    {'lat': 53.978333, 'lng': 27.654722
     },
    {'lat': 53.985833, 'lng': 27.657777
     },
    {'lat': 54.006666, 'lng': 27.658888
     },
    {'lat': 54.011666, 'lng': 27.660555
     },
    {'lat': 54.018888, 'lng': 27.665277
     },
    {'lat': 54.025555, 'lng': 27.672777
     },
    {'lat': 54.036111, 'lng': 27.693333
     },
    {'lat': 54.041111, 'lng': 27.699166
     },
    {'lat': 54.046388, 'lng': 27.702500
     },
    {'lat': 54.051111, 'lng': 27.706666
     },
    {'lat': 54.049166, 'lng': 27.700555
     },
    {'lat': 54.046666, 'lng': 27.699722
     },
    {'lat': 54.041944, 'lng': 27.696666
     },
    {'lat': 54.037500, 'lng': 27.691111
     },
    {'lat': 54.026944, 'lng': 27.670555
     },
    {'lat': 54.019722, 'lng': 27.662777
     },
    {'lat': 54.012222, 'lng': 27.657500
     },
    {'lat': 54.006944, 'lng': 27.655833
     },
    {'lat': 53.986388, 'lng': 27.654722
     },
    {'lat': 53.965000, 'lng': 27.641388
     },
    {'lat': 53.963055, 'lng': 27.637500
     },
    {'lat': 53.961944, 'lng': 27.623333
     },
]

poly254 = [
    {'lat': 53.961944, 'lng': 27.623333
     },
    {'lat': 53.958888, 'lng': 27.631666
     },
    {'lat': 53.961388, 'lng': 27.639166
     },
    {'lat': 53.963611, 'lng': 27.643888
     },
    {'lat': 53.978333, 'lng': 27.654722
     },
    {'lat': 53.985833, 'lng': 27.657777
     },
    {'lat': 54.006666, 'lng': 27.658888
     },
    {'lat': 54.011666, 'lng': 27.660555
     },
    {'lat': 54.018888, 'lng': 27.665277
     },
    {'lat': 54.025555, 'lng': 27.672777
     },
    {'lat': 54.036111, 'lng': 27.693333
     },
    {'lat': 54.041111, 'lng': 27.699166
     },
    {'lat': 54.046388, 'lng': 27.702500
     },
    {'lat': 54.051111, 'lng': 27.706666
     },
    {'lat': 54.049166, 'lng': 27.700555
     },
    {'lat': 54.046666, 'lng': 27.699722
     },
    {'lat': 54.041944, 'lng': 27.696666
     },
    {'lat': 54.037500, 'lng': 27.691111
     },
    {'lat': 54.026944, 'lng': 27.670555
     },
    {'lat': 54.019722, 'lng': 27.662777
     },
    {'lat': 54.012222, 'lng': 27.657500
     },
    {'lat': 54.006944, 'lng': 27.655833
     },
    {'lat': 53.986388, 'lng': 27.654722
     },
    {'lat': 53.965000, 'lng': 27.641388
     },
    {'lat': 53.963055, 'lng': 27.637500
     },
    {'lat': 53.961944, 'lng': 27.623333
     },
]


poly255 = [
    {'lat': 54.427500, 'lng': 30.104166
     },
    {'lat': 54.349444, 'lng': 30.180555
     },
    {'lat': 54.451944, 'lng': 30.488611
     },
    {'lat': 54.530000, 'lng': 30.411944
     },
    {'lat': 54.427500, 'lng': 30.104166
     },
]


poly256 = [
    {'lat': 55.039166, 'lng': 30.229722
     },
    {'lat': 55.133611, 'lng': 30.543055
     },
    {'lat': 55.213055, 'lng': 30.470000
     },
    {'lat': 55.118611, 'lng': 30.156666
     },
    {'lat': 55.039166, 'lng': 30.229722
     },
]


poly257 = [
    {'lat': 53.998055, 'lng': 29.920555
     },
    {'lat': 53.850833, 'lng': 30.156944
     },
    {'lat': 53.912500, 'lng': 30.267500
     },
    {'lat': 54.060000, 'lng': 30.031388
     },
    {'lat': 53.998055, 'lng': 29.920555
     },
]

poly258 = [
    {'lat': 53.932500, 'lng': 27.854722
     },
    {'lat': 53.773055, 'lng': 28.091944
     },
    {'lat': 53.832222, 'lng': 28.206111
     },
    {'lat': 53.991944, 'lng': 27.969444
     },
    {'lat': 53.932500, 'lng': 27.854722
     },
]

poly259 = [
    {'lat': 52.520833, 'lng': 30.835000
     },
    {'lat': 52.448888, 'lng': 31.145833
     },
    {'lat': 52.533055, 'lng': 31.198055
     },
    {'lat': 52.605000, 'lng': 30.887222
     },
    {'lat': 52.520833, 'lng': 30.835000
     },
]


poly260 = [
    {'lat': 52.108333, 'lng': 23.715555
     },
    {'lat': 52.025833, 'lng': 24.017222
     },
    {'lat': 52.108055, 'lng': 24.076666
     },
    {'lat': 52.212500, 'lng': 23.747777
     },
    {'lat': 52.191666, 'lng': 23.723888
     },
    {'lat': 52.172500, 'lng': 23.760277
     },
    {'lat': 52.108333, 'lng': 23.715555
     },
]


poly261 = [
    {'lat': 53.701666, 'lng': 23.972222
     },
    {'lat': 53.498611, 'lng': 23.983611
     },
    {'lat': 53.502222, 'lng': 24.134722
     },
    {'lat': 53.704722, 'lng': 24.124166
     },
    {'lat': 53.701666, 'lng': 23.972222
     },
]

poly262 = [
    {'lat': 53.658076, 'lng': 23.882085
     },
    {'lat': 53.656381, 'lng': 23.974804
     },
    {'lat': 53.672088, 'lng': 23.973673
     },
    {'lat': 53.693418, 'lng': 23.883459
     },
    {'lat': 53.658087, 'lng': 23.882067
     },
]

poly263 = [
    {'lat': 52.637180, 'lng': 29.761897
     },
    {'lat': 52.605345, 'lng': 29.733137
     },
    {'lat': 52.588182, 'lng': 29.783420
     },
    {'lat': 52.608735, 'lng': 29.801515
     },
    {'lat': 52.635947, 'lng': 29.779244
     },
    {'lat': 52.637180, 'lng': 29.761897
     },
]


poly264 = [
    {'lat': 52.172571, 'lng': 26.141921
     },
    {'lat': 52.178989, 'lng': 26.114257
     },
    {'lat': 52.192607, 'lng': 26.122617
     },
    {'lat': 52.186191, 'lng': 26.150282
     },
    {'lat': 52.172571, 'lng': 26.141921
     },
]

poly265 = [
    {'lat': 53.198341, 'lng': 29.192227
     },
    {'lat': 53.181727, 'lng': 29.208156
     },
    {'lat': 53.177306, 'lng': 29.195377
     },
    {'lat': 53.193921, 'lng': 29.179448
     },
    {'lat': 53.198341, 'lng': 29.192227
     },
]


poly266 = [
    {'lat': 52.118028, 'lng': 26.095031
     },
    {'lat': 52.111938, 'lng': 26.068933
     },
    {'lat': 52.103710, 'lng': 26.067802
     },
    {'lat': 52.096923, 'lng': 26.097293
     },
    {'lat': 52.108625, 'lng': 26.108689
     },
    {'lat': 52.118028, 'lng': 26.095031
     },
]


poly267 = [
    {'lat': 52.144284, 'lng': 23.739962
     },
    {'lat': 52.125254, 'lng': 23.726652
     },
    {'lat': 52.133771, 'lng': 23.713003
     },
    {'lat': 52.146697, 'lng': 23.718223
     },
    {'lat': 52.144338, 'lng': 23.740136
     },
]


poly268 = [
    {'lat': 53.654067, 'lng': 23.974694
     },
    {'lat': 53.633924, 'lng': 23.975843
     },
    {'lat': 53.639211, 'lng': 23.957992
     },
    {'lat': 53.651264, 'lng': 23.958018
     },
    {'lat': 53.654067, 'lng': 23.974738
     },
]


poly269 = [
    {'lat': 53.802664, 'lng': 25.376892
     },
    {'lat': 53.784454, 'lng': 25.387941
     },
    {'lat': 53.783934, 'lng': 25.364718
     },
    {'lat': 53.799003, 'lng': 25.362630
     },
    {'lat': 53.802716, 'lng': 25.376805
     },
]


poly270 = [
    {'lat': 53.823327, 'lng': 27.584306
     },
    {'lat': 53.817313, 'lng': 27.587916
     },
    {'lat': 53.819442, 'lng': 27.591183
     },
    {'lat': 53.823423, 'lng': 27.588791
     },
    {'lat': 53.823327, 'lng': 27.584306
     },
]


poly271 = [
    {'lat': 53.869218, 'lng': 27.647004
     },
    {'lat': 53.861620, 'lng': 27.641291
     },
    {'lat': 53.858149, 'lng': 27.641296
     },
    {'lat': 53.855555, 'lng': 27.636316
     },
    {'lat': 53.850277, 'lng': 27.652500
     },
    {'lat': 53.850555, 'lng': 27.671944
     },
    {'lat': 53.857840, 'lng': 27.677286
     },
    {'lat': 53.861578, 'lng': 27.668546
     },
    {'lat': 53.862854, 'lng': 27.651820
     },
    {'lat': 53.864595, 'lng': 27.651154
     },
    {'lat': 53.864374, 'lng': 27.649159
     },
    {'lat': 53.869218, 'lng': 27.647004
     },
]

poly272 = [
    {'lat': 54.099034, 'lng': 28.307552
     },
    {'lat': 54.107107, 'lng': 28.339434
     },
    {'lat': 54.104626, 'lng': 28.344287
     },
    {'lat': 54.095858, 'lng': 28.329108
     },
    {'lat': 54.099034, 'lng': 28.307552
     },
]


poly273 = [
    {'lat': 52.843069, 'lng': 30.019871
     },
    {'lat': 52.865027, 'lng': 30.029266
     },
    {'lat': 52.881200, 'lng': 29.965238
     },
    {'lat': 52.869438, 'lng': 29.950797
     },
    {'lat': 52.835922, 'lng': 29.980549
     },
    {'lat': 52.843069, 'lng': 30.019821
     },
]

poly274 = [
    {'lat': 52.423356, 'lng': 30.939401
     },
    {'lat': 52.422505, 'lng': 30.945404
     },
    {'lat': 52.411175, 'lng': 30.943577
     },
    {'lat': 52.413941, 'lng': 30.930789
     },
    {'lat': 52.423356, 'lng': 30.939401
     },
]

poly275 = [
    {'lat': 52.108832, 'lng': 23.666495
     },
    {'lat': 52.101675, 'lng': 23.672672
     },
    {'lat': 52.103553, 'lng': 23.678409
     },
    {'lat': 52.110709, 'lng': 23.672233
     },
    {'lat': 52.108832, 'lng': 23.666495
     }]

poly276 = [
    {'lat': 53.116746, 'lng': 26.039721
     },
    {'lat': 53.119515, 'lng': 26.037581
     },
    {'lat': 53.120575, 'lng': 26.034150
     },
    {'lat': 53.122346, 'lng': 26.032457
     },
    {'lat': 53.123533, 'lng': 26.034585
     },
    {'lat': 53.123883, 'lng': 26.037222
     },
    {'lat': 53.122338, 'lng': 26.038938
     },
    {'lat': 53.124083, 'lng': 26.043592
     },
    {'lat': 53.122474, 'lng': 26.049043
     },
    {'lat': 53.116746, 'lng': 26.039721
     },
]

poly277 = [
    {'lat': 53.949105, 'lng': 27.696360
     },
    {'lat': 53.952637, 'lng': 27.707446
     },
    {'lat': 53.956850, 'lng': 27.703588
     },
    {'lat': 53.953316, 'lng': 27.692502
     },
    {'lat': 53.949105, 'lng': 27.696360
     },
]


poly278 = [
    {'lat': 53.199911, 'lng': 29.190814
     },
    {'lat': 53.184759, 'lng': 29.205299
     },
    {'lat': 53.184785, 'lng': 29.223437
     },
    {'lat': 53.201060, 'lng': 29.224437
     },
    {'lat': 53.204899, 'lng': 29.206473
     },
    {'lat': 53.199911, 'lng': 29.190814
     },
]

poly279 = [
    {'lat': 53.928063, 'lng': 27.509195
     },
    {'lat': 53.928998, 'lng': 27.512605
     },
    {'lat': 53.927108, 'lng': 27.516398
     },
    {'lat': 53.925003, 'lng': 27.513475
     },
    {'lat': 53.928053, 'lng': 27.509195
     },
]


poly280 = [
    {'lat': 53.924081, 'lng': 27.546464
     },
    {'lat': 53.922154, 'lng': 27.548552
     },
    {'lat': 53.921696, 'lng': 27.547333
     },
    {'lat': 53.923623, 'lng': 27.545246
     },
    {'lat': 53.924081, 'lng': 27.546464
     },
]


poly281 = [
    {'lat': 53.939482, 'lng': 27.490037
     },
    {'lat': 53.940479, 'lng': 27.490838
     },
    {'lat': 53.940372, 'lng': 27.491221
     },
    {'lat': 53.939376, 'lng': 27.490420
     },
    {'lat': 53.939482, 'lng': 27.490037
     },
]

polygone22 = [
    {'lat': 56.138410, 'lng': 28.160264
     },
    {'lat': 56.143333, 'lng': 28.155555
     },
    {'lat': 56.095000, 'lng': 28.046111
     },
    {'lat': 56.076388, 'lng': 27.990555
     },
    {'lat': 56.029722, 'lng': 27.941111
     },
    {'lat': 56.029166, 'lng': 27.918888
     },
    {'lat': 56.021944, 'lng': 27.876944
     },
    {'lat': 55.968333, 'lng': 27.841666
     },
    {'lat': 55.888611, 'lng': 27.671111
     },
    {'lat': 55.859166, 'lng': 27.677777
     },
    {'lat': 55.853888, 'lng': 27.775833
     },
    {'lat': 55.816111, 'lng': 27.771388
     },
    {'lat': 55.803888, 'lng': 27.668888
     },
    {'lat': 55.759444, 'lng': 27.648888
     },
    {'lat': 55.762777, 'lng': 27.513055
     },
    {'lat': 55.756944, 'lng': 27.291388
     },
    {'lat': 55.767500, 'lng': 27.240000
     },
    {'lat': 55.818055, 'lng': 27.150555
     },
    {'lat': 55.801111, 'lng': 27.097222
     },
    {'lat': 55.797222, 'lng': 27.019166
     },
    {'lat': 55.744722, 'lng': 26.940555
     },
    {'lat': 55.725555, 'lng': 26.938888
     },
    {'lat': 55.681666, 'lng': 26.927500
     },
    {'lat': 55.683333, 'lng': 26.855000
     },
    {'lat': 55.662222, 'lng': 26.820555
     },
    {'lat': 55.655000, 'lng': 26.784444
     },
    {'lat': 55.633888, 'lng': 26.688333
     },
    {'lat': 55.565277, 'lng': 26.672500
     },
    {'lat': 55.515833, 'lng': 26.608333
     },
    {'lat': 55.358888, 'lng': 26.680277
     },
    {'lat': 55.338888, 'lng': 26.836944
     },
    {'lat': 55.317500, 'lng': 26.914444
     },
    {'lat': 55.266666, 'lng': 26.869722
     },
    {'lat': 55.176111, 'lng': 26.750555
     },
    {'lat': 55.123333, 'lng': 26.726666
     },
    {'lat': 55.121666, 'lng': 26.535277
     },
    {'lat': 55.108611, 'lng': 26.472222
     },
    {'lat': 55.074444, 'lng': 26.404444
     },
    {'lat': 55.082222, 'lng': 26.343888
     },
    {'lat': 54.981111, 'lng': 26.254166
     },
    {'lat': 54.953055, 'lng': 26.139722
     },
    {'lat': 54.883055, 'lng': 26.097777
     },
    {'lat': 54.849166, 'lng': 25.937500
     },
    {'lat': 54.782222, 'lng': 25.797222
     },
    {'lat': 54.722777, 'lng': 25.785000
     },
    {'lat': 54.609166, 'lng': 25.797777
     },
    {'lat': 54.612222, 'lng': 25.931666
     },
    {'lat': 54.573333, 'lng': 25.930833
     },
    {'lat': 54.573611, 'lng': 25.800833
     },
    {'lat': 54.519722, 'lng': 25.756666
     },
    {'lat': 54.438333, 'lng': 25.694444
     },
    {'lat': 54.406388, 'lng': 25.780555
     },
    {'lat': 54.174444, 'lng': 25.865277
     },
    {'lat': 54.079444, 'lng': 25.790000
     },
    {'lat': 54.070000, 'lng': 25.742777
     },
    {'lat': 54.089444, 'lng': 25.586111
     },
    {'lat': 54.127222, 'lng': 25.488888
     },
    {'lat': 54.194722, 'lng': 25.456666
     },
    {'lat': 54.216388, 'lng': 25.509166
     },
    {'lat': 54.266666, 'lng': 25.483333
     },
    {'lat': 54.237777, 'lng': 25.380555
     },
    {'lat': 54.226388, 'lng': 25.260000
     },
    {'lat': 54.187222, 'lng': 25.236111
     },
    {'lat': 54.130000, 'lng': 25.116944
     },
    {'lat': 54.110277, 'lng': 25.082500
     },
    {'lat': 54.096388, 'lng': 24.993611
     },
    {'lat': 54.129722, 'lng': 24.958888
     },
    {'lat': 54.105277, 'lng': 24.844722
     },
    {'lat': 54.051944, 'lng': 24.909166
     },
    {'lat': 54.018055, 'lng': 24.901944
     },
    {'lat': 53.975277, 'lng': 24.834722
     },
    {'lat': 53.921388, 'lng': 24.832222
     },
    {'lat': 53.907777, 'lng': 24.802222
     },
    {'lat': 53.906111, 'lng': 24.642500
     },
    {'lat': 53.941111, 'lng': 24.562500
     },
    {'lat': 53.838055, 'lng': 24.405833
     },
    {'lat': 53.905833, 'lng': 24.190277
     },
    {'lat': 53.846388, 'lng': 24.155277
     },
    {'lat': 53.845833, 'lng': 24.101666
     },
    {'lat': 53.903055, 'lng': 24.070277
     },
    {'lat': 53.848333, 'lng': 23.609166
     },
    {'lat': 53.733032, 'lng': 23.634517
     },
    {'lat': 53.732278, 'lng': 23.665573
     },
    {'lat': 53.707777, 'lng': 23.684166
     },
    {'lat': 53.688888, 'lng': 23.644722
     },
    {'lat': 53.526111, 'lng': 23.713611
     },
    {'lat': 53.286111, 'lng': 23.845277
     },
    {'lat': 53.188611, 'lng': 23.946944
     },
    {'lat': 53.123055, 'lng': 23.971111
     },
    {'lat': 53.095277, 'lng': 23.939166
     },
    {'lat': 53.047500, 'lng': 23.959166
     },
    {'lat': 52.929166, 'lng': 24.000000
     },
    {'lat': 52.698055, 'lng': 23.992777
     },
    {'lat': 52.616666, 'lng': 23.987777
     },
    {'lat': 52.584166, 'lng': 23.835833
     },
    {'lat': 52.513055, 'lng': 23.482222
     },
    {'lat': 52.377222, 'lng': 23.406944
     },
    {'lat': 52.380000, 'lng': 23.343888
     },
    {'lat': 52.281944, 'lng': 23.252777
     },
    {'lat': 52.178611, 'lng': 23.659722
     },
    {'lat': 52.136388, 'lng': 23.642500
     },
    {'lat': 52.053333, 'lng': 23.714444
     },
    {'lat': 51.994722, 'lng': 23.736111
     },
    {'lat': 51.932500, 'lng': 23.688055
     },
    {'lat': 51.797500, 'lng': 23.683333
     },
    {'lat': 51.749166, 'lng': 23.653888
     },
    {'lat': 51.730833, 'lng': 23.589444
     },
    {'lat': 51.670555, 'lng': 23.596111
     },
    {'lat': 51.693888, 'lng': 23.782500
     },
    {'lat': 51.683333, 'lng': 23.819166
     },
    {'lat': 51.651111, 'lng': 23.940000
     },
    {'lat': 51.622222, 'lng': 23.981111
     },
    {'lat': 51.738055, 'lng': 24.166388
     },
    {'lat': 51.775555, 'lng': 24.158888
     },
    {'lat': 51.782500, 'lng': 24.211111
     },
    {'lat': 51.898888, 'lng': 24.336111
     },
    {'lat': 51.974444, 'lng': 24.608611
     },
    {'lat': 51.920000, 'lng': 24.688055
     },
    {'lat': 51.996666, 'lng': 25.053055
     },
    {'lat': 52.002222, 'lng': 25.579166
     },
    {'lat': 51.959722, 'lng': 26.012500
     },
    {'lat': 51.931388, 'lng': 26.122222
     },
    {'lat': 51.902222, 'lng': 26.252777
     },
    {'lat': 51.901111, 'lng': 26.431111
     },
    {'lat': 51.888333, 'lng': 26.519722
     },
    {'lat': 51.852222, 'lng': 26.552500
     },
    {'lat': 51.856666, 'lng': 26.707777
     },
    {'lat': 51.877777, 'lng': 26.793888
     },
    {'lat': 51.795555, 'lng': 26.866388
     },
    {'lat': 51.800277, 'lng': 27.246666
     },
    {'lat': 51.723333, 'lng': 27.251666
     },
    {'lat': 51.640833, 'lng': 27.350000
     },
    {'lat': 51.697222, 'lng': 27.545555
     },
    {'lat': 51.652777, 'lng': 27.628055
     },
    {'lat': 51.651666, 'lng': 27.901666
     },
    {'lat': 51.734444, 'lng': 28.056944
     },
    {'lat': 51.731388, 'lng': 28.311388
     },
    {'lat': 51.571111, 'lng': 28.776944
     },
    {'lat': 51.728888, 'lng': 29.177777
     },
    {'lat': 51.516666, 'lng': 29.369722
     },
    {'lat': 51.560277, 'lng': 29.776944
     },
    {'lat': 51.540833, 'lng': 30.208055
     },
    {'lat': 51.457500, 'lng': 30.378611
     },
    {'lat': 51.325833, 'lng': 30.491666
     },
    {'lat': 51.333888, 'lng': 30.563888
     },
    {'lat': 51.632500, 'lng': 30.437500
     },
    {'lat': 51.838333, 'lng': 30.616111
     },
    {'lat': 51.963888, 'lng': 30.762500
     },
    {'lat': 52.113888, 'lng': 30.921388
     },
    {'lat': 52.133333, 'lng': 31.148333
     },
    {'lat': 52.090000, 'lng': 31.239444
     },
    {'lat': 52.166944, 'lng': 31.372777
     },
    {'lat': 52.162777, 'lng': 31.782222
     },
]


polys = [poly200, poly201, poly202, poly203, poly204, poly205, poly206, poly207, poly208, poly209, poly210, poly211, poly212, poly213, poly214, poly215, poly216, poly217, poly218, poly219, poly220, poly221, poly222, poly223, poly224, poly225, poly226, poly227, poly228, poly229, poly230, poly231, poly232, poly233, poly234, poly235, poly236, poly237, poly238, poly239,
         poly240, poly241, poly243, poly244, poly245, poly246, poly247, poly248, poly249, poly250, poly251, poly252, poly253, poly254, poly255, poly256, poly257, poly258, poly259, poly260, poly261, poly262, poly263, poly264, poly265, poly266, poly267, poly268, poly269, poly270, poly271, poly272, poly273, poly274, poly275, poly276, poly277, poly278, poly279, poly280]

# print(polys)
# print(circles)

polyJson = {}
polyArray = []


i = 0

for poly in polys :

    tempArray = []

    tempC = []
    for c in poly:
        tempC.append(c['lat'])
        tempC.append(c['lng'])
        tempArray.append(tempC)
        tempC = []
    
    polyT={}
    polyT["coordinates"] = tempArray

    polyArray.append(polyT)

circleArray = []
for name in circles:
    data = circles[name]
    circleArray.append(data)
    


with open('circles.json', 'w') as z:
    json.dump(circleArray, z)

with open('polys.json', 'w') as z:
    json.dump(polyArray, z)
