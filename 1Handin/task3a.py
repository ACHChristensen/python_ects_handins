#Opgave 3.a : Vis monumentet som bliver returneret i metoden, på et kort over københavn ved brug af plotting:¨
import task3
import folium

'''Dette viser plotting af et monument på et kort over kbh ved brug af plotting'''
def plotting_by_cooridinates(monument_name = None, monument_id = None):
    map_monument = folium.Map(location=(cooridinates['latitude'], cooridinates['longitude']), zoom_start=14)
    if(monument_name==None or monument_id==None):
        return map_monument
    else:
        cooridinates = task3.cooridinates_of_monument("monumenter.csv", name = monument_name, id = monument_id)
        tooltip = "Click Here For More Info"
        marker = folium.Marker(
            location=[cooridinates['latitude'], cooridinates['longitude']],
            popup="<strong>"+str(monument_name)+"</strong>",
            tooltip=tooltip)
        marker.add_to(map_monument)
        return map_monument
 
if __name__ == '__main__':
    None