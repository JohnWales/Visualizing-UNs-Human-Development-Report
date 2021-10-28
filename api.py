import requests
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output

import json

app = dash.Dash(__name__)


# --------------------------------------------------------------------------------------------------------- #
response = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=137506')

# List of countries
api = response.json()
df = pd.DataFrame(api)
#print(df["country_name"].values)



# --------------------------------------------------------------------------------------------------------- #
# App layout



df = pd.read_csv('csv_files/hdi.csv')
df1 = pd.read_csv('csv_files/life_expectancy_index.csv')


fig = px.scatter(df, x="Country", y="2019",
                 size="2019", color="Country", hover_name="Country",
                 size_max=10)

fig1 = px.scatter(df1, x="Country", y="2018",
                 size="2018", color="Country", hover_name="Country",
                 size_max=10)

app.layout = html.Div([
    html.H1("HDI values for all countries in 2019", style={'text-align': 'center'}),
    dcc.Graph(
        id='country-vs-hdi',
        figure=fig,
        figure1 = fig1
    )
])




# --------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    app.run_server(debug=True)


