# import requests
# import pandas as pd
# import plotly.express as px  # (version 4.7.0)
# import plotly.graph_objects as go
# from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
# import dash  # (version 1.12.0) pip install dash
# #import dash_core_components as dcc
# from dash import dcc
# #import dash_html_components as html
# from dash import html
# from dash.dependencies import Input, Output
# import numpy as np




# app = dash.Dash(__name__)
# server = app.server



# # --------------------------------------------------------------------------------------------------------- #





# # --------------------------------------------------------------------------------------------------------- #
# # # App layout



# df = pd.read_csv('csv_files/all_data.csv')
# # df = pd.read_csv('csv_files/backup.csv')


# # Found that all the indicators except for year are objects not ints. This could be the source of the random values along the axis problem
# print(df.info())


# # Trying to make the y axis ascend numerically
# # df = df.sort_values("Human Development Index").reset_index(drop=True)
# # df = df.sort_values("Life Expectancy").reset_index(drop=True)
# # df = df.sort_values("Education Index").reset_index(drop=True)
# # df = df.sort_values("Income Index").reset_index(drop=True)

# # df.reset_index(drop=True, inplace=True)




# # df17 = df7.sort_values("hdi_value").reset_index(drop=True)

# external_stylesheets = [
#     {
#         "href": "https://fonts.googleapis.com/css2?"
#                 "family=Lato:wght@400;700&display=swap",
#         "rel": "stylesheet",
#     },
# ]

# # --------------------------------------------------------------------------------------------------------- #

# df8 = df.copy()
# # df8 = df8['year','hdi_value','life_expectancy']

# df8 = df8[['Life Expectancy','year','Human Development Index','Education Index','Income Index']]
# # print(df8)

# available_indicators = df['Country_name'].unique()



# app.layout = html.Div([
#     html.Div(children=[
#         html.Button('Add Chart', id='add-chart', n_clicks=0),
#     ]),
#     html.Div(id='container', children=[]),

# ])


# @app.callback(
#     Output('container', 'children'),
#     [Input('add-chart', 'n_clicks')],
#     [State('container', 'children')]
# )
# def display_graphs(n_clicks, div_children):
#     new_child = html.Div(
#         style={'width': '45%', 'display': 'inline-block', 'outline': 'thin lightgrey solid', 'padding': 10},
#         children=[
#             dcc.Graph(
#                 id={
#                     'type': 'dynamic-graph',
#                     'index': n_clicks
#                 },
#                 figure={}
#             ),
#             # dcc.Slider(
#             #     df['year'].min(),
#             #     df['year'].max(),
#             #     step=None,
#             #     value=df['year'].min(),
#             #     marks={str(year): str(year) for year in df['year'].unique()},
#             #     id='year-slider'
#             # ),
#             dcc.RadioItems(
#                 id={
#                     'type': 'graph-choice',
#                     'index': n_clicks
#                 },
#                 options=[
#                          {'label': 'Line Chart', 'value': 'line'},
#                          {'label': 'Bar Chart', 'value': 'bar'},
#                          {'label': 'Pie Chart', 'value': 'pie'},
#                          {'label': 'Map', 'value': 'map'},
#                          {'label': 'Bubble Map', 'value': 'bubblemap'}],
                         
#                 value='line',
#             ),
#             dcc.Dropdown(
#                 id={
#                     'type': 'country-dropdown',
#                     'index': n_clicks
#                 },
#                 options=[{'label': s, 'value': s} for s in np.sort(df['Country_name'].unique())],
#                 multi=True,
#                 value=[],
#                 placeholder="Select a Country"
#             ),
#             html.H3("x-axis"),
#             dcc.Dropdown(
#                 id={
#                     'type': 'xaxis-dropdown',
#                     'index': n_clicks
#                 },
#                 options=[{'label': c, 'value': c} for c in ['Human Development Index', 'Life Expectancy', 'Country_name', 'year', 'Income Index']],
#                 # options=[{'label': c, 'value': c} for c in ['year']],
#                 value=[],
#                 clearable=False,
#                 placeholder="Select a value for the x-axis"
#                 # disabled=True
#             ),
#             html.H3("y-axis"),
#             dcc.Dropdown(
#                 id={
#                     'type': 'yaxis-dropdown',
#                     'index': n_clicks
#                 },
#                 # options=[{'label': n, 'value': n} for n in ['hdi_value', 'life_expectancy', 'Country_name', 'year']],
#                 options=[{'label': n, 'value': n} for n in ['Life Expectancy','Human Development Index','Education Index','Income Index']],
#                 value=[],
#                 clearable=False,
#                 placeholder="Select a value for the y-axis"
#             )
#         ]
#     )
#     div_children.append(new_child)
#     return div_children




# @app.callback(
#     Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
#     # Multiple inputs so it needs to be inside a list
#     [Input(component_id={'type': 'country-dropdown', 'index': MATCH}, component_property='value'),
#      Input(component_id={'type': 'xaxis-dropdown', 'index': MATCH}, component_property='value'),
#      Input(component_id={'type': 'yaxis-dropdown', 'index': MATCH}, component_property='value'),
#     #  Input('year-slider', 'value'),
#      Input({'type': 'graph-choice', 'index': MATCH}, 'value')]
# )


# # country-chosen = Countries selected from dropdown
# # ctg_value = Country_name
# # indicator_chosen_yaxis = year
# def update_graph(country_chosen, ctg_value, indicator_chosen_yaxis, chart_choice):
#     # Country from dropdown
#     print("country-chosen = ", country_chosen)
#     print("ctg_value = ", ctg_value)
#     print("indicator_chosen_yaxis = ", indicator_chosen_yaxis)
#     print("chart_choice = ", chart_choice)

#     dff = df[df.Country_name.isin(country_chosen)]
    
#     if chart_choice == 'bar':
#         # dff = dff.groupby([ctg_value], as_index=False)[['hdi_value', 'life_expectancy', 'Country_name', 'year']].sum()
#         fig = px.bar(dff, x='Country_name', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", barmode='group', title="Bar Chart", 
#         labels={
#                      "Country_name": "Country name"
#                  },)
#         return fig
#     elif chart_choice == 'line':
#         # filtered_df = df[df.year == selected_year]
#         # fig = px.line(filtered_df, x='year', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
#         fig = px.line(dff, x='year', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
#         # fig = px.line(dff, x=ctg_value, y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
#         labels={
#                     "year": "Year"
#                 },)
#         fig.update_traces(mode='lines+markers')
#         return fig
#     elif chart_choice == 'pie':
#         dff = df[df['Country_name'].isin(country_chosen)]
#         # fig = px.pie(dff, names=ctg_value, values=indicator_chosen_yaxis, hover_name="Country_name")
#         fig = px.pie(dff, names="Country_name", values=indicator_chosen_yaxis, title="Pie Chart")
#         return fig
#     elif chart_choice == 'map':
#         # # dff = df[df['Country_name'].isin(country_chosen)]
#         fig = px.choropleth(dff, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", title="Map", 
#                     color_continuous_scale=px.colors.sequential.Plasma)
#         return fig
#     elif chart_choice == 'bubblemap':
#         fig = px.scatter_geo(dff, locations="Country_code", title="Bubble Map", hover_name="Country_name")
#         return fig



# if __name__ == '__main__':
#     app.run_server(debug=True)



# from ensurepip import bootstrap
from pydoc import classname
from turtle import width
import dash  # use Dash version 1.16.0 or higher for this app to work
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

import dash_bootstrap_components as dbc

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
# app = dash.Dash(__name__, external_stylesheets = [dbc.themes.CYBORG])


# df = pd.read_csv('csv_files/all_data.csv')
df = pd.read_csv('csv_files/backup.csv')

df9 = df.copy()

df8 = df.copy()
# df8 = df8[['Life Expectancy','Human Development Index','Education Index','Income Index','Gross National Income']]
df8 = df8[['Life Expectancy','Human Development Index','Education Index','Income Index','Gross National Income',
'Total Population','Gender Inequality Index','Unemployment ( Percentage of Labour Force )','Life Expectancy ( Years )',
'Mean Years of Schooling']]

country_df = ['Afghanistan' ,'Angola' ,'Albania' ,'Andorra' ,'United Arab Emirates','Argentina' ,'Armenia' ,'Antigua and Barbuda' ,'Australia' ,'Austria','Azerbaijan' ,'Burundi' ,'Belgium' ,'Benin' ,'Burkina Faso' ,'Bangladesh','Bulgaria' ,'Bahrain' ,'Bahamas' ,'Bosnia and Herzegovina' ,'Belarus','Belize' ,'Bolivia (Plurinational State of)' ,'Brazil' ,'Barbados','Brunei Darussalam' ,'Bhutan' ,'Botswana' ,'Central African Republic','Canada' ,'Switzerland' ,'Chile' ,'China' ,'Cote dIvoire','Cameroon','Congo (Democratic Republic of the)' ,'Congo' ,'Colombia' ,'Comoros','Cabo Verde' ,'Costa Rica' ,'Cuba' ,'Cyprus' ,'Czechia' ,'Germany' ,'Djibouti','Dominica' ,'Denmark' ,'Dominican Republic' ,'Algeria' ,'Ecuador' ,'Egypt','Eritrea' ,'Spain' ,'Estonia' ,'Ethiopia' ,'Finland' ,'Fiji' ,'France','Micronesia (Federated States of)' ,'Gabon' ,'United Kingdom' ,'Georgia','Ghana' ,'Guinea' ,'Gambia' ,'Guinea-Bissau' ,'Equatorial Guinea' ,'Greece','Grenada' ,'Guatemala' ,'Guyana' ,'Hong Kong, China (SAR)' ,'Honduras','Croatia' ,'Haiti' ,'Hungary' ,'Indonesia' ,'India' ,'Ireland','Iran (Islamic Republic of)' ,'Iraq' ,'Iceland' ,'Israel' ,'Italy' ,'Jamaica','Jordan' ,'Japan' ,'Kazakhstan' ,'Kenya' ,'Kyrgyzstan' ,'Cambodia' ,'Kiribati','Saint Kitts and Nevis' ,'Korea (Republic of)' ,'Kuwait','Lao Peoples Democratic Republic','Lebanon' ,'Liberia' ,'Libya','Saint Lucia' ,'Liechtenstein' ,'Sri Lanka' ,'Lesotho' ,'Lithuania','Luxembourg' ,'Latvia' ,'Morocco' ,'Moldova (Republic of)' ,'Madagascar','Maldives' ,'Mexico' ,'Marshall Islands' ,'North Macedonia' ,'Mali' ,'Malta','Myanmar' ,'Montenegro' ,'Mongolia' ,'Mozambique' ,'Mauritania' ,'Mauritius','Malawi' ,'Malaysia' ,'Namibia' ,'Niger' ,'Nigeria' ,'Nicaragua' ,'Netherlands','Norway' ,'Nepal' ,'New Zealand','Oman' ,'Pakistan' ,'Panama' ,'Peru','Philippines' ,'Palau' ,'Papua New Guinea' ,'Poland' ,'Portugal' ,'Paraguay','Palestine, State of' ,'Qatar' ,'Romania' ,'Russian Federation' ,'Rwanda','Saudi Arabia' ,'Sudan' ,'Senegal' ,'Singapore' ,'Solomon Islands','Sierra Leone' ,'El Salvador' ,'Serbia' ,'South Sudan','Sao Tome and Principe' ,'Suriname' ,'Slovakia' ,'Slovenia' ,'Sweden','Eswatini (Kingdom of)' ,'Seychelles' ,'Syrian Arab Republic' ,'Chad' ,'Togo','Thailand' ,'Tajikistan' ,'Turkmenistan' ,'Timor-Leste' ,'Tonga','Trinidad and Tobago' ,'Tunisia' ,'Turkey' ,'Tanzania (United Republic of)','Uganda' ,'Ukraine' ,'Uruguay' ,'United States' ,'Uzbekistan','Saint Vincent and the Grenadines' ,'Venezuela (Bolivarian Republic of)','Viet Nam' ,'Vanuatu' ,'Samoa' ,'Yemen' ,'South Africa' ,'Zambia' ,'Zimbabwe']

# df['Total Population'].fillna(value=df['Total Population'].mean(), inplace=True)

app.layout = html.Div([

    dcc.Slider(
        # min = 1990,
        # max = 2019,
        # dots = False,
        df9['year'].min(),
        df9['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    ),
    dbc.Row([
        dbc.Col([
            html.H4('Choose Indicator', style={'font-size':'100%', 'text-align':'center', 'color': 'white'}),
            dcc.Dropdown(
                id='scatter-indicator-dropdown',
                value=[],
                options=[{'label': n, 'value': n} for n in df8],
                clearable=False,
                placeholder="Choose Indicator",
                style={'font-size':'90%', 'padding':'0px 20px 20px 20px'}
            ),


            html.H4('Choose Country', style={'font-size':'100%', 'text-align':'center', 'color': 'white'}),
            dcc.Dropdown(id='country-scatter-dropdown',
                        value=[],
                        # value=['United States', 'Russian Federation'], 
                        multi=True,
                        clearable=True,
                        options=[{'label': x, 'value': x} for x in df.Country_name.unique()], 
                        # options=[{'label': x, 'value': x} for x in country_df], 
                        placeholder="Select a Country",
                        style={'font-size':'90%', 'padding':'0px 20px 20px 20px'},
                        # style={'font-size':'90%', 'padding':'0px 20px 20px 20px', 'white-space':'nowrap', 'overflow-y': 'scroll', 'height':'50%'},
            ),
        ],
        align="center",
        width=2,
        class_name="col1"
        ),

        dbc.Col(
            dcc.Graph(id='scatter-graph-with-slider', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                config={
                    'staticPlot': False,     # True, False
                    'scrollZoom': False,      # True, False
                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                    'showTips': True,       # True, False
                    'displayModeBar': 'hover',  # True, False, 'hover'
                    'watermark': False,
                    'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d']
                    },
                # className='six columns',
                className='scatter',
            ),
            width=9
        ),
    ]),


    dbc.Row([
        dbc.Col([
            html.H4('Choose Indicator', style={'font-size':'100%', 'text-align':'center', 'color': 'white'}),
            dcc.Dropdown(
                id='yaxis-dropdown',
                value=[],
                options=[{'label': n, 'value': n} for n in df8],
                clearable=False,
                placeholder="Choose Indicator",
                style={'font-size':'90%', 'padding':'0px 20px 20px 20px'}
            ),


            html.H4('Choose Country', style={'font-size':'100%', 'text-align':'center', 'color': 'white'}),
            dcc.Dropdown(id='country_dropdown',
                        value=[],
                        # value=['United States', 'Russian Federation'], 
                        multi=True,
                        clearable=True,
                        options=[{'label': x, 'value': x} for x in df.Country_name.unique()], 
                        # options=[{'label': x, 'value': x} for x in country_df], 
                        placeholder="Select a Country",
                        style={'font-size':'90%', 'padding':'0px 20px 20px 20px'},
                        # style={'font-size':'90%', 'padding':'0px 20px 20px 20px', 'white-space':'nowrap', 'overflow-y': 'scroll', 'height':'50%'},
            ),
        ],
        align="center",
        width=2,
        class_name="col1"
        ),
        
    

        dbc.Col(
            dcc.Graph(id='line-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                config={
                    'staticPlot': False,     # True, False
                    'scrollZoom': False,      # True, False
                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                    'showTips': True,       # True, False
                    'displayModeBar': 'hover',  # True, False, 'hover'
                    'watermark': False,
                    'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d']
                    },
                # className='six columns',
                className='line_graph',
            ),
            width=6
        ),
        dbc.Col(
            dcc.Graph(id='pie-graph', figure={}, className='six columns',
                config={
                    'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d']
                }
            ),
            width=3,
            className='pie_chart',
        )
    ],class_name="row1"
    ),
    dbc.Row(
        dbc.Col(
            dcc.Graph(id='map-graph', figure={}, 
            className='six columns',
                config={
                    'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d']
                }),
            className="map_graph"
    ),class_name="row2",
    ),
]) 
# End of layout




@app.callback(
    Output('scatter-graph-with-slider', 'figure'),
    Input('year-slider', 'value'),
    Input('country-scatter-dropdown', 'value'),
    Input('scatter-indicator-dropdown', 'value')
)

def update_figure(selected_year, country_chosen, indicator_chosen_yaxis):
    # filtered_df = df[df.Country_name.isin(country_chosen)], df[df.year == selected_year]
    # filtered_df = df[df.Country_name.isin(country_chosen)]
    filtered_df = df[df.year == selected_year]
    fig = px.scatter(filtered_df, x='Country_name', y=indicator_chosen_yaxis,
                        size='Total Population', color='Country_name', size_max=55)

    fig.update_layout(transition_duration=500)
    return fig




@app.callback(
    Output(component_id='line-graph', component_property='figure'),
    Input(component_id='country_dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
def update_graph(country_chosen, indicator_chosen_yaxis):
    dff = df[df.Country_name.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y=indicator_chosen_yaxis, color='Country_name',
                  custom_data=['Country_name', 'Country_code', 'Life Expectancy', 'year'],
                  labels={
                    "year": "Year",
                    "Country_name": "Country"
                })
    fig.update_traces(mode='lines+markers')
    fig.update_layout(legend_title="Country Name", hovermode="x", font_color="white",
        legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
    )
    fig.layout.plot_bgcolor = 'white'
    fig.update_layout(font_color="black")
    # fig.add_bar(x='year', y=indicator_chosen_yaxis)
    return fig



# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='line-graph', component_property='hoverData'),
    Input(component_id='line-graph', component_property='clickData'),
    Input(component_id='line-graph', component_property='selectedData'),
    Input(component_id='country_dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
def update_pie_graph(hov_data, clk_data, slct_data, country_chosen, indicator_chosen_yaxis):
    if hov_data is None:
        dff2 = df[df.Country_name.isin(country_chosen)]
        dff2 = dff2[dff2.year == 2000]
        print(dff2)
        # fig2 = px.pie(data_frame=dff2, values='Country_name', names=indicator_chosen_yaxis,
        #               title=indicator_chosen_yaxis, color='Country_name')
        fig2 = px.pie(dff2, values=indicator_chosen_yaxis, names=country_chosen,
                      title=indicator_chosen_yaxis, color='Country_name')
        fig2.update_traces(textposition='inside', textinfo='percent+label+value', showlegend=False)
        fig2.layout.plot_bgcolor = 'white'
        fig2.update_layout(font_color="black")
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')

        dff2 = df[df.Country_name.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2, values=indicator_chosen_yaxis, names='Country_name', title=f'{indicator_chosen_yaxis} {hov_year}', color='Country_name')
        fig2.update_traces(textposition='inside', textinfo='percent+label+value', showlegend=False)
        fig2.layout.plot_bgcolor = 'white'
        fig2.update_layout(font_color="black")
        return fig2
        


@app.callback(
    Output(component_id='map-graph', component_property='figure'),
    Input(component_id='line-graph', component_property='hoverData'),
    Input(component_id='line-graph', component_property='clickData'),
    Input(component_id='line-graph', component_property='selectedData'),
    Input(component_id='country_dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
def update_map_graph(hov_data, clk_data, slct_data, country_chosen, indicator_chosen_yaxis):
    if hov_data is None:
        dff2 = df[df.Country_name.isin(country_chosen)]
        dff2 = dff2[dff2.year == 2000]
        print(dff2)
        fig3 = px.choropleth(dff2, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", 
                    color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")  
        fig3.update_traces(showlegend=False)  
        fig3.layout.plot_bgcolor = 'white' 
        fig3.update_layout(font_color="black")
        return fig3
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')

        dff2 = df[df.Country_name.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig3 = px.choropleth(dff2, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", 
                    color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")  
        fig3.update_traces(showlegend=False)   
        fig3.layout.plot_bgcolor = 'white' 
        fig3.update_layout(font_color="black")
        return fig3



if __name__ == '__main__':
    app.run_server(debug=True)

