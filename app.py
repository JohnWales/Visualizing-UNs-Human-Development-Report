# from ensurepip import bootstrap
from optparse import Values
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

df8 = df8[['Life Expectancy','Human Development Index','Education Index','Income Index','Gross National Income',
'Total Population','Gender Inequality Index','Unemployment ( Percentage of Labour Force )','Life Expectancy ( Years )',
'Mean Years of Schooling']]

country_df = ['Afghanistan' ,'Angola' ,'Albania' ,'Andorra' ,'United Arab Emirates','Argentina' ,'Armenia' ,'Antigua and Barbuda' ,'Australia' ,'Austria','Azerbaijan' ,'Burundi' ,'Belgium' ,'Benin' ,'Burkina Faso' ,'Bangladesh','Bulgaria' ,'Bahrain' ,'Bahamas' ,'Bosnia and Herzegovina' ,'Belarus','Belize' ,'Bolivia (Plurinational State of)' ,'Brazil' ,'Barbados','Brunei Darussalam' ,'Bhutan' ,'Botswana' ,'Central African Republic','Canada' ,'Switzerland' ,'Chile' ,'China' ,'Cote dIvoire','Cameroon','Congo (Democratic Republic of the)' ,'Congo' ,'Colombia' ,'Comoros','Cabo Verde' ,'Costa Rica' ,'Cuba' ,'Cyprus' ,'Czechia' ,'Germany' ,'Djibouti','Dominica' ,'Denmark' ,'Dominican Republic' ,'Algeria' ,'Ecuador' ,'Egypt','Eritrea' ,'Spain' ,'Estonia' ,'Ethiopia' ,'Finland' ,'Fiji' ,'France','Micronesia (Federated States of)' ,'Gabon' ,'United Kingdom' ,'Georgia','Ghana' ,'Guinea' ,'Gambia' ,'Guinea-Bissau' ,'Equatorial Guinea' ,'Greece','Grenada' ,'Guatemala' ,'Guyana' ,'Hong Kong, China (SAR)' ,'Honduras','Croatia' ,'Haiti' ,'Hungary' ,'Indonesia' ,'India' ,'Ireland','Iran (Islamic Republic of)' ,'Iraq' ,'Iceland' ,'Israel' ,'Italy' ,'Jamaica','Jordan' ,'Japan' ,'Kazakhstan' ,'Kenya' ,'Kyrgyzstan' ,'Cambodia' ,'Kiribati','Saint Kitts and Nevis' ,'Korea (Republic of)' ,'Kuwait','Lao Peoples Democratic Republic','Lebanon' ,'Liberia' ,'Libya','Saint Lucia' ,'Liechtenstein' ,'Sri Lanka' ,'Lesotho' ,'Lithuania','Luxembourg' ,'Latvia' ,'Morocco' ,'Moldova (Republic of)' ,'Madagascar','Maldives' ,'Mexico' ,'Marshall Islands' ,'North Macedonia' ,'Mali' ,'Malta','Myanmar' ,'Montenegro' ,'Mongolia' ,'Mozambique' ,'Mauritania' ,'Mauritius','Malawi' ,'Malaysia' ,'Namibia' ,'Niger' ,'Nigeria' ,'Nicaragua' ,'Netherlands','Norway' ,'Nepal' ,'New Zealand','Oman' ,'Pakistan' ,'Panama' ,'Peru','Philippines' ,'Palau' ,'Papua New Guinea' ,'Poland' ,'Portugal' ,'Paraguay','Palestine, State of' ,'Qatar' ,'Romania' ,'Russian Federation' ,'Rwanda','Saudi Arabia' ,'Sudan' ,'Senegal' ,'Singapore' ,'Solomon Islands','Sierra Leone' ,'El Salvador' ,'Serbia' ,'South Sudan','Sao Tome and Principe' ,'Suriname' ,'Slovakia' ,'Slovenia' ,'Sweden','Eswatini (Kingdom of)' ,'Seychelles' ,'Syrian Arab Republic' ,'Chad' ,'Togo','Thailand' ,'Tajikistan' ,'Turkmenistan' ,'Timor-Leste' ,'Tonga','Trinidad and Tobago' ,'Tunisia' ,'Turkey' ,'Tanzania (United Republic of)','Uganda' ,'Ukraine' ,'Uruguay' ,'United States' ,'Uzbekistan','Saint Vincent and the Grenadines' ,'Venezuela (Bolivarian Republic of)','Viet Nam' ,'Vanuatu' ,'Samoa' ,'Yemen' ,'South Africa' ,'Zambia' ,'Zimbabwe']



# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Start of Layout

app.layout = html.Div([

    dbc.Row(
        dbc.Col(
        html.H1('VISUALIZING THE UNs HUMAN DEVELOPMENT REPORT')
        ),class_name="title",
    ),

    dbc.Row([
        dbc.Col([
            html.H4('Choose Indicator', style={'font-size':'100%', 'text-align':'center', 'color': 'white'}),
            dcc.Dropdown(
                id='yaxis-dropdown',
                value=[],
                # value=['Human Development Index'],
                options=[{'label': n, 'value': n} for n in df8],
                clearable=False,
                placeholder="Choose Indicator",
                style={'font-size':'90%', 'padding':'0px 20px 20px 20px'}
            ),

            # html.H4('Choose X Indicator', style={'font-size':'100%', 'text-align':'center', 'color': 'white'}),
            # dcc.Dropdown(
            #     id='xaxis-dropdown',
            #     value=[],
            #     # value=['Human Development Index'],
            #     options=[{'label': n, 'value': n} for n in df8],
            #     clearable=False,
            #     placeholder="Choose X Indicator",
            #     style={'font-size':'90%', 'padding':'0px 20px 20px 20px'}
            # ),


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
            dcc.Graph(id='line-graph', figure={}, clickData=None, hoverData=None, 
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



    dbc.Row([
        dbc.Col([
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
            # width=9
        dcc.Slider(
            df9['year'].min(),
            df9['year'].max(),
            step=None,
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            id='year-slider'
        ),
        ]),
    ],class_name="row2"
    ),


    dbc.Row(
        dbc.Col(
            dcc.Graph(id='map-graph', figure={}, 
            className='six columns',
                config={
                    'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d']
                }),
            className="map_graph"
    ),class_name="row3"
    ),
]) 

# End of layout
# --------------------------------------------------------------------------------------------------------------------------------------------------------#




# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Connect the Plotly graphs with Dash Components

@app.callback(
    Output('scatter-graph-with-slider', 'figure'),
    Input('year-slider', 'value'),
    Input('yaxis-dropdown', 'value')
)

def update_figure(selected_year, indicator_chosen_yaxis):
    # filtered_df = df[df.Country_name.isin(country_chosen)], df[df.year == selected_year]
    # filtered_df = df[df.Country_name.isin(country_chosen)]
    filtered_df = df[df.year == selected_year]
    fig = px.scatter(filtered_df, x='Country_name', y=indicator_chosen_yaxis,
                        size='Total Population', color='Country_name', size_max=100,
                         labels={
                    "Country_name": "Country Name"
                })

    fig.update_layout(transition_duration=500),
    fig.update_xaxes(visible=False, showticklabels=False),
    fig.layout.plot_bgcolor = 'white'
    fig.update_layout(font_color="black")
    return fig



@app.callback(
    Output(component_id='line-graph', component_property='figure'),
    Input(component_id='country_dropdown', component_property='value'),
    # Input(component_id='xaxis-dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
# def update_graph(country_chosen, indicator_chosen_yaxis, indicator_chosen_xaxis):
def update_graph(country_chosen, indicator_chosen_yaxis):
    dff = df[df.Country_name.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y=indicator_chosen_yaxis, color='Country_name',
                  custom_data=['Country_name', 'Country_code', 'Life Expectancy', 'year'],
                  labels={
                    "year": "Year",
                    "Country_name": "Country Name"
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
        fig2 = px.pie(dff2, values=indicator_chosen_yaxis, names=country_chosen,
                      title=indicator_chosen_yaxis, color='Country_name')
        fig2.update_traces(textposition='inside', textinfo='percent+label+value', showlegend=False)
        fig2.layout.plot_bgcolor = 'white'
        fig2.update_layout(font_color="black")
        return fig2
    else:
        dff2 = df[df.Country_name.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2, values=indicator_chosen_yaxis, names=country_chosen, title=f'{indicator_chosen_yaxis} {hov_year}', color='Country_name')
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
        dff2 = dff2[dff2.year == 2019]
        fig3 = px.choropleth(dff2, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", 
                    color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")  
        fig3.update_traces(showlegend=False)  
        fig3.layout.plot_bgcolor = 'white' 
        fig3.update_layout(font_color="black")
        return fig3
    else:
        dff2 = df[df.Country_name.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig3 = px.choropleth(dff2, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", 
                    color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")  
        fig3.update_traces(showlegend=False)   
        fig3.layout.plot_bgcolor = 'white' 
        fig3.update_layout(font_color="black")
        return fig3

# --------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run_server(debug=True)

