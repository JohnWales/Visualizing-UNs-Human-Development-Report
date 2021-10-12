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
response = requests.get("http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/country_code=AFG,ZWE/indicator_id=103206,103606,103706/year=1990,2000,2019/structure=ciy")
df1 = response.json()



categories=["observation_time","temperature","wind_speed","precip","humidity",
            "cloudcover","feelslike","uv_index","visibility"]


def api():
    api_requests = requests.get(
        "http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=137506"
        #"http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/country_code=AFG,ZWE/indicator_id=103206,103606,103706/year=1990,2000,2019/structure=ciy"
          )
    json_data = api_requests.json()
    df = pd.DataFrame(json_data)



    print("\n")
    print (df.columns)
    print("\n")

    #print (df.iloc[0][0])

    x = 0
    #print(df["indicator_value"][x]["137506"].values())      # List of all HDI values for Afghanistan
    #print(df["indicator_value"][x]["137506"].keys())        # List of all Years
    print(df["indicator_value"][x]["137506"])
    #year = df["indicator_value"][x]["137506"].keys()
    #years_list = []
    #while x < 1:
    #    years_list.append(year)
    #    x = x + 1

    #print(years_list)



api()


# --------------------------------------------------------------------------------------------------------- #
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'})    
    
    ])



# --------------------------------------------------------------------------------------------------------- #
#if __name__ == '__main__':
#    app.run_server(debug=True)




