"""
This library is used to do all data plotting. It imports preprocessed data from app.py
"""
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app import data

theme_colors={'background': "#32383E", 'text': "#FFFFFF"}

def render_linechart(column):
    fig = px.line(data, x='x', y=column)
    fig.update_traces(mode="lines")
    fig.update_layout(xaxis_title="x",
                      yaxis_title="f(x)",
                      font_size=25,
                      plot_bgcolor=theme_colors['background'],
                      paper_bgcolor=theme_colors['background'],
                      font_color=theme_colors['text'],
                      height=720
                      )
    content = html.Div(
        dcc.Graph(
            figure=fig
        )
    )
    return(content)