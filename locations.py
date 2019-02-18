import folium
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderServiceError
from geopy.geocoders import Bing

def get_locations(f):
    manloc = {}
    for user in f["users"]:
        if user["location"] == "":
            pass
        elif not user["location"] in manloc:
            manloc[user["location"]] = str(user["name"]) + "||"
        else:
            manloc[user["location"]] += str(user["name"]) + "||"
    return manloc

def map_add(locations, map):
    geolocator = Bing(api_key="Ag0zrFeOxLpmBE5EdTPEQp2laoQ8HoaXLEHObPUMdWhm1RF_QbCG5v64zk1eGJft ")

    try:
        a = 0
        for i in locations:
            location = geolocator.geocode(i)
            map.add_child(folium.Marker(location=[location.latitude + a, location.longitude + a],
                          popup=str(locations[i]),
                          icon=folium.Icon(color="black", icon_color="white", icon= "cloud")))
            a += 0.0001
    except IndexError as error:
        pass
    except AttributeError as error:
        pass
    except GeocoderTimedOut as error:
        pass
    except GeocoderServiceError as error:
        pass

def map(js):
    map = folium.Map()
    locations = get_locations(js)
    map_add(locations, map)
    map.save('templates/Map.html')

if __name__ == "__main__":
    pass