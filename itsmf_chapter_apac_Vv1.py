import folium
from folium import plugins
import base64
import os

def create_itsmf_apac_map():
    """
    Creates a map of APAC region showing ITSMF chapter locations
    """
    
    # Center coordinates for APAC region (roughly centered between all countries)
    center_lat = 15.0
    center_lon = 120.0
    
    # Create the base map centered on APAC region
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=4,
        tiles='OpenStreetMap'
    )
    
    # ITSMF Chapter locations in APAC
    itsmf_chapters = [
        {
            'country': 'India',
            'city': 'Mumbai',
            'lat': 19.0760,
            'lon': 72.8777,
            'chapter': 'ITSMF India',
            'details': 'Major IT Service Management hub in India'
        },
        {
            'country': 'India',
            'city': 'Bangalore',
            'lat': 12.9716,
            'lon': 77.5946,
            'chapter': 'ITSMF India - Bangalore',
            'details': 'Silicon Valley of India'
        },
        {
            'country': 'Malaysia',
            'city': 'Kuala Lumpur',
            'lat': 3.1390,
            'lon': 101.6869,
            'chapter': 'ITSMF Malaysia',
            'details': 'National chapter headquarters'
        },
        {
            'country': 'Thailand',
            'city': 'Bangkok',
            'lat': 13.7563,
            'lon': 100.5018,
            'chapter': 'ITSMF Thailand',
            'details': 'Central hub for SE Asia ITSM activities'
        },
        {
            'country': 'Hong Kong',
            'city': 'Hong Kong',
            'lat': 22.3193,
            'lon': 114.1694,
            'chapter': 'ITSMF Hong Kong',
            'details': 'Financial services ITSM focus'
        },
        {
            'country': 'Australia',
            'city': 'Sydney',
            'lat': -33.8688,
            'lon': 151.2093,
            'chapter': 'ITSMF Australia - Sydney',
            'details': 'Largest ITSMF chapter in APAC'
        },
        {
            'country': 'Australia',
            'city': 'Melbourne',
            'lat': -37.8136,
            'lon': 144.9631,
            'chapter': 'ITSMF Australia - Melbourne',
            'details': 'Strong enterprise ITSM community'
        },
        {
            'country': 'New Zealand',
            'city': 'Auckland',
            'lat': -36.8485,
            'lon': 174.7633,
            'chapter': 'ITSMF New Zealand',
            'details': 'National chapter covering both islands'
        }
    ]
    
    # Color scheme for different countries
    country_colors = {
        'India': 'orange',
        'Malaysia': 'green',
        'Thailand': 'red',
        'Hong Kong': 'purple',
        'Australia': 'blue',
        'New Zealand': 'darkgreen'
    }
    
    # Add markers for each ITSMF chapter
    for chapter in itsmf_chapters:
        popup_content = f"""
        <div style="width: 200px;">
            <h4>{chapter['chapter']}</h4>
            <p><strong>Location:</strong> {chapter['city']}, {chapter['country']}</p>
            <p><strong>Details:</strong> {chapter['details']}</p>
        </div>
        """
        
        folium.Marker(
            [chapter['lat'], chapter['lon']],
            popup=folium.Popup(popup_content, max_width=250),
            tooltip=f"{chapter['chapter']} - {chapter['city']}",
            icon=folium.Icon(
                color=country_colors[chapter['country']], 
                icon='info-sign',
                prefix='fa'
            )
        ).add_to(m)
    
    # Add company logo placeholders
    logo_html = '''
    <div style="position: fixed; 
                top: 10px; left: 10px; width: 240px; height: 80px; 
                background-color: white; border: 2px solid #333;
                z-index:9999; font-size:14px; text-align:center;
                padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
        <strong>ITSMF APAC</strong>
        <br><small>Chapter Locations</small>
    </div>
    '''
    
    # Try to load actual logo if available
    try:
        with open('itsmf-logo.png', 'rb') as f:
            logo_data = base64.b64encode(f.read()).decode()
        
        logo_html = f'''
        <div style="position: fixed; 
                    top: 10px; left: 10px; width: 240px; height: 80px; 
                    z-index:9999; background: white; border: 2px solid #333;
                    border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
            <img src="data:image/png;base64,{logo_data}" 
                 style="width: 100%; height: 100%; object-fit: contain;">
        </div>
        '''
    except FileNotFoundError:
        print("ITSMF logo file not found. Using placeholder.")

    m.get_root().html.add_child(folium.Element(logo_html))
    
    # Create legend showing country color codes
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 300px; height: 200px; 
                background-color: white; border: 2px solid #333; z-index:9999; 
                font-size: 12px; padding: 15px; border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
    <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
        ITSMF APAC Chapters
    </h4>
    <div style="margin: 5px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #ff8c00; margin-right: 8px; border-radius: 50%;"></span>
        <strong>India:</strong> Mumbai, Bangalore
    </div>
    <div style="margin: 5px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #28a745; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Malaysia:</strong> Kuala Lumpur
    </div>
    <div style="margin: 5px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #dc3545; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Thailand:</strong> Bangkok
    </div>
    <div style="margin: 5px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #6f42c1; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Hong Kong:</strong> Hong Kong
    </div>
    <div style="margin: 5px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #007bff; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Australia:</strong> Sydney, Melbourne
    </div>
    <div style="margin: 5px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #006400; margin-right: 8px; border-radius: 50%;"></span>
        <strong>New Zealand:</strong> Auckland
    </div>
    </div>
    '''
    
    m.get_root().html.add_child(folium.Element(legend_html))

    # Create info panel
    info_html = '''
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 350px; height: 200px; 
                background-color: white; border: 2px solid #333; z-index:9999; 
                font-size: 12px; padding: 15px; border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
    <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
        About ITSMF APAC
    </h4>
    <p style="margin: 8px 0; line-height: 1.4;">
        <strong>IT Service Management Forum (ITSMF)</strong> is a global organization 
        promoting best practices in IT Service Management across the Asia-Pacific region.
    </p>
    <p style="margin: 8px 0; line-height: 1.4;">
        These chapters provide local networking, training, and certification opportunities 
        for ITSM professionals.
    </p>
    <div style="font-size: 11px; color: #666; text-align: center; margin-top: 15px;">
        <em>Click on markers for chapter details</em>
    </div>
    </div>
    '''
    
    m.get_root().html.add_child(folium.Element(info_html))
    
    # Add a title to the map
    title_html = '''
    <h2 style="position: absolute; top: 100px; left: 50%; transform: translateX(-50%);
               z-index: 1000; background: rgba(255,255,255,0.9); 
               padding: 15px 30px; border-radius: 10px; margin: 0;
               box-shadow: 0 2px 10px rgba(0,0,0,0.3); color: #333;
               font-family: Arial, sans-serif;">
        ITSMF Asia-Pacific Chapter Locations
    </h2>
    '''
    m.get_root().html.add_child(folium.Element(title_html))
    
    return m

# Generate and save the map
if __name__ == "__main__":
    # Create the map
    itsmf_map = create_itsmf_apac_map()
    
    # Save the map with the requested naming convention
    output_file = "itsmf_apac_chapters.html"
    itsmf_map.save(output_file)
    
    print(f"ITSMF APAC map has been saved as '{output_file}'")
    print("\nMap includes ITSMF chapters in:")
    print("- India (Mumbai, Bangalore)")
    print("- Malaysia (Kuala Lumpur)")
    print("- Thailand (Bangkok)")
    print("- Hong Kong")
    print("- Australia (Sydney, Melbourne)")
    print("- New Zealand (Auckland)")
    print("\nTo customize:")
    print("1. Add 'itsmf-logo.png' file for ITSMF branding")
    print("2. Modify chapter details or add more locations as needed")
    
    # Optional: Open the map in the default browser
    import webbrowser
    import os
    
    # Get the absolute path to the HTML file
    abs_path = os.path.abspath(output_file)
    
    # Open in browser (comment out if you don't want auto-open)
    webbrowser.open(f'file://{abs_path}')