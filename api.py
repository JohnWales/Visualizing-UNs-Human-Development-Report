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


# # --------------------------------------------------------------------------------------------------------- #
response = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=103206')

# List of countries
api = response.json()
df = pd.DataFrame(api)
# print(df["country_name"].values)



# # --------------------------------------------------------------------------------------------------------- #
# # App layout



df = pd.read_csv('csv_files/hdi.csv')
df1 = pd.read_csv('csv_files/life_expectancy_index.csv')

df_year = df[['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']]

# print(df_year)

# HDI 2019
fig = px.scatter(df, x="Country_code", y="2019",
                 size="2019", color="Country_name", hover_name="Country_name",
                 size_max=10)

# Life expectancy 2018
fig1 = px.scatter(df1, x="Country_code", y="2018",
                 size="2018", color="Country_name", hover_name="Country_name",
                 size_max=10)

# HDI bar chart 2019
fig2 = px.bar(df, x = 'Country_code', y = '2019', 
                color="Country_name", hover_name="Country_name")

# Life expectancy 2019
fig3 = px.scatter(df1, x = 'Country_code', y = '2019', hover_name="Country_name")

# Life Expectancy 2019 Line Graph
fig4 = px.line(df1, x = 'Country_code', y = '2019', title='Line Graph')

# fig5 = px.strip(df1, x='Country_code', y='2019')



app.layout = html.Div(children=[
    html.Div([
    html.H1("HDI values for all countries in 2019", style={'text-align': 'center'}),
    dcc.Graph(
        id='country-vs-hdi',
        figure=fig
    )
]),
    html.Div([
        html.H1("HDI values for all countries in 2018", style={'text-align': 'center'}),
        dcc.Graph(
            id='country-vs-lifeexpactancy',
            figure=fig1
        )
    ]),
    html.Div([
        html.H1("HDI bar chart for all countries in 2019", style={'text-align': 'center'}),
        dcc.Graph(
            id='hdi-barchart',
            figure=fig2
        )
    ]),
    html.Div([
        html.H1("HDI + life expectancy 2019", style={'text-align': 'center'}),
        dcc.Graph(
            id='hdi-lifeexpectancy',
            figure=fig3
        ),
        dcc.Graph(
            id='hdi-lifeexpectancy1',
            figure=fig
        )
    ]),
    html.Div([
        html.H1("Line Graph", style={'text-align': 'center'}),
        dcc.Graph(
            id='hdi-linegraph',
            figure=fig4
        )
    ]),
    # html.Div([
    #     html.H1("Strip Plot", style={'text-align': 'center'}),
    #     dcc.Graph(
    #         id='hdi-stripplot',
    #         figure=fig5
    #     )
    # ]),



    dcc.Dropdown(id='dpdn2', value=[], multi=True,
            options=[{'label': x, 'value': x} for x in
                    df.Country_name.unique()]),
    # dcc.Dropdown(id='dpdn3', value=[], multi=True,
    #         options=[{'label': x, 'value': x} for x in
    #                 df1.Country_name.unique()]),
    html.Div([
        html.H1("Dropdown Graph", style={'text-align': 'center'}),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
            config={
                'staticPlot': False,     # True, False
                'scrollZoom': True,      # True, False
                'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                'showTips': False,       # True, False
                'displayModeBar': True,  # True, False, 'hover'
                'watermark': True,
                # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                },
            className='six columns'
            )
    ]),



    html.Div([

        html.Br(),
        html.Label(['Choose 3 Cuisines to Compare:'],style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Dropdown(id='cuisine_one',
            options=[{'label':x, 'value':x} for x in df.Country_name.unique()],
            multi=False,
            # value = [],
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose Cuisine...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),

        dcc.Dropdown(id='cuisine_two',
            options=[{'label':x, 'value':x} for x in df1.Country_name.unique()],
            multi=False,
            # value = [],
            clearable=False,
            style={'width':"90%"},
            persistence='string',
            persistence_type='session'),

    ],className='three columns'),

    html.Div([
        dcc.Graph(id='our_graph')
    ],className='nine columns'),



])

@app.callback(
Output(component_id='my-graph', component_property='figure'),
Input(component_id='dpdn2', component_property='value')
)

def update_graph(country_chosen):
    dff = df[df.Country_name.isin(country_chosen)]
    # dff1 = df[df.Country_name.isin(country_chosen1)]
    fig = px.line(data_frame=dff, x='2018', y='Country_code', color='Country_name', hover_name="2018")
    # fig1 = px.line(data_frame=dff1, x='2018', y='Country_code', color='Country_name')
    # fig = px.bar(data_frame=dff, x ='2018', y ='Country_code', color="Country_name")
    fig.update_traces(mode='lines+markers')
    # fig1.update_traces(mode='lines+markers')

    return fig






@app.callback(
    Output('our_graph','figure'),
    [Input('cuisine_one','value'),
     Input('cuisine_two','value')]
)

def build_graph(first_cuisine, second_cuisine):
    dff1=df[(df['Country_code']==first_cuisine)|
           (df['Country_code']==second_cuisine)]
    # print(dff[:5])

    fig = px.line(dff1, x="2019", y="Country_code", color='Country_code')
    fig.update_layout(yaxis={'title':'NEGATIVE POINT'},
                      title={'text':'Restaurant Inspections in NYC',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig




# --------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run_server(debug=True)