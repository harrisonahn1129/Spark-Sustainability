# This is the function that forms the dictionary of resourceID's with keys that describes which resourceID connects to which dataset.
def getSourceDict():
    source = {
        "CANOPY_CHANGE_ASSESSMENT: 2014-2019 TREE CANOPY CHANGE": "6ff3992b-035a-4d8e-8f2d-f6a99d516571",
        "HYDROGRAPHY_LINE": "6ca65cc3-df65-4f33-8637-89085935d432",
        "HYDROGRAPHY_POLYGON": "aa048a03-ff62-4740-9b1b-ef643a2fdb1a",
        "9INCH_SEA_LEVEL_RISE_1PCT_ANNUAL_FLOOD": "5f99767f-876d-46ba-9d8b-2bcfa39213fe",
        "9INCH_SEA_LEVEL_RISE_10PCT_ANNUAL FLOOD": "5c6b21a3-f7e0-4939-bb8c-f5b6cf2f60a1",
        "21INCH_SEA_LEVEL_RISE_1PCT_ANNUAL_FLOOD": "cb0ad3a1-e7d2-4fa5-b23f-4176a027f836",
        "21INCH_SEA_LEVEL_RISE_10PCT_ANNUAL_FLOOD": "54032fd8-9ae4-4d09-937e-db0938e737e2",
        "36INCH_SEA_LEVEL_RISE_1PCT_ANNUAL_FLOOD": "3620f50d-1f49-4d6d-976b-6ac475a00aa8",
        "36INCH_SEA_LEVEL_RISE_10PCT_ANNUAL_FLOOD": "d8ae2aaa-af13-4443-9e13-80d2ea177846",
    }
    return source

import requests
# import shapefile
import matplotlib.pyplot as plt
import geopandas as gpd

# fromNametoID function takes a string of name of the source as input. It searches the key in the source dictionary that is the same
# as the input. It will return the resourceID of the found key.
def fromNametoID(sourceName):
    ID = getSourceDict()[sourceName]

    return ID

# sourceList function takes no input. It will iterate through the keys in the source dictionary and return the list of keys (strings)
# in the dictionary (names of sources).
def sourceList():
    srcList = []
    dic = getSourceDict()
    for key in dic:
        srcList.append(key)

    return srcList

# Testing with HYDROGRAPHY_LINE to see if we can pull the shapefile dataset
dataname = HYDROGRAPHY_LINE
RID = fromNametoID(dataname)
print(RID)
