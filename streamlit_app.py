import streamlit as st
import folium
from shapely.geometry import Point
import geopandas as gpd
import pandas as pd
import streamlit.components.v1 as components
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def check_state(file_name):
    # Path to the GeoJSON file containing the farm plot boundary
    farm_plot_file = file_name

    # Path to the SHP file containing state boundaries and names
    state_boundary_file = './data/cleaned_state_boundary.shp'

    # Read the farm plot boundary from the GeoJSON file
    farm_plot = gpd.read_file(farm_plot_file)

    # Read the state boundaries and names from the SHP file
    state_boundaries = gpd.read_file(state_boundary_file)
    # Convert the farm plot geometry to the same CRS as the state boundaries
    farm_plot = farm_plot.to_crs(state_boundaries.crs)

    # Iterate over the state boundaries and check if the farm plot is within any state
    for index, state in state_boundaries.iterrows():
        if farm_plot.geometry.within(state.geometry).any():
            state_name = state['STATE']
            st.sidebar.success("The farm plot has been loaded.")
            return(state_name)
            break

def dictionary(file_name, col1, col2, col3, col4, uploaded_long_val, uploaded_lat_val):
    input_file = './data/data.csv'  # Replace with the path to your input CSV file
    word_to_search = check_state(file_name)  # Replace with the word you want to search

    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Filter rows where the last column contains the word
    filtered_df = df[df.iloc[:, -1].str.contains(word_to_search, na=False)].reset_index(drop=True)
    #st.write(filtered_df)
    # Extract the "Kind" column from the filtered DataFrame
    kinds = filtered_df['Kind']
    rec = kinds.unique()[0:1]
    df = pd.DataFrame(rec)
    print(uploaded_long_val)
    print(uploaded_lat_val)
    owm = OWM('4c87f00e27fc340e470f2d34fd1e516f')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_coords(float(uploaded_long_val), float(uploaded_lat_val))
    w = observation.weather

    loc_temp = round(w.temperature('celsius')['temp'],2)
    loc_temp = str(loc_temp)
    loc_wind = round(w.wind('km_hour')['speed'],2)
    loc_wind = str(loc_wind)
    loc_humid = round(w.humidity,2)
    loc_humid = str(loc_humid)
   
    col1.metric(":mostly_sunny: Temperature", loc_temp + " °C", "1.2 °C")
    col2.metric(":tornado: Wind", loc_wind + " km/hr", "-8%")
    col3.metric(":droplet: Humidity", loc_humid + " %", "4%")

    col4.caption(":green[**:ear_of_rice: Recommended crop**]")
    for index, row in df.iterrows():
        col4.write(f"**{row[0]}**") 


    expander = col4.expander("Variety/Hybrid Name")
    expander.write("""Swarna Shusk Dhan (RCPR 56-IR93827-29-1-1-4) (IET 27962)""")

def main():

    st.set_page_config(layout="wide")  # Set the app layout to wide
    st.title(":seedling: What crop should you plant?")
    #st.caption("Crop recommendation app by Dinesh")
    css = '''
    <style>
    #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
    section.main > div:has(~ footer ) {
        padding-bottom: 5px;
        padding-top: 10x;
    
    }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)

    if "load_state" not in st.session_state:
        st.session_state.load_state = False

    loading_animation_placeholder = st.empty()

    # Create a Folium map with desired size
    tile_url = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    url = "C:/Users/Dinesh.Sreekanthan/PycharmProjects/gis_map/geospatial-data-using-python/data/vector_farm.geojson"
    
    folium_map = folium.Map(location=[12.9826273, 80.2652262], zoom_start=14, width=1000, height=350, tiles=tile_url, attr='Tiles &copy; Esri', control_scale=True)
    
    # Define the different tile layers
    tile_layers = {
        "World Imagery": tile_url,
        "OpenStreetMap": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    }
    
    col1, col2, col3, col4 = st.columns(4)
    col1.empty()

    # Get the radio button selection from the user
    tile_selection = st.sidebar.radio("Map Tiles", list(tile_layers.keys()))
    
    # Update the tile layer based on the selection
    if tile_selection in tile_layers:        
        selected_tile_url = tile_layers[tile_selection]
        folium.TileLayer(selected_tile_url, attr=tile_selection).add_to(folium_map)
    
    w = st.sidebar.file_uploader("Upload a CSV file", type="geojson")

    add_geojson_button = st.sidebar.button("Load Farm GeoJSON")
    
    if add_geojson_button:
        st.session_state.load_state = True
        
        if (w):
            df = gpd.read_file(w.name)

            #Find the center point
            df['Center_point'] = df['geometry'].centroid
            #Extract lat and lon from the centerpoint
            df["lat"] = df.Center_point.map(lambda p: p.x)
            df["long"] = df.Center_point.map(lambda p: p.y)
            uploaded_lat_val = (df["lat"][0])
            uploaded_long_val = (df["long"][0])

            #st.write(uploaded_lat_val)
            #st.write(uploaded_long_val)

            folium_map = folium.Map(location=[uploaded_long_val, uploaded_lat_val], zoom_start=17, width=1000, height=350, tiles=tile_url, attr='Tiles &copy; Esri', control_scale=True)
            folium.GeoJson(
                data=w.name, 
                style_function=lambda feature: {'color': 'white'}
            ).add_to(folium_map)
            dictionary(w.name, col1, col2, col3, col4, uploaded_long_val, uploaded_lat_val)
        else: st.sidebar.error("No GeoJSON file selected")


    # Generate the HTML for the map
    folium_map_html = folium_map.get_root().render()
    
    # Modify the HTML to set the map width to 100%
    modified_html = folium_map_html.replace('<div class="folium-map"', '<div class="folium-map" style="width: 100%;"')

    # Display the modified map HTML using st.components.v1.html
    st.components.v1.html(modified_html, width=1000, height=350, scrolling=False)

if __name__ == "__main__":
    main()