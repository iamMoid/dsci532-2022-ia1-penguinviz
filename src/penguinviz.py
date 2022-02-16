import pandas as pd
import altair as alt
from dash import Dash, dcc, html, Input, Output
from palmerpenguins import load_penguins

penguins = load_penguins()
print(penguins)

def plot_altair(xcol, ycol):
    plot = alt.Chart(
            data = penguins   
        ).encode(
            x = xcol,
            y = ycol
        ).mark_point()
    return plot.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        dcc.Dropdown(
            id='xcol',
            value='bill_length_mm',
            options=[{'label': i, 'value': i} for i in penguins.columns]),
        dcc.Dropdown(
            id='ycol',
            value='bill_depth_mm',
            options=[{'label': i, 'value': i} for i in penguins.columns]),
        html.Iframe(
            id='scatterplot',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            srcDoc=plot_altair(xcol, ycol)
        ])
        
@app.callback(
    Output('scatterplot', 'srcDoc'),
    Input('xslider', 'value'))
def update_output(xcol, ycol):
    return plot_altair(xcol, ycol)

if __name__ == '__main__':
    app.run_server(debug=True)