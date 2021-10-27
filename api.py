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


api_requests = requests.get(
    "http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=137506"
    #"http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/country_code=AFG,ZWE/indicator_id=103206,103606,103706/year=1990,2000,2019/structure=ciy"
        )
json_data = api_requests.json()
df = pd.DataFrame(json_data)



print("\n")
print (df.columns)
print("\n")



# List of all years and values
def years_and_values():
    x = 0
    list = []
    while x < 189:
        list.append(df["indicator_value"][x]["137506"])
        x += 1
    return list[0]
years_and_values()


# List of all the HDI values for every country
def hdi_values():
    y = 0
    values_list = []
    while y < 189:
        values_list.append(df["indicator_value"][y]["137506"].values())
        y += 1
    return list(values_list[0])
hdi_values()


# List of all countries. This can be used for the Y-axis
countries = df['country_name'].values
#print(countries)

# List of all the years. X-axis
years = df["indicator_value"][0]["137506"].keys()
years = list(years)
#print(years)




# --------------------------------------------------------------------------------------------------------- #
# App layout
# API call -> GET -> return json object
#data = json.obj
#gdp = pop-data.gdp //list
# life_exp = data.leftex //list

# for val in gdp":
# for val2 in life_expo


df1 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
df2 = pd.DataFrame( {
    "AFG": {"1990":"0.302",
                "1991": 0.307,
                "1992": 0.316,
                "1993": 0.312,
                "1994": 0.307,
                "1995": 0.331,
                "1996": 0.335,
                "1997": 0.339,
                "1998": 0.344,
                "1999": 0.348,
                "2000": 0.35,
                "2001": 0.353,
                "2002": 0.384,
                "2003": 0.393,
                "2004": 0.409,
                "2005": 0.418,
                "2006": 0.429,
                "2007": 0.447,
                "2008": 0.447,
                "2009": 0.46,
                "2010": 0.472,
                "2011": 0.477,
                "2012": 0.489,
                "2013": 0.496,
                "2014": 0.5,
                "2015": 0.5,
                "2016": 0.502,
                "2017": 0.506,
                "2018": 0.509,
                "2019": 0.511},
    "AGO": {"1999":"0.391",
                "2000": 0.4,
                "2001": 0.41,
                "2002": 0.426,
                "2003": 0.435,
                "2004": 0.446,
                "2005": 0.46,
                "2006": 0.473,
                "2007": 0.489,
                "2008": 0.501,
                "2009": 0.515,
                "2010": 0.517,
                "2011": 0.533,
                "2012": 0.544,
                "2013": 0.555,
                "2014": 0.565,
                "2015": 0.572,
                "2016": 0.578,
                "2017": 0.582,
                "2018": 0.582,
                "2019": 0.581}
})

df6 = pd.read_csv('2020_data/Table 2-Table 1.csv')

fig = px.scatter(df6, x="2019", y="Country",
size="2019", color="Country", hover_name="Country",
                  log_x=True, size_max=20
                )

app.layout = html.Div([
    dcc.Graph(
        id='country-vs-2019',
        figure=fig
    )
])

#    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'})


# df6 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# fig = px.scatter(df6, x="gdp per capita", y="life expectancy",
#                  size="population", color="continent", hover_name="country",
#                  log_x=True, size_max=60)

# app.layout = html.Div([
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])

# --------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    app.run_server(debug=True)


