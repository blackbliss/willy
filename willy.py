#!/usr/bin/env python
# encoding: utf-8
"""
willy.py
An awesome webradio written in Python and AngularJS

Authors:
- Daniele Costarella <daniele.costarella@gmail.com>
- Matteo Sticco <matteo.sticco@gmail.com>
Copyright (c) 2017 ${TM_ORGANIZATION_NAME}. All rights reserved.
"""

from flask import Flask, request, render_template
from radio import RadioPlayer
import json

app = Flask(__name__, static_path='/static')

radio = RadioPlayer()


@app.route('/')
def hello():
    return render_template('stations.html')
    #return 'Great, it works!!!'


@app.route('/api/stations', methods=['GET'])
def getStations():
    print 'Retrieving stations...'

    radios = radio.get_stations()

    # with open('_radio_stations.json') as data_file:
    #     radios = json.load(data_file)

    #radio.play_station("RTL 102.5")
    
    return json.dumps(radios)


@app.route('/api/stations', methods=['POST'])
def addStations():
    return 'Adding stations... (todo)'


@app.route('/api/play-station', methods=['GET'])
def playStation():
    print "Playing radio station.."
    radio.play_station("RTL 102.5")

    return ('', 200)


if __name__ == '__main__':
    # Run and make server accessible from any
    # computer in the network
    app.run(host='0.0.0.0', port=8080, debug=True)
