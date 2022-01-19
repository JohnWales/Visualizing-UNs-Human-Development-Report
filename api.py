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
# response = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=103206')

# # List of countries
# api = response.json()
# df = pd.DataFrame(api)
# print(df["country_name"].values)



# --------------------------------------------------------------------------------------------------------- #
# # App layout


df = pd.read_csv('csv_files/hdi.csv')
df1 = pd.read_csv('csv_files/life_expectancy_index.csv')
# df7 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df7 = pd.read_csv('csv_files/all_data.csv')


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]








# --------------------------------------------------------------------------------------------------------- #








app.layout = html.Div(children=[


    html.Div([
        html.H1(children="Visualising the Human Developemnt Report", className='header-title', style={'fontSize': '48px', 'text-align': 'center'}),
        html.P(children="This is a visual representation on the United Nations Human Developemtn Report from 1990 to present day.", className='header-description'),

    html.H3("Pick Country"),
    dcc.Dropdown(id='country-dropdown', value=[], multi=True,
    options=[{'label': x, 'value': x} for x in
            df7.Country_name.unique()]),

    html.H3("x-axis"),
    dcc.Dropdown(id='x-dropdown', value=[], multi=True,
    options=[{'label': x, 'value': x} for x in
            df7]),

    html.H3("y-axis"),
    dcc.Dropdown(id='y-dropdown', value=[], multi=True,
    options=[{'label': x, 'value': x} for x in
            df7]),


    dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
        config={
            'staticPlot': False,     # Zooming when dragging mouse and forming a box and also classical zooming
            'scrollZoom': False,      # Classical zooming
            'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
            'showTips': False,     
            'displayModeBar': True,  # True, False, 'hover'
            'watermark': False,
            # 'modeBarButtonsToRemove': ['pan2d','select2d'],
            },
        className='six columns'
        )
    # dcc.Slider(
    #     id='year-slider',
    #     min=df7['year'].min(),
    #     max=df7['year'].max(),
    #     value=df7['year'].min(),
    #     marks={str(year): str(year) for year in df7['year'].unique()},
    #     step=None
    # )

    ]),






    # dcc.Graph(id='graph-with-slider'),
    # dcc.Slider(
    #     id='year-slider',
    #     min=df7['year'].min(),
    #     max=df7['year'].max(),
    #     value=df7['year'].min(),
    #     marks={str(year): str(year) for year in df7['year'].unique()},
    #     step=None
    # )




])














# --------------------------------------------------------------------------------------------------------- #






@app.callback(
Output(component_id='my-graph', component_property='figure'),
Input(component_id='country-dropdown', component_property='value')
# Input(component_id='x-dropdown', component_property='value'),
# Input(component_id='y-dropdown', component_property='value')
)

def update_graph(country_chosen):
    dff = df7[df7.Country_name.isin(country_chosen)]
    # dff1 = df[df.Country_name.isin(country_chosen1)]
    fig = px.line(data_frame=dff, x='year', y='life_expectancy', color='Country_name', hover_name="year")
    # fig1 = px.line(data_frame=dff1, x='2018', y='Country_code', color='Country_name')
    # fig = px.bar(data_frame=dff, x ='2018', y ='Country_code', color="Country_name")
    fig.update_traces(mode='lines+markers')
    # fig1.update_traces(mode='lines+markers')

    return fig




# @app.callback(
# Output(component_id='my-graph', component_property='figure'),
# Input(component_id='dropdown', component_property='value')
# )

# def update_graph(country_chosen):
#     dff = df7[df7.Country_name.isin(country_chosen)]
#     # dff1 = df[df.Country_name.isin(country_chosen1)]
#     fig = px.line(data_frame=dff, x='year', y='life_expectancy', color='Country_name', hover_name="year")
#     # fig1 = px.line(data_frame=dff1, x='2018', y='Country_code', color='Country_name')
#     # fig = px.bar(data_frame=dff, x ='2018', y ='Country_code', color="Country_name")
#     fig.update_traces(mode='lines+markers')
#     # fig1.update_traces(mode='lines+markers')

#     return fig


# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df7[df7.year == selected_year]

#     fig7 = px.scatter(filtered_df, x="life_expectancy", y="hdi_value", hover_name="Country_name", size_max=100, color='Country_name')

#     fig7.update_layout(transition_duration=500)

#     return fig7










# --------------------------------------------------------------------------------------------------------- #





if __name__ == '__main__':
    app.run_server(debug=True)