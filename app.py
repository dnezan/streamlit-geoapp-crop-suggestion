import streamlit as st
import folium
import time
import geopandas as gpd
import pandas as pd

def dictionary():
    input_file = './data/data.csv'  # Replace with the path to your input CSV file
    word_to_search = 'Tamil Nadu'  # Replace with the word you want to search

    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Filter rows where the last column contains the word
    filtered_df = df[df.iloc[:, -1].str.contains(word_to_search, na=False)].reset_index(drop=True)
    #st.write(filtered_df)
    # Extract the "Kind" column from the filtered DataFrame
    kinds = filtered_df['Kind']
    rec = kinds.unique()[0:5]
    df = pd.DataFrame(rec)
    #df = df.drop(df.columns[0], axis=1)


    # Display the resulting DataFrame
    #st.sidebar.dataframe(df, use_container_width=True)
    st.sidebar.subheader("Recommended crop :ear_of_rice:")
    for index, row in df.iterrows():
        #st.sidebar.write(f"Row {index + 1}")
        st.sidebar.write(f"{row[0]}")

    #st.sidebar.write()


def main():


    st.set_page_config(layout="wide")  # Set the app layout to wide
    st.title(":seedling: Crop Recommendation App")
    css = '''
    <style>
    section.main > div:has(~ footer ) {
        padding-bottom: 5px;
        padding-top: 10x;
    
    }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)

    if "load_state" not in st.session_state:
        st.session_state.load_state = False

    # Create a Folium map with desired size
    tile_url = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    url = "C:/Users/Dinesh.Sreekanthan/PycharmProjects/gis_map/geospatial-data-using-python/data/vector_farm.geojson"
    
    folium_map = folium.Map(location=[12.9826273, 80.2652262], zoom_start=14, width=1000, height=500, tiles=tile_url, attr='Tiles &copy; Esri', control_scale=True)
    
    # Define the different tile layers
    tile_layers = {
        "World Imagery": tile_url,
        "OpenStreetMap": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    }
    
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

            folium_map = folium.Map(location=[uploaded_long_val, uploaded_lat_val], zoom_start=30, width=1000, height=500, tiles=tile_url, attr='Tiles &copy; Esri', control_scale=True)
            folium.GeoJson(
                data=w.name, 
                style_function=lambda feature: {'color': 'white'}
            ).add_to(folium_map)
            dictionary()
        else: st.sidebar.error("No GeoJSON file selected")


    # Generate the HTML for the map
    folium_map_html = folium_map.get_root().render()
    
    # Modify the HTML to set the map width to 100%
    modified_html = folium_map_html.replace('<div class="folium-map"', '<div class="folium-map" style="width: 100%;"')

    # Display the modified map HTML using st.components.v1.html
    st.components.v1.html(modified_html, width=1000, height=500, scrolling=False)


if __name__ == "__main__":
    main()
