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


# df9 = px.data.gapminder().query("year==2007")
# fig = px.scatter_geo(df9, locations="iso_alpha", color="continent",
#                      hover_name="country", size="pop",
#                      projection="natural earth")
# fig.show()






# --------------------------------------------------------------------------------------------------------- #

df8 = df.copy()
# df8 = df8['year','hdi_value','life_expectancy']

df8 = df8[['life_expectancy','year','hdi_value']]
# print(df8)

available_indicators = df['Country_name'].unique()



app.layout = html.Div([
    html.Div(children=[
        html.Button('Add Chart', id='add-chart', n_clicks=0),
    ]),
    html.Div(id='container', children=[])
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
            ),
            html.H3("x-axis"),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-ctg',
                    'index': n_clicks
                },
                # options=[{'label': c, 'value': c} for c in ['hdi_value', 'life_expectancy', 'Country_name', 'year']],
                options=[{'label': c, 'value': c} for c in ['year']],
                value=[],
                clearable=False
            ),
            html.H3("y-axis"),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-num',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['hdi_value', 'life_expectancy', 'Country_name', 'year']],
                value=[],
                clearable=False
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
        fig = px.bar(dff, x='Country_name', y=num_value, color='Country_name', hover_name="year")
        return fig
    elif chart_choice == 'line':
        if len(s_value) == 0:
            return {}
        else:
            # dff = dff.groupby([ctg_value, 'year'], as_index=False)[['hdi_value', 'life_expectancy', 'Country_name', 'year']].sum()
            # fig = px.line(dff, x='year', y=num_value, color=ctg_value)
            # return fig
            fig = px.line(dff, x='year', y=num_value, color='Country_name', hover_name="year")
            fig.update_traces(mode='lines+markers')
            return fig
    elif chart_choice == 'pie':
        dff = df[df['Country_name'].isin(s_value)]
        # fig = px.pie(dff, names=ctg_value, values=num_value, hover_name="Country_name")
        fig = px.pie(dff, names="Country_name", values=num_value, hover_name="Country_name")
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)


# app.layout = html.Div(children=[


#     html.Div([
#         html.H1(children="Visualising the Human Developemnt Report", className='header-title', style={'fontSize': '48px', 'text-align': 'center'}),
#         html.P(children="This is a visual representation on the United Nations Human Developemtn Report from 1990 to present day.", className='header-description'),

#     html.Div
#     ([
#         html.H3("Pick Country"),
#         dcc.Dropdown(id='country-dropdown', value=[], multi=True,
#         options=[{'label': x, 'value': x} for x in
#                 df7.Country_name.unique()]),

#         html.H3("x-axis"),
#         dcc.Dropdown(id='x-dropdown', value=[], multi=True,
#         options=[{'label': x, 'value': x} for x in
#                 df8]),

#         html.H3("y-axis"),
#         dcc.Dropdown(id='y-dropdown', value=[], multi=True,
#         options=[{'label': x, 'value': x} for x in
#                 df8]),
#     ]),





#     dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
#         config={
#             'staticPlot': False,     # Zooming when dragging mouse and forming a box and also classical zooming
#             'scrollZoom': False,      # Classical zooming
#             'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
#             'showTips': False,     
#             'displayModeBar': True,  # True, False, 'hover'
#             'watermark': False,
#             # 'modeBarButtonsToRemove': ['pan2d','select2d'],
#             },
#         className='six columns'
#         ),
#     dcc.Slider(
#         id='year-slider',
#         min=df7['year'].min(),
#         max=df7['year'].max(),
#         value=df7['year'].min(),
#         marks={str(year): str(year) for year in df7['year'].unique()},
#         step=None
#     )

#     ]),

# ])



   

       












# --------------------------------------------------------------------------------------------------------- #






# @app.callback(
# Output(component_id='my-graph', component_property='figure'),
# Input(component_id='country-dropdown', component_property='value')
# # Input('year-slider', 'value'),
# # Input(component_id='x-dropdown', component_property='value'),
# # Input(component_id='y-dropdown', component_property='value')
# )

# def update_graph(country_chosen):
#     dff = df7[df7.Country_name.isin(country_chosen)]

#     fig7 = px.line(data_frame=dff, x='year', y='life_expectancy', color='Country_name', hover_name="year")

#     fig7.update_traces(mode='lines+markers')

#     return fig7














# --------------------------------------------------------------------------------------------------------- #





# if __name__ == '__main__':
#     app.run_server(debug=True)