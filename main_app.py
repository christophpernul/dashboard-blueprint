"""
This is the main app. Here we define our app structure. We load the corresponding HTML elements from
another python library app_elements.
"""
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
import app_elements

tab_nav_bar = \
            dbc.Tabs(id="tab-navbar",
                     active_tab="tab-1",
                     children=[
                                dbc.Tab(label="First Tab", tab_id="tab-1"),
                                dbc.Tab(label="Second Tab", tab_id="tab-2")
                              ],
                     card=True
                    )

body = [dbc.CardHeader(tab_nav_bar),
        dbc.CardBody(html.Div(id="tab-content"))
]

app.layout = dbc.Card(body)

@app.callback(Output('tab-content', 'children'),
              Input('tab-navbar', 'active_tab'))
def switch_tabs(tab):
    if tab == "tab-1":
        html_element = app_elements.render_tab1(tab_title="KPI Element",
                                                kpi_title="Average y")
        return(html_element)
    elif tab == "tab-2":
        html_element = app_elements.render_tab2()
        return(html_element)

if __name__ == '__main__':
    app.run_server(debug=True)