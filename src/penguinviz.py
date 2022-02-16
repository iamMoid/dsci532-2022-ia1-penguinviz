import pandas as pd
import altair as alt
from dash import Dash, dcc, html, Input, Output
from palmerpenguins import load_penguins

penguins = load_penguins()

def plot_altair(xcol, ycol, ccol):
    plot = alt.Chart(
            data = penguins   
        ).encode(
            x = xcol,
            y = ycol,
            color = ccol
        ).mark_point()
    return plot.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        html.Iframe(
            id='scatterplot',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair(xcol='bill_length_mm',
                               ycol='bill_depth_mm',
                               ccol='species')),
        dcc.Dropdown(
            id='xcol',
            value='bill_length_mm',
            options=[{'label': i, 'value': i} for i in list(set(penguins.columns.values) - set(['species', 'island', 'sex']))]),
        dcc.Dropdown(
            id='ycol',
            value='bill_depth_mm',
            options=[{'label': i, 'value': i} for i in list(set(penguins.columns.values) - set(['species', 'island', 'sex']))]),
        dcc.Dropdown(
            id='ccol',
            value='species',
            options=[{'label': i, 'value': i} for i in ['species', 'island', 'sex']])
        ])
        
@app.callback(
    Output('scatterplot', 'srcDoc'),
    Input('xcol', 'value'),
    Input('ycol', 'value'),
    Input('ccol', 'value')
    )
def update_output(xcol, ycol, ccol):
    return plot_altair(xcol, ycol, ccol)

if __name__ == '__main__':
    app.run_server(debug=True)