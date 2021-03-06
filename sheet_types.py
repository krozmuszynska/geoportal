# class describes one row in the Types sheet
class Marker:

    def __init__(self, id: str, name: str, icon_name: str, prefix: str, marker_color: str, icon_color: str, spin: int, zoom_min: int, zoom_max: int, extra_classes: str, icon_url: str, shadow_url: str, icon_size: str, shadow_size: str, icon_anchor: str, shadow_anchor: str, popup_anchor: str):
        self.id = id
        self.name = name
        self.icon_name = icon_name
        self.prefix = prefix
        self.marker_color = marker_color
        self.icon_color = icon_color
        self.spin = bool(spin)
        self.zoom_min = zoom_min
        self.zoom_max = zoom_max
        self.extra_classes = extra_classes
        self.icon_url = icon_url
        self.shadow_url = shadow_url
        self.icon_size = icon_size
        self.shadow_size = shadow_size
        self.icon_anchor = icon_anchor
        self.shadow_anchor = shadow_anchor
        self.popup_anchor = popup_anchor

    def __str__(self):
        return f"""
            ({self.id}): {self.name}, {self.prefix}-{self.icon_name}
            {self.marker_color}, {self.icon_color}, {self.spin}, {self.zoom_min}-{self.zoom_max}, {self.extra_classes}
            {self.icon_url}
            {self.shadow_url}
            {self.icon_size}, {self.shadow_size}
            {self.icon_anchor}, {self.shadow_anchor}, {self.popup_anchor}
        """


# class describes one row in the Tiles sheet
class Tile:
    def __init__(self, id, name, url, tile_size, zoom_offset, max_zoom, attribution):
        self.id = id
        self.name = name
        self.url = url
        self.tile_size = tile_size
        self.zoom_offset = zoom_offset
        self.max_zoom = max_zoom
        self.attribution = attribution

    def __str__(self):
        return f"""
            ({self.id}): {self.name}
            {self.url}
            {self.tile_size}, {self.zoom_offset}, {self.max_zoom}
            {self.attribution}
        """


# class describes one row in the WMS sheet
class WMS:
    def __init__(self, id: str, name: str, url: str, layer_name: str, format: str, transparent: int, attribution: str):
        self.id = id
        self.name = name
        self.url = url
        self.layer_name = layer_name
        self.format = format
        self.transparent = bool(transparent)
        self.attribution = attribution

    def __str__(self):
        return f"""
            ({self.id}): {self.name}
            {self.url}
            {self.layer_name}, {self.format}, {self.transparent}
            {self.attribution}
        """


# class describes one row in the Data sheet
class Geo_data:
    def __init__(self, id, lat: float, lng: float, marker_type: Marker, name: str, description: str, search_keys: str, street: str, building_number: str, local_number: str, zip: str, city: str, country: str, phone: str, email: str, website: str, image_url: str):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.marker_type = marker_type
        self.name = name
        self.description = description
        self.search_keys = search_keys
        self.street = street
        self.building_number = building_number
        self.local_number = local_number
        self.zip = zip
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.website = website
        self.image_url = image_url

    # helper method to get POI address as a string
    def get_adr_str(self):
        return f"{self.street} {self.building_number}, {self.zip} {self.city}, {self.country}"

    def __str__(self):
        return f"""
            ({self.id}): [{self.lat}, {self.lng}] {self.name}
            {self.search_keys}: {self.description}
            {self.street} {self.building_number}/{self.local_number}, {self.zip} {self.city}, {self.country}
            {self.telephone}, {self.email}
            {self.web}
            {self.image_url}
        """
