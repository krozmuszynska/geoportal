
from sheet_types import *
from typing import Callable
from openpyxl import load_workbook, Workbook
import geojson

# helper method to get cell value as string
def get_str(work_book, work_sheet, col_id, row_id):
    return str(work_book[work_sheet][f'{str(col_id)}{str(row_id)}'].value) if work_book[work_sheet][f'{str(col_id)}{str(row_id)}'].value else ''

# helper method to get cell value
def get_val(work_book, work_sheet, col_id, row_id):
    return work_book[work_sheet][f'{str(col_id)}{str(row_id)}'].value

# helper method to get last row in the sheet
def get_max_row(work_book, work_sheet, column_id):
    return max((a.row for a in work_book[work_sheet][column_id] if a.value is not None))

def get_tile(work_book: Workbook, work_sheet: str, row_num: int) -> Tile:
    return Tile(
        get_str(work_book, work_sheet, 'A', row_num),
        get_str(work_book, work_sheet, 'B', row_num),
        get_str(work_book, work_sheet, 'C', row_num),
        get_val(work_book, work_sheet, 'D', row_num),
        get_val(work_book, work_sheet, 'E', row_num),
        get_val(work_book, work_sheet, 'F', row_num),
        get_str(work_book, work_sheet, 'G', row_num)        
    )

def get_marker(work_book: Workbook, work_sheet: str, row_num: int) -> Marker:
    return Marker(
        get_str(work_book, work_sheet, 'A', row_num),
        get_str(work_book, work_sheet, 'B', row_num),
        get_str(work_book, work_sheet, 'C', row_num),
        get_str(work_book, work_sheet, 'D', row_num),
        get_str(work_book, work_sheet, 'E', row_num),
        get_str(work_book, work_sheet, 'F', row_num),
        get_val(work_book, work_sheet, 'G', row_num),
        get_val(work_book, work_sheet, 'H', row_num),
        get_val(work_book, work_sheet, 'I', row_num),
        get_str(work_book, work_sheet, 'J', row_num),
        get_str(work_book, work_sheet, 'K', row_num),
        get_str(work_book, work_sheet, 'L', row_num),
        get_str(work_book, work_sheet, 'M', row_num),
        get_str(work_book, work_sheet, 'N', row_num),
        get_str(work_book, work_sheet, 'O', row_num),
        get_str(work_book, work_sheet, 'P', row_num),
        get_str(work_book, work_sheet, 'Q', row_num)
    )

def get_wms(work_book: Workbook, work_sheet: str, row_num: int) -> WMS:
    return WMS(
        get_str(work_book, work_sheet, 'A', row_num),
        get_str(work_book, work_sheet, 'B', row_num),
        get_str(work_book, work_sheet, 'C', row_num),
        get_str(work_book, work_sheet, 'D', row_num),
        get_val(work_book, work_sheet, 'E', row_num),
        get_str(work_book, work_sheet, 'F', row_num),
        get_str(work_book, work_sheet, 'G', row_num)     
    )

def get_data(work_book: Workbook, work_sheet: str, row_num: int) -> Geo_data:
    return Geo_data(
        get_str(work_book, work_sheet, 'A', row_num),
        get_val(work_book, work_sheet, 'B', row_num),
        get_val(work_book, work_sheet, 'C', row_num),
        get_str(work_book, work_sheet, 'D', row_num),
        get_str(work_book, work_sheet, 'E', row_num),
        get_str(work_book, work_sheet, 'F', row_num),
        get_str(work_book, work_sheet, 'G', row_num),
        get_str(work_book, work_sheet, 'H', row_num),
        get_str(work_book, work_sheet, 'I', row_num),
        get_str(work_book, work_sheet, 'J', row_num),
        get_str(work_book, work_sheet, 'K', row_num),
        get_str(work_book, work_sheet, 'L', row_num),
        get_str(work_book, work_sheet, 'M', row_num),
        get_str(work_book, work_sheet, 'N', row_num),
        get_str(work_book, work_sheet, 'O', row_num),
        get_str(work_book, work_sheet, 'P', row_num),
        get_str(work_book, work_sheet, 'Q', row_num)
    )

def get_sheet(work_book: Workbook, work_sheet: str, sheet_type_fn: Callable, rtype: str):
    max_row_num = get_max_row(work_book, work_sheet, 'A')
    if rtype == 'list':
        mlist = []
        for r in range(2, max_row_num + 1):
            mlist.append( sheet_type_fn(work_book, work_sheet, r) )
        return mlist
    elif rtype == 'dict':
        mdict = {}
        for r in range(2, max_row_num + 1):
            d = sheet_type_fn(work_book, work_sheet, r)
            mdict.update( {d.id: d} )
        return mdict

def get_geojson(data: Geo_data, md: dict) -> geojson.FeatureCollection:
    ftl = []
    for d in data:
        ftl.append(
            geojson.Feature(
                    geometry=geojson.Point((
                        d.lng,
                        d.lat
                    )),
                    properties={
                        'name': d.name,
                        'address': d.get_adr_str(),
                        'search': d.search_keys,
                        'phone': d.phone,
                        'website': d.website,
                        'email': d.email,
                        'image': d.image_url,
                        'description': d.description,
                        'marker': {
                            'id': d.marker_type,
                            'name': md.get(d.marker_type).name,
                            'icon': md.get(d.marker_type).icon_name,
                            'prefix': md.get(d.marker_type).prefix,
                            'markerColor': md.get(d.marker_type).marker_color,
                            'iconColor': md.get(d.marker_type).icon_color,
                            'spin': md.get(d.marker_type).spin,
                            'zoom_min': md.get(d.marker_type).zoom_min,
                            'zoom_max': md.get(d.marker_type).zoom_max,
                            'extraClasses': md.get(d.marker_type).extra_classes,
                            'iconUrl': md.get(d.marker_type).icon_url,
                            'shadowUrl': md.get(d.marker_type).shadow_url,
                            'iconSize': md.get(d.marker_type).icon_size,
                            'shadowSize': md.get(d.marker_type).shadow_size,
                            'iconAnchor': md.get(d.marker_type).icon_anchor,
                            'shadowAnchor': md.get(d.marker_type).shadow_anchor,
                            'popupAnchor': md.get(d.marker_type).popup_anchor
                        }

                    }
                ) 
        )
    return geojson.FeatureCollection(ftl)