from carto.print import Printer
import os
import time

CARTO_USER_NAME = os.environ.get('CARTO_USER_NAME')
CARTO_API_KEY = os.environ.get("CARTO_API_KEY", "default_public")
MAP_URL = 'tpl_' + '_'.join(os.environ['CARTO_MAP_URL'].split('-'))
MAP_WIDTH_CM = os.environ.get("MAP_WIDTH_CM", 100)
MAP_HEIGHT_CM = os.environ.get("MAP_HEIGHT_CM", 60)
MAP_ZOOM = os.environ.get("MAP_ZOOM", 11)
MAP_BBOX = os.environ.get("MAP_BBOX", "-73.91754180192949,40.745569339272336,-73.34899932146074,40.84979029075523")
MAP_DPI = os.environ.get("MAP_DPI", 300)
MAP_IMAGE_TYPE = os.environ.get("MAP_IMAGE_TYPE", 'CMYK')



if os.environ.get('CARTO_USER_NAME') is None:
    raise ValueError("You must provide a carto user name for the map owner")

if os.environ.get('CARTO_MAP_URL') is None:
    raise ValueError("You must provide a carto map ID")


print(f"Generating {MAP_DPI} dpi render in {MAP_IMAGE_TYPE} format for map {MAP_URL}")
time.sleep(5)
printer = Printer(CARTO_USER_NAME, MAP_URL, CARTO_API_KEY, MAP_WIDTH_CM, MAP_HEIGHT_CM, MAP_ZOOM, MAP_BBOX, MAP_DPI, MAP_IMAGE_TYPE)
printer.export('/usr/app/output')
