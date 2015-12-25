
import openpyxl as px
import json
from pprint import pprint

with open('places_raw.json') as data_file:    
    data = json.load(data_file)

pprint(data)




#json = open("place_generated.json", "w+")
#json.write("[\n\t")
