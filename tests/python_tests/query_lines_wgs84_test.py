#!/usr/bin/env python

from nose.tools import *
from utilities import execution_path, run_all
import os, mapnik

print mapnik

def setup():
    # All of the paths used are relative, if we run the tests
    # from another directory we need to chdir()
    os.chdir(execution_path('.'))

if 'shape' in mapnik.DatasourceCache.plugin_names():
    def test_lines_layer():
        srs = '+init=epsg:4326'
        lyr = mapnik.Layer('test')
        ds = mapnik.Shapefile(file='../data/shp/bus/bus_wgs84.shp')
        lyr.datasource = ds
        lyr.srs = srs
        # REQUEST=GetFeatureInfo
        # layers=bus_linies
        minx = 2.8278381
        miny = 41.9718469
        maxx = 2.8285673
        maxy = 41.9723039
        
        _width = 1090
        _height = 429
        _map = mapnik.Map(_width, _height, srs)
        _map.layers.append(lyr)
        # zoom determines tolerance
#        _map.zoom_all()
#        _map_env = _map.envelope()
        env = mapnik.Envelope(minx, miny, maxx, maxy)
#        env.minx = minx
#        env.miny = miny
#        env.maxx = maxx
#        env.maxy = maxy
        _map.zoom_to_box(env)

        _x = 565
        _y = 235

        x = minx + (maxx - minx) * _x / _width
        y = miny + (maxy - miny) * _y / _height

        print minx, miny, maxx, maxy
        print x, y   

        features = _map.query_point(0,x,y).features
        for f in features:
            print f

if __name__ == "__main__":
    setup()
    run_all(eval(x) for x in dir() if x.startswith("test_"))
