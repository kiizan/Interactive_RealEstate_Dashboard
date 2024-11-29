import streamlit as st
import pandas as pd
from datetime import datetime
from database import setup_database
from queries import get_cities, get_equipment, get_filtered_ads
import altair as alt
import plotly.express as px

def main():
    st.title("Real Estate Advertisement Filter")

    # Database setup
    Session = setup_database()
    session = Session()

    # Filters
    st.sidebar.header("Filter Options")

    # City filter
    cities = get_cities(session)
    city = st.sidebar.selectbox("Select City", options=[""] + cities)

    # Price filter
    price_min = st.sidebar.number_input("Min Price", min_value=0, value=1000)
    price_max = st.sidebar.number_input("Max Price", min_value=0, value=1000000000)

    # Rooms filter
    rooms_min = st.sidebar.number_input("Min Rooms", min_value=1, value=1)
    rooms_max = st.sidebar.number_input("Max Rooms", min_value=1, value=5)

    # Bathrooms filter
    bathrooms_min = st.sidebar.number_input("Min Bathrooms", min_value=1, value=1)
    bathrooms_max = st.sidebar.number_input("Max Bathrooms", min_value=1, value=5)

    # Equipment filter
    equipment_list = get_equipment(session)
    equipment = st.sidebar.multiselect("Select Equipment", options=equipment_list)

    # Date range filter
    start_date = st.sidebar.date_input("Start Date", value=datetime(2024, 1, 1))
    end_date = st.sidebar.date_input("End Date", value=datetime.today())

    # Apply filters and get filtered advertisements
    filtered_ads = get_filtered_ads(
        session,
        price_min,
        price_max,
        rooms_min,
        rooms_max,
        bathrooms_min,
        bathrooms_max,
        city if city != "All" else None,
        equipment,
        start_date,
        end_date
    )

    # Display filtered results
    if filtered_ads:
        st.write(f"Found {len(filtered_ads)} results:")
        ads_df = pd.DataFrame(filtered_ads, columns=["Title", "Price", "Date", "Rooms", "Bathrooms", "Surface Area", "Link", "City", "Equipment"])
        st.dataframe(ads_df)
        visualize(ads_df)
    else:
        st.write("No results found")

    # Close the session
    session.close()

### Visualization Function
def visualize(ads_df):
    # A bar graph showing the number of ads per city
    st.subheader('Number of Ads per City')
    chart_ads_per_city = alt.Chart(ads_df).mark_bar().encode(
        x='City:N',
        y='count():Q',
        color='City:N'
    )
    st.altair_chart(chart_ads_per_city, use_container_width=True)

    st.subheader('Sunburst of Ads Per City')

    # Group data by city and count ads
    ads_per_city = ads_df.groupby('City').size().reset_index(name='Count')

    # Sunburst with Plotly
    fig = px.sunburst(
        ads_per_city,
        path=['City'],
        values='Count',
        color='Count',
        color_continuous_scale='Inferno',
        title='Ads Per City'
    )
    fig.update_layout(title_font_size=20, title_x=0.5, margin=dict(t=50, l=25, r=25, b=25))

    st.plotly_chart(fig, use_container_width=True)

    # A histogram to visualize the distribution of prices
    st.subheader('Price Distribution')
    chart_price_histogram = alt.Chart(ads_df).mark_bar().encode(
        x='Price:Q',
        y='count():Q'
    )
    st.altair_chart(chart_price_histogram, use_container_width=True)

    # A boxplot comparing price ranges per city
    st.subheader('Price Ranges per City')
    chart_price_boxplot = alt.Chart(ads_df).mark_boxplot().encode(
        x='City:N',
        y='Price:Q'
    )
    st.altair_chart(chart_price_boxplot, use_container_width=True)

    # Analysis of property characteristics
    st.subheader('Property Characteristics')
    # A camembert illustrating the distribution of equipment
    chart_equipment_camembert = alt.Chart(ads_df).mark_arc().encode(
        theta='count():Q',
        color='Equipment:N'
    )
    st.altair_chart(chart_equipment_camembert, use_container_width=True)

    # A bar chart for the number of rooms per city
    st.subheader('Number of Rooms per City')
    chart_rooms_bar = alt.Chart(ads_df).mark_bar(color='#ffffff').encode(
    x='City:N',
    y=alt.Y('Rooms:Q', title='Number of Rooms')
    )
    st.altair_chart(chart_rooms_bar, use_container_width=True)

    # A bar chart for the number of bathrooms per city
    st.subheader('Number of Bathrooms per City')
    chart_bathrooms_bar = alt.Chart(ads_df).mark_bar(color='fuchsia').encode(
    x='City:N',
    y=alt.Y('Bathrooms:Q', title='Number of Bathrooms')
    )
    st.altair_chart(chart_bathrooms_bar, use_container_width=True)
    # Temporal analysis
    st.subheader('Evolution of Ads over Time')
    chart_ads_over_time = alt.Chart(ads_df).mark_line().encode(
        x='Date:T',
        y='count():Q'
    )
    st.altair_chart(chart_ads_over_time, use_container_width=True)


   # Relationship between surface and price
    st.subheader('Surface vs Price')
    chart_surface_price_scatter = alt.Chart(ads_df).mark_point().encode(
        x=alt.X('Surface Area:Q', title='Surface (m²)'),
        y='Price:Q',
        color='City:N',
        tooltip=['Title', 'Price', 'Surface Area', 'City']
    )
    st.altair_chart(chart_surface_price_scatter, use_container_width=True)

    # Table for filtered data
    st.subheader('Filtered Data')
    st.dataframe(ads_df)

if __name__ == "__main__":
    main()