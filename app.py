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




app = dash.Dash(__name__)
server = app.server



# --------------------------------------------------------------------------------------------------------- #





# --------------------------------------------------------------------------------------------------------- #
# # App layout



df = pd.read_csv('csv_files/all_data.csv')
# df = pd.read_csv('csv_files/backup.csv')


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
                    'type': 'map-choice',
                    'index': n_clicks
                },
                options=[
                         {'label': 'Line Chart', 'value': 'line'},
                         {'label': 'Bar Chart', 'value': 'bar'},
                         {'label': 'Pie Chart', 'value': 'pie'},
                         {'label': 'Map', 'value': 'map'},
                         {'label': 'Bubble Map', 'value': 'bubblemap'}],
                         
                value='line',
            ),
            dcc.Dropdown(
                id={
                    'type': 'country-dropdown',
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
                    'type': 'xaxis-dropdown',
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
                    'type': 'yaxis-dropdown',
                    'index': n_clicks
                },
                # options=[{'label': n, 'value': n} for n in ['hdi_value', 'life_expectancy', 'Country_name', 'year']],
                options=[{'label': n, 'value': n} for n in ['Life Expectancy','Human Development Index','Education Index','Income Index']],
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
    # Multiple inputs so it needs to be inside a list
    [Input(component_id={'type': 'country-dropdown', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'xaxis-dropdown', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'yaxis-dropdown', 'index': MATCH}, component_property='value'),
     Input({'type': 'map-choice', 'index': MATCH}, 'value')]

    #  prevent_initial_call=True
)


# country-chosen = Countries selected from dropdown
# ctg_value = Country_name
# indicator_chosen_yaxis = year
def update_graph(country_chosen, ctg_value, indicator_chosen_yaxis, chart_choice):
    # Country from dropdown
    print("country-chosen = ", country_chosen)
    # dff = df[df['year'].isin(country-chosen)]
    # print(dff)

    print("ctg_value = ", ctg_value)
    print("indicator_chosen_yaxis = ", indicator_chosen_yaxis)
    print("chart_choice = ", chart_choice)

    dff = df[df.Country_name.isin(country_chosen)]
    
    if chart_choice == 'bar':
        # dff = dff.groupby([ctg_value], as_index=False)[['hdi_value', 'life_expectancy', 'Country_name', 'year']].sum()
        fig = px.bar(dff, x='Country_name', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", barmode='group', title="Bar Chart", 
        labels={
                     "Country_name": "Country name"
                 },)
        return fig
        
    elif chart_choice == 'line':
        fig = px.line(dff, x='year', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
        labels={
                    "year": "Year"
                },)
        fig.update_traces(mode='lines+markers')
        return fig
    elif chart_choice == 'pie':
        dff = df[df['Country_name'].isin(country_chosen)]
        # fig = px.pie(dff, names=ctg_value, values=indicator_chosen_yaxis, hover_name="Country_name")
        fig = px.pie(dff, names="Country_name", values=indicator_chosen_yaxis, title="Pie Chart")
        return fig
    elif chart_choice == 'map':
        # # dff = df[df['Country_name'].isin(country_chosen)]
        fig = px.choropleth(dff, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", 
                    color_continuous_scale=px.colors.sequential.Plasma)
        return fig
    elif chart_choice == 'bubblemap':
        fig = px.scatter_geo(dff, locations="Country_code")
        return fig



if __name__ == '__main__':
    app.run_server(debug=True)

