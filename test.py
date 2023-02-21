import geopandas as gpd

gdb = './EJSCREEN_2021_USPR_Tracts.gdb'

fc = gpd.read_file(gdb)

# Write to CSV 
fc.to_csv('./USPR_TRACTS_out_csv.csv')

# Write to GeoJSON
#fc.to_file('./out_geojson.geojson', driver='GeoJSON')