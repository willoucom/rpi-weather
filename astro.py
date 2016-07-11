#!/usr/bin/env python
#===============================================================================
# astro.py
#
# 2016-07-10
# Wilfried JEANNIARD
#===============================================================================
import time
import httplib
import sys
from xml.dom.minidom import parseString
from sense_hat import SenseHat
from astrotools import AstroTools

from astro8x8icons import LED8x8ICONS

icons = ['SUNNY','RAIN','CLOUD','SHOWERS','SNOW','STORM']

ZIPCODE     = 98109
NUM_DAYS    = 1
NOAA_URL    = "graphical.weather.gov"
REQ_BASE    = r"/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?"
TIME_FORMAT = "12+hourly"

tools = AstroTools()


sense = SenseHat()
sense.clear()
sense.low_light = True
sense.set_rotation(90)
time.sleep(2)

def giveup():
    """Action to take if anything bad happens."""
    sense.show_message("Error occured.")
    sense.set_pixels(LED8x8ICONS['UNKNOWN'])
    print "Error occured."
    sys.exit(1)

def validate_zip(zip_arg):
    """Return integer conversion of supplied string if valid, global default ZIPCODE otherwise."""
    try:
        zip = int(zip_arg)
        if zip < 99999 and zip > 0:
            return zip
    except ValueError:
        pass
    return ZIPCODE

def get_offset():
    """ Returns 0 if local time after 6AM and before 6PM, 1 otherwise."""
    hour = time.localtime().tm_hour
    if hour > 6 and hour < 18:
        return 0
    else:
        return 1

def make_noaa_request():
    """Make request to NOAA REST server and return data."""
    REQUEST = REQ_BASE + "zipCodeList={0:05d}&".format(ZIPCODE)+\
                        "format={0}&".format(TIME_FORMAT)+\
                        "numDays={0}".format(NUM_DAYS)
    try:
        conn = httplib.HTTPConnection(NOAA_URL)
        conn.request("GET", REQUEST)
        resp = conn.getresponse()
        data = resp.read()
    except:
        giveup()
    else:
        return data

def get_noaa_forecast():
    """Return a string of forecast results."""
    vals = parseString(make_noaa_request()) \
            .getElementsByTagName("weather-conditions")

    if len(vals) < 2*NUM_DAYS:
        print "Request-Result Mismatch: REQ=%d RES=%d" % (NUM_DAYS,len(vals))
        giveup()

    if '12' in TIME_FORMAT:
        offset = get_offset()
    else:
        offset = 0

    forecast = [e.getAttribute("weather-summary") for e in vals[offset::2]]

    return forecast

def print_forecast(forecast=None):
    """Print forecast to screen."""
    if forecast == None:
        return
    print '-'*20
    print time.strftime('%Y/%m/%d %H:%M:%S')
    print "ZIPCODE {0}".format(ZIPCODE)
    print '-'*20
    for daily in forecast:
        print daily

def display_forecast(forecast=None):
    """Display forecast as icons on LED 8x8 matrices."""
    if forecast == None:
        return
    else:
        # sense.show_letter('?')
        # sense.set_pixels(LED8x8ICONS['UNKNOWN'])
        sense.clear()
        for icon in icons:
            if icon in forecast[0].encode('ascii','ignore').upper():
                # icon = "SHOWERS"
                time.sleep(2)
                # tools.transition("DOWN",25,25,50,0.96)
                sense.set_pixels(LED8x8ICONS[icon])

#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ZIPCODE = validate_zip(sys.argv[1])
    forecast = get_noaa_forecast()
    print_forecast(forecast)
    display_forecast(forecast)

    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
