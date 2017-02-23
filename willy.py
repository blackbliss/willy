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
import json

app = Flask(__name__, static_path='/static')


@app.route('/')
def hello():
    return render_template('stations.html')
    #return 'Great, it works!!!'


@app.route('/api/stations', methods=['GET'])
def getStations():
    print 'Retrieving stations...'
    
    radios = [
        {
            "name": "Virgin Radio", 
            "url": "http://icecast.unitedradio.it/Virgin.mp3"
        },
        {
            "name": "RTL 102.5", 
            "url": "http://shoutcast.rtl.it:3010/"
        },
        {
            "name": "Radio Deejay", 
            "url": "http://radiodeejay-lh.akamaihd.net/i/RadioDeejay_Live_1@189857/index_96_a-b.m3u8?sd=10&rebase=on"
        }
        ];
    
    return json.dumps(radios)


@app.route('/api/stations', methods=['POST'])
def addStations():
    return 'Adding stations... (todo)'


if __name__ == '__main__':
    # Run and make server accessible from any
    # computer in the network
    app.run(host='0.0.0.0', port=8080, debug=True)
