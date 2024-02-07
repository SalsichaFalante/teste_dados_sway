import folium
import geopandas as gpd

# Carregar os shapefiles usando GeoPandas
data1 = gpd.read_file(r'SHP/BH Rio Corumbá.shp')
data2 = gpd.read_file(r'SHP/BH Rio Descoberto.shp')
data3 = gpd.read_file(r'SHP/BH Rio Maranhão.shp')
data4 = gpd.read_file(r'SHP/BH Rio Paranoá.shp')
data5 = gpd.read_file(r'SHP/BH Rio Preto.shp')
data6 = gpd.read_file(r'SHP/BH Rio São Marcos.shp')
data7 = gpd.read_file(r'SHP/BH São Bartolomeu.shp')
data_len = gpd.read_file(r'SHP/Lentico.shp')
data_lot = gpd.read_file(r'SHP/Lotico.shp')
data_lagos = gpd.read_file(r'SHP/LAGO.shp')
data_rios = gpd.read_file(r'SHP/Rios_Mapa_chuvas.shp')

#Enquadramento do mapa
max_lon, min_lon = -45.0000, -50.0000
max_lat, min_lat = -13.0000, -18.0000

# Criar um mapa Folium
m = folium.Map(location=[data1.geometry.centroid.y.mean(),
                        data1.geometry.centroid.x.mean()],
                        zoom_start=10,
                        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr='Esri',
                        zoom_control=False,
                        control_scale=True,
                        max_bounds=True,
                        min_lat=min_lat,
                        max_lat=max_lat,
                        min_lon=min_lon,
                        max_lon=max_lon,
                        )

# Grupos
G1 = folium.FeatureGroup('Lentico').add_to(m)
G2 = folium.FeatureGroup('Lotico').add_to(m)
G3 = folium.FeatureGroup('Bacias').add_to(m)

# Personaliza um estilo padrão
default_style = {
        'color': 'lightblue',
        'fillColor': 'lightblue',
        'fillOpacity': 0, 
    }

def style_function_len(feature):
    props = feature.get('properties')
    markup = f"""
        <a href="{props.get('url')}">
            <div style="font-size: 0.8em;">
            <div style="width: 10px;
                        height: 10px;
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: orange;">
            </div>
            {props.get('name')}
        </div>
        </a>
    """
    return {"html": markup}


def style_function_lot(feature):
    props = feature.get('properties')
    markup = f"""
        <a href="{props.get('url')}">
            <div style="font-size: 0.8em;">
            <div style="width: 10px;
                        height: 10px;
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: blue;">
            </div>
            {props.get('name')}
        </div>
        </a>
    """
    return {"html": markup}

# Adicionar os polígonos do shapefile ao mapa
for idx, row in data1.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)
for idx, row in data2.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)
for idx, row in data3.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)
for idx, row in data4.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)
for idx, row in data5.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)
for idx, row in data6.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)
for idx, row in data7.iterrows():
    geo_json = row.geometry.__geo_interface__
    folium.GeoJson(geo_json, style_function=lambda x: default_style).add_to(G3)

'''
for idx, row in data_len.iterrows():
    folium.Marker(
            [row.geometry.y, row.geometry.x],
            icon=folium.Icon(color='orange'), 
            popup = '<strong>ESTACAO: {Name}</strong><br>Clorofila: {Clorofila}<br>Temperatura da Amostra: {t_Amostra}<br>Turbidez: {turbidez}<br>DBO: {dbo}<br>NH4: {NH4}<br>NT: {NT}<br>Oxigênio Dissolvido: {od}<br>PH: {PH}<br>PT: {PT}<br>ST: {st}<br>Coliformes: {Coliformes}'.format(**row)
            ).add_to(G1)
'''

for idx, row in data_len.iterrows():
    content = f"""
        <div style="font-size: 1.2em;">
            <strong>ESTACAO: {row['Name']}</strong><br>
            <br>
            <strong>Clorofila:</strong> {row['Clorofila']}<br>
            <strong>Temperatura da Amostra:</strong> {row['t_Amostra']}<br>
            <strong>Turbidez:</strong> {row['turbidez']}<br>
            <strong>DBO:</strong> {row['dbo']}<br>
            <strong>NH4:</strong> {row['NH4']}<br>
            <strong>NT:</strong> {row['NT']}<br>
            <strong>Oxigênio Dissolvido:</strong> {row['od']}<br>
            <strong>PH:</strong> {row['PH']}<br>
            <strong>PT:</strong> {row['PT']}<br>
            <strong>ST:</strong> {row['st']}<br>
            <strong>Coliformes:</strong> {row['Coliformes']}
        </div>
    """
    folium.Marker(
        [row.geometry.y, row.geometry.x],
        icon=folium.Icon(color='orange', icon='tint', prefix='fa'),
        popup=folium.Popup(content, max_width=300)
    ).add_to(G1)



for idx, row in data_lot.iterrows():
    folium.Marker(
            [row.geometry.y, row.geometry.x],
            icon=folium.Icon(color='blue', icon='tint', prefix='fa'), popup = "<strong>ESTACAO: {row['ESTACAO']</strong><br>}Codigo: {row['CodEstacao']}<br>Bacia: {row['BACIA']}<br>Unidade Hidrografica: {row['UH']}"
        ).add_to(G2)


#m.save("MAPA.html")
m.save('MAPA.html')

# Texto para as estações de monitoramento
#"<strong>ESTACAO: {row['ESTACAO']</strong><br>}Codigo: {row['CodEstacao']}<br>Bacia: {row['BACIA']}<br>Unidade Hidrografica: {row['UH']}"