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
        zoom_start=3,
        tiles='OpenStreetMap'
    )
    
    # ITSMF Chapter locations in APAC
    itsmf_chapters = [
        {
            'country': 'India',
            'city': 'Bangalore',
            'lat': 12.9716,
            'lon': 77.5946,
            'chapter': 'ITSMF India',
            'details': 'Silicon Valley of India',
            'website': 'https://itsmfindiachapter.com/'
        },
        {
            'country': 'Malaysia',
            'city': 'Kuala Lumpur',
            'lat': 3.1390,
            'lon': 101.6869,
            'chapter': 'ITSMF Malaysia',
            'details': 'National chapter headquarters',
            'website': 'https://itsmf.org.my/'
        },
        {
            'country': 'Thailand',
            'city': 'Bangkok',
            'lat': 13.7563,
            'lon': 100.5018,
            'chapter': 'ITSMF Thailand',
            'details': 'Central hub for SE Asia ITSM activities',
            'website': 'https://www.itsmf.or.th'
        },
        {
            'country': 'Hong Kong',
            'city': 'Hong Kong',
            'lat': 22.3193,
            'lon': 114.1694,
            'chapter': 'ITSMF Hong Kong',
            'details': 'Financial services ITSM focus',
            'website': 'http://www.itsmf.org.hk/eng/default.asp'
        },
        {
            'country': 'Australia',
            'city': 'Melbourne',
            'lat': -37.8136,
            'lon': 144.9631,
            'chapter': 'ITSMF Australia',
            'details': 'Strong enterprise ITSM community',
            'website': 'https://www.itsmf.com.au'
        },
        {
            'country': 'New Zealand',
            'city': 'Auckland',
            'lat': -36.8485,
            'lon': 174.7633,
            'chapter': 'ITSMF New Zealand',
            'details': 'National chapter covering both islands',
            'website': 'http://itsmf.org.nz/'
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
        <div style="width: 250px;">
            <h4>{chapter['chapter']}</h4>
            <p><strong>Location:</strong> {chapter['city']}, {chapter['country']}</p>
            <p><strong>Details:</strong> {chapter['details']}</p>
            <p><strong>Website:</strong> <a href="{chapter['website']}" target="_blank">{chapter['website']}</a></p>
        </div>
        """
        
        folium.Marker(
            [chapter['lat'], chapter['lon']],
            popup=folium.Popup(popup_content, max_width=280),
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

    # m.get_root().html.add_child(folium.Element(logo_html))
    
    # Create legend showing country color codes with website URLs
    legend_html = '''
    <div style="position: fixed; 
                top: 100px; left: 20px; width: 350px; height: 230px; 
                background-color: white; border: 2px solid #333; z-index:9999; 
                font-size: 11px; padding: 15px; border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
    <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
        ITSMF APAC Chapters
    </h4>
    <div style="margin: 4px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #ff8c00; margin-right: 8px; border-radius: 50%;"></span>
        <strong>India:</strong> Bangalore - <a href="https://itsmfindiachapter.com/" target="_blank">https://itsmfindiachapter.com/</a>
    </div>
    <div style="margin: 4px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #28a745; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Malaysia:</strong> Kuala Lumpur - <a href="https://www.itsmf.my" target="_blank">www.itsmf.my</a>
    </div>
    <div style="margin: 4px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #dc3545; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Thailand:</strong> Bangkok - <a href="https://www.itsmf.or.th" target="_blank">www.itsmf.or.th</a>
    </div>
    <div style="margin: 4px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #6f42c1; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Hong Kong:</strong> Hong Kong - <a href="https://www.itsmf.hk" target="_blank">www.itsmf.hk</a>
    </div>
    <div style="margin: 4px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #007bff; margin-right: 8px; border-radius: 50%;"></span>
        <strong>Australia:</strong> Melbourne - <a href="https://www.itsmf.com.au" target="_blank">www.itsmf.com.au</a>
    </div>
    <div style="margin: 4px 0;">
        <span style="display: inline-block; width: 15px; height: 15px; 
                     background-color: #006400; margin-right: 8px; border-radius: 50%;"></span>
        <strong>New Zealand:</strong> Auckland - <a href="https://www.itsmf.co.nz" target="_blank">www.itsmf.co.nz</a>
    </div>
    </div>
    '''
    
    m.get_root().html.add_child(folium.Element(legend_html))

## begin
# Create a legend showing country color codes, website URLs, and an event calendar
    legend_html = '''
    <div style="position: fixed; 
                top: 50px; right: 20px; width: 380px; height: auto; 
                background-color: white; border: 2px solid #333; z-index:9999; 
                font-size: 13px; padding: 15px; border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
        
        <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
            ITSMF APAC Chapters
        </h4>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #ff8c00; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
            <strong>India:</strong> Bangalore
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #28a745; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
            <strong>Malaysia:</strong> Kuala Lumpur
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #dc3545; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
            <strong>Thailand:</strong> Bangkok
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #6f42c1; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
            <strong>Hong Kong:</strong> Hong Kong
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #007bff; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
            <strong>Australia:</strong> Melbourne
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 16px; height: 16px; background-color: #006400; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
            <strong>New Zealand:</strong> Auckland
        </div>

        <hr style="border-top: 1px solid #ccc; margin: 15px 0;">

        <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
            Event Calendar 🗓️
        </h4>
        
        <div style="display: flex; justify-content: space-around;">
            <div style="width: 48%;">
                <p style="text-align: center; font-weight: bold; margin-bottom: 5px;"><u>September 2025</u></p>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #ff8c00; border-radius: 50%; margin-right: 5px;"></span>India: 12th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #28a745; border-radius: 50%; margin-right: 5px;"></span>Malaysia: 18th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #dc3545; border-radius: 50%; margin-right: 5px;"></span>Thailand: 19th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #6f42c1; border-radius: 50%; margin-right: 5px;"></span>Hong Kong: 25th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #007bff; border-radius: 50%; margin-right: 5px;"></span>Australia: 26th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #006400; border-radius: 50%; margin-right: 5px;"></span>New Zealand: 27th</div>
            </div>
            
            <div style="width: 48%;">
                <p style="text-align: center; font-weight: bold; margin-bottom: 5px;"><u>October 2025</u></p>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #ff8c00; border-radius: 50%; margin-right: 5px;"></span>India: 10th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #28a745; border-radius: 50%; margin-right: 5px;"></span>Malaysia: 16th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #dc3545; border-radius: 50%; margin-right: 5px;"></span>Thailand: 17th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #6f42c1; border-radius: 50%; margin-right: 5px;"></span>Hong Kong: 23rd</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #007bff; border-radius: 50%; margin-right: 5px;"></span>Australia: 24th</div>
                <div style="margin: 5px 0;"><span style="display: inline-block; width: 12px; height: 12px; background-color: #006400; border-radius: 50%; margin-right: 5px;"></span>New Zealand: 25th</div>
            </div>
        </div>
    </div>
    '''

    m.get_root().html.add_child(folium.Element(legend_html))

## end

    # Create info panel
    info_html = '''
    <div style="position: fixed; 
                bottom: 100px; left: 20px; width: 350px; height: 200px; 
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
        <em>Click on markers for chapter details and website links</em>
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
    print("- India (Bangalore)")
    print("- Malaysia (Kuala Lumpur)")
    print("- Thailand (Bangkok)")
    print("- Hong Kong")
    print("- Australia (Melbourne)")
    print("- New Zealand (Auckland)")
    print("\nEach chapter includes website links in the marker popups and legend")
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