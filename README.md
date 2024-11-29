
# Interactive Real Estate Dashboard (IRED) 🏠

## Overview 📊
**IRED** (Interactive Real Estate Dashboard) is a web application built with **Streamlit**, **PostgreSQL**, and **Python**. It allows users to explore, filter, and analyze real estate advertisements interactively, offering insights into the real estate market.

---

## Features 🎯
- **Filter Ads** by city, price, rooms, bathrooms, and equipment.
- **Interactive Visualizations** with **Altair** and **Plotly**.
- **Real-Time Data Exploration** through **PostgreSQL** integration.
- **Display Key Metrics**: price distribution, rooms, surface area, etc.
  
---

## Tech Stack ⚙️
- **Python** 3.9+
- **Streamlit** for the web app
- **PostgreSQL** for database management
- **Pandas** for data manipulation
- **Altair & Plotly** for data visualizations

---

## Requirements 🔧

### Software Dependencies:
- Python 3.9 or higher
- PostgreSQL (or compatible database)
- Streamlit for building the web app
- Pandas, Altair, Plotly, psycopg2 for connecting to PostgreSQL

### Install Python Packages:
```bash
pip install -r requirements.txt
```

### Requirements for Database:
- PostgreSQL Database (or compatible system) running locally or remotely.

---

## Database Setup 🗄️

### Step 1: Create Database
If you're setting up your own database:

1. Create a new PostgreSQL database:
   ```bash
   CREATE DATABASE real_estate_dashboard;
   ```

2. Set up the necessary tables with the following structure:
   - **Annonce** (for ads)
   - **Ville** (for city)
   - **Équipement** (for listing features)
   - **AnnonceEquipement** (for equipment relationships)

### Step 2: Connect to Database
Ensure your database connection details are properly configured in the `queries.py` file to interact with your local or remote PostgreSQL instance.

---

## How to Run 🚀

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-estate-dashboard.git
   cd real-estate-dashboard
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

   This will open the application in your default web browser.

---

## Usage 👨‍💻

### Filter Ads:
- **City**: Choose from the available cities or leave blank for all cities.
- **Price**: Set a price range to filter ads based on your budget.
- **Rooms**: Specify the minimum and maximum number of rooms.
- **Bathrooms**: Choose the bathroom range for the properties.
- **Equipment**: Select the available equipment like a pool, garage, etc.
- **Date Range**: Filter properties added within a specific date range.

---

## Visualizations 📈

The dashboard includes several interactive charts to analyze real estate data:

1. **Bar Chart** - Number of ads per city.
2. **Sunburst Chart** - Distribution of ads per city.
3. **Histogram** - Distribution of property prices.
4. **Boxplot** - Price ranges across different cities.
5. **Scatter Plot** - Relation between surface area and price.
6. **Time Series** - Evolution of advertisements over time.

---

## Contributing 🤝

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements 🙏
- [Streamlit](https://streamlit.io/) - For building interactive apps easily.
- [PostgreSQL](https://www.postgresql.org/) - For reliable database management.
- [Altair](https://altair-viz.github.io/) & [Plotly](https://plotly.com/) - For interactive visualizations.
