import argparse
from openpyxl import load_workbook
import geojson
from jinja2 import Template
import pprint
from helper import *
from sheet_types import *
from pathlib import Path

# Construct the argument parser
# ap = argparse.ArgumentParser()
# Add the arguments to the parser
# ap.add_argument("-i", type=str, dest='input', required=True, help="input file with addresses to process")
# ap.add_argument("-o", type=str, dest='output', default='out.json', required=False, help="output name for geoJSON")
# args = ap.parse_args()
# INPUT_FILE = args.input
# OUTPUT_FILE = args.output

INPUT_FILE = 'data.xlsx'
OUTPUT_FILE = 'index.html'
DATA_FILE = 'geojson.js'
EXPORT_DIR = 'geoportal'
PAGE_TITLE = 'Geoportal z danymi informacyjne o regionalnych dyrekcjach lasów państwowych i nadleśnictwach'
AUTHOR = 'Kinga Rozmuszyńska &copy; 2020'

def main():
    # load workbook
    work_book = load_workbook(filename=INPUT_FILE)
    print(f'Reading file {INPUT_FILE}...')

    tile_list = get_sheet(work_book, 'tiles', get_tile, 'list')
    wms_list = get_sheet(work_book, 'wms', get_wms, 'list')
    marker_dict = get_sheet(work_book, 'markers', get_marker, 'dict')
    data_list = get_sheet(work_book, 'data', get_data, 'list')

    fc = get_geojson(data_list, marker_dict)
    dump = geojson.dumps(fc, indent=4, sort_keys=True, ensure_ascii=False,)

    Path(EXPORT_DIR).mkdir(parents=True, exist_ok=True)

    print(f"Export geoportal data file to {EXPORT_DIR}/{DATA_FILE}")
    with open(f"{EXPORT_DIR}/{DATA_FILE}", 'w', encoding='utf-8') as f:
        f.write('var jsonData = ')
        f.write(dump)

    with open('index.html.jinja') as f:
        tmpl = Template(f.read())

    marker_type_list = []
    for d in data_list:
        marker_type_list.append(d.marker_type)
    unique_marker_list = list(set(marker_type_list))
    res = tmpl.render(wms_list=wms_list, tile_list=tile_list, marker_dict=marker_dict, unique_marker_list=unique_marker_list, data_file=DATA_FILE, page_title=PAGE_TITLE, author=AUTHOR)

    print(f"Export geoportal webpage to {EXPORT_DIR}/{OUTPUT_FILE}")
    with open(f"{EXPORT_DIR}/{OUTPUT_FILE}", 'w', encoding='utf-8') as f:
        f.write(res)

    print(f"Geoportal is ready to use, please open {EXPORT_DIR}/{OUTPUT_FILE} to see how it looks like")

if __name__ == "__main__":
    main()