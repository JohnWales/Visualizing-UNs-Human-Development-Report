import requests
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
import dash  # (version 1.12.0) pip install dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
import numpy as np

import os

import json

# from flask_caching import Cache

app = dash.Dash(__name__)
server = app.server
# cache = Cache(app.server, config={
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'redis',
#     'CACHE_REDIS_URL': os.environ.get('REDIS_URL', '')
# })
# app.config.suppress_callback_exceptions = True

# timeout = 20


# --------------------------------------------------------------------------------------------------------- #





# --------------------------------------------------------------------------------------------------------- #
# # App layout



# df7 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv('csv_files/all_data.csv')

# df17 = df7.sort_values("hdi_value").reset_index(drop=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# --------------------------------------------------------------------------------------------------------- #

df8 = df.copy()
# df8 = df8['year','hdi_value','life_expectancy']

df8 = df8[['Life Expectancy','year','Human Development Index','Education Index','Income Index']]
# print(df8)

available_indicators = df['Country_name'].unique()



app.layout = html.Div([
    html.Div(children=[
        html.Button('Add Chart', id='add-chart', n_clicks=0),
    ]),
    html.Div(id='container', children=[]),

    # dcc.Store stores the intermediate value
    dcc.Store(id='intermediate-value')
])


@app.callback(
    Output('container', 'children'),
    [Input('add-chart', 'n_clicks')],
    [State('container', 'children')]
)
def display_graphs(n_clicks, div_children):
    new_child = html.Div(
        style={'width': '45%', 'display': 'inline-block', 'outline': 'thin lightgrey solid', 'padding': 10},
        children=[
            dcc.Graph(
                id={
                    'type': 'dynamic-graph',
                    'index': n_clicks
                },
                figure={}
            ),
            dcc.RadioItems(
                id={
                    'type': 'dynamic-choice',
                    'index': n_clicks
                },
                options=[
                         {'label': 'Line Chart', 'value': 'line'},
                         {'label': 'Bar Chart', 'value': 'bar'},
                         {'label': 'Pie Chart', 'value': 'pie'}],
                value='line',
            ),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-s',
                    'index': n_clicks
                },
                options=[{'label': s, 'value': s} for s in np.sort(df['Country_name'].unique())],
                multi=True,
                value=[],
                placeholder="Select a Country"
            ),
            html.H3("x-axis"),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-ctg',
                    'index': n_clicks
                },
                # options=[{'label': c, 'value': c} for c in ['Human Development Index', 'Life Expectancy', 'Country_name', 'year', 'Income Index']],
                options=[{'label': c, 'value': c} for c in ['year']],
                value=[],
                clearable=False,
                placeholder="Select a value for the x-axis",
                disabled=True
            ),
            html.H3("y-axis"),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-num',
                    'index': n_clicks
                },
                # options=[{'label': n, 'value': n} for n in ['hdi_value', 'life_expectancy', 'Country_name', 'year']],
                options=[{'label': n, 'value': n} for n in ['Human Development Index', 'Life Expectancy', "Education Index", 'Income Index']],
                value=[],
                clearable=False,
                placeholder="Select a value for the y-axis"
            )
        ]
    )
    div_children.append(new_child)
    return div_children




@app.callback(
    Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
    [Input(component_id={'type': 'dynamic-dpn-s', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'dynamic-dpn-ctg', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'dynamic-dpn-num', 'index': MATCH}, component_property='value'),
     Input({'type': 'dynamic-choice', 'index': MATCH}, 'value')]
)


# s_value = Countries selected from dropdown
# ctg_value = Country_name
# num_value = year
def update_graph(s_value, ctg_value, num_value, chart_choice):
    # Country from dropdown
    print("s_value = ", s_value)
    # dff = df[df['year'].isin(s_value)]
    # print(dff)

    print("ctg_value = ", ctg_value)
    print("num_value = ", num_value)
    print("chart_choice = ", chart_choice)

    dff = df[df.Country_name.isin(s_value)]
    
    if chart_choice == 'bar':
        # dff = dff.groupby([ctg_value], as_index=False)[['hdi_value', 'life_expectancy', 'Country_name', 'year']].sum()
        fig = px.bar(dff, x='Country_name', y=num_value, color='Country_name', hover_name="year", barmode='group', title="Bar Chart", 
        labels={
                     "Country_name": "Country name"
                 },)
        return fig
    elif chart_choice == 'line':
        # if len(s_value) == 0:
        #     return {}
        # else:
            # dff = dff.groupby([ctg_value, 'year'], as_index=False)[['hdi_value', 'life_expectancy', 'Country_name', 'year']].sum()
            # fig = px.line(dff, x='year', y=num_value, color=ctg_value)
            # return fig
            fig = px.line(dff, x='year', y=num_value, color='Country_name', hover_name="year", title="Line Graph", 
            labels={
                     "year": "Year"
                 },)
            fig.update_traces(mode='lines+markers')
            return fig
    elif chart_choice == 'pie':
        # if len(s_value) == 60:
        #     return {}
        # else:
            dff = df[df['Country_name'].isin(s_value)]
            # fig = px.pie(dff, names=ctg_value, values=num_value, hover_name="Country_name")
            fig = px.pie(dff, names="Country_name", values=num_value, title="Pie Chart")
            return fig


if __name__ == '__main__':
    app.run_server(debug=True)
