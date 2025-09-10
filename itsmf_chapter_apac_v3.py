import folium
from folium import plugins
import base64
import os
from datetime import datetime

# Define itsmf_chapters globally
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
        'website': 'https://www.linkedin.com/company/itsmf-thailand-chapter/'
    },
    {
        'country': 'Hong Kong',
        'city': 'Hong Kong',
        'lat': 22.3193,
        'lon': 114.1694,
        'chapter': 'ITSMF Hong Kong',
        'details': 'Financial services ITSM focus',
        'website': 'http://www.itsmf.org.hk/eng/'
    },
    {
        'country': 'Australia',
        'city': 'Melbourne',
        'lat': -37.8136,
        'lon': 144.9631,
        'chapter': 'ITSMF Australia',
        'details': 'Strong enterprise ITSM community',
        'website': 'https://itsmfaus.site-ym.com/'
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

# Define event data structure
itsmf_events = [
    {
        'country': 'Thailand',
        'date': '09 October 2025',
        'title': 'Webinar: ITSMF Thailand / ITSM and Business Continuity',
        'link': 'https://www.linkedin.com/events/7368878092259426305'
    },
    {
        'country': 'Australia',
        'date': 'Thursday, 11 September 2025',
        'title': 'National Monthly Event - 11th Sept 2025 - SIAM Bodies of Knowledge',
        'link': 'https://itsmfaus.site-ym.com/events/EventDetails.aspx?id=1982781'
    },
    {
        'country': 'Australia',
        'date': 'Thursday, 25 September 2025',
        'title': 'ACT F2F Event - 25th Sept 2025 - AI-Driven ITSM: Live Demo. Real-Use Cases. Real Outcomes.',
        'link': 'https://itsmfaus.site-ym.com/events/EventDetails.aspx?id=1983729'
    }
]

def parse_date(date_str):
    """Parse date string into datetime object for sorting."""
    # Remove day name if present (e.g., 'Thursday, ')
    date_str = ' '.join(date_str.split(',')[1:]).strip() if ',' in date_str else date_str
    return datetime.strptime(date_str, '%d %B %Y')

def create_itsmf_apac_map():
    """
    Creates a map of APAC region showing ITSMF chapter locations
    """

    # Sort events by date
    itsmf_events_sorted = sorted(itsmf_events, key=lambda e: parse_date(e['date']))

    # Center coordinates for APAC region
    center_lat = 15.0
    center_lon = 120.0

    # Create the base map
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=3,
        tiles='OpenStreetMap'
    )

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

    # Dynamically generate legend HTML using itsmf_chapters data
    legend_items = []
    for chapter in itsmf_chapters:
        color = country_colors[chapter['country']]
        legend_items.append(
            f'''
            <div style="margin: 5px 0;">
                <span style="display: inline-block; width: 16px; height: 16px;
                             background-color: {color}; margin-right: 8px; border-radius: 50%; vertical-align: middle;"></span>
                <strong>{chapter['country']}:</strong> {chapter['city']} -
                <a href="{chapter['website']}" target="_blank">{chapter['website']}</a>
            </div>
            '''
        )

    # Generate event list HTML (sorted by date)
    event_items = []
    for event in itsmf_events_sorted:
        color = country_colors[event['country']]
        event_items.append(
            f'''
            <div style="margin: 8px 0; padding: 5px; border-left: 3px solid {color}; background-color: #f9f9f9; border-radius: 0 3px 3px 0;">
                <div style="font-weight: bold; color: {color};">{event['country']}</div>
                <div style="font-size: 12px; margin: 2px 0;">
                    <strong>{event['date']}</strong><br>
                    {event['title']}<br>
                    <a href="{event['link']}" target="_blank" style="color: #0066cc; font-size: 11px;">More info</a>
                </div>
            </div>
            '''
        )

    legend_html = f'''
    <div style="position: fixed;
                top: 20px; right: 20px; width: 450px; height: auto;
                background-color: white; border: 2px solid #333; z-index:9999;
                font-size: 13px; padding: 15px; border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);">

        <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
            ITSMF APAC Chapters
        </h4>
        {''.join(legend_items)}

        <hr style="border-top: 1px solid #ccc; margin: 15px 0;">

        <h4 style="margin-top: 0; color: #333; text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 5px;">
            Upcoming Events 🗓️
        </h4>

        <div style="max-height: 300px; overflow-y: auto; margin-top: 10px;">
            {''.join(event_items)}
        </div>
    </div>
    '''

    m.get_root().html.add_child(folium.Element(legend_html))

    # Create info panel
    info_html = '''
    <div style="position: fixed;
                top: 200px; left: 20px; width: 350px; height: 200px;
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

    # Save the map
    output_file = "itsmf_apac_chapters.html"
    itsmf_map.save(output_file)

    print(f"ITSMF APAC map has been saved as '{output_file}'")
    print("\nMap includes ITSMF chapters in:")
    for chapter in itsmf_chapters:
        print(f"- {chapter['country']} ({chapter['city']})")

    print("\nEach chapter includes website links in the marker popups and legend")
    print("\nTo customize:")
    print("1. Add 'itsmf-logo.png' file for ITSMF branding")
    print("2. Modify chapter details or add more locations as needed")

    # Optional: Open the map in the default browser
    import webbrowser
    abs_path = os.path.abspath(output_file)
    webbrowser.open(f'file://{abs_path}')
