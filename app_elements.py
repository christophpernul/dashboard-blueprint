"""
This file defines all HTML elements, that are used in the main app on all tabs.
It imports data and app from app.py (for callbacks)
"""
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

### Load the data, that was prepared at initialization
from app import app, data
import data_lib as dl
import plotting_lib as pl

def cardify_element(function):
    ### Decorator, that wraps the called function (which renders the HTML element) inside a dbc.Card
    def inner(*args, **kwargs):
        cardified_element = \
            dbc.Card(
                dbc.CardBody(
                    function(*args, **kwargs)
                )
            )
        return(cardified_element)
    return(inner)

@cardify_element
def dbc_column(element):
    return(dbc.Col(element))

def render_tab1(tab_title, kpi_title):
    avg = dl.get_average(data)
    heading = \
        dbc.Col(
            dbc_column(html.H1(html.B(tab_title))),
            width=6,
            align='center'
        )
    kpi_box = \
        html.Div(
            dbc.Row(
                [dbc.Col(html.H2(kpi_title)),
                 dbc.Col(html.H2(str(round(avg, 2))))],
                justify='around'
            ),
        )
    kpi_panel = dbc.Col(dbc_column(html.Div([kpi_box])),
                        width=6,
                        align='center'
                )

    header_panel = dbc.Row([heading, kpi_panel], justify='around')
    return(html.Div([header_panel]))

def render_tab2():
    dropdown_element = dcc.Dropdown(options=[
                                            {"label": "Linear function", "value": "y"},
                                            {"label": "Bessel function y1(x)", "value": "z"}
                                            ],
                                    value="z",
                                    id="dropdown"
    )
    graph_element = html.Div(id="graph")
    body = dbc.Row([
                dbc.Col(dropdown_element,
                        width=4,
                        align='center'
                        ),
                dbc.Col(graph_element,
                        width=8,
                        align='center'
                        )
            ],
                justify='around'
            )

    return(html.Div([body]))

########################################### CALLBACK FUNCTIONS #########################################################
# These callback functions need to be defined outside of the function, which uses it, because
# all callbacks need to be defined when the app is started!
@app.callback(Output('graph', 'children'),
              Input('dropdown', 'value')
              )
def dropdown_timeseries_chart(column: str):
    """
    Get the content element for the chart for the given dropdown selection.
    """
    html_div = pl.render_linechart(column)
    return (html_div)