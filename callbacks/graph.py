import pandas as pd
import plotly.graph_objects as go

from app import *
from dash.dependencies import Input, Output, State


@app.callback(
    [Output("graph", "figure"),
     Output("graph-title", "children")],
    [Input("reduction-dropdown", "value"),
     Input("column-dropdown", "value"),
     Input("compliance-dropdown", "value")],
    State("dataframes", "data")
)
def update_chart(reduction, column, percentages, dataframes):
    for df in dataframes:
        # Keys were changes to str for json, change back to int
        dataframes[int(df)] = pd.DataFrame.from_dict(dataframes.pop(df))
    percentages.sort()

    fig = go.Figure()
    # 0% compliance
    fig.add_trace(go.Scatter(x=dataframes[0]["days"],
                             y=dataframes[0][column],
                             line=dict(color="black"),
                             name="0%", meta="0%",
                             hovertemplate=
                             "%{x}<br>Fälle: %{y:.3s}" +
                             "<extra><br>%{meta} compliance</extra>"))
    # Other selected % compliance
    for p in percentages:
        name = "{}%".format(p)
        fig.add_trace(go.Scatter(x=dataframes[p]["days"][92:],
                                 y=dataframes[p][column][92:],
                                 line=dict(color=colors[p]),
                                 name=name, meta=name,
                                 hovertemplate=
                                 "%{x}<br>Fälle: %{y:.3s}" +
                                 "<extra><br>%{meta} compliance</extra>"))

    # Vertical line
    fig.add_shape(xref="x", x0=92, x1=92,
                  yref="paper", y0=0, y1=1, type="line",
                  line=dict(color="grey", dash="dash"))
    # "Begin measures" annotation
    fig.add_annotation(xref="x", x=92,
                       text="<b>Start<br>Interventionen</b>",
                       align="left",
                       xanchor="left",
                       showarrow=False,
                       font=dict(color="grey"))

    # Layout options
    fig.update_layout(
        height=500,
        legend=dict(title_text="Compliance"),
        margin=dict(l=0, r=0, t=30),
        # hovermode="x"
    )

    # X axis
    fig.update_xaxes(
        tick0=92,
        dtick=7,
        autorange=False,
        range=[91, 126],
        ticks="outside",
        tickson="boundaries",
        tickangle=-45,
        ticklen=4
    )

    title = "{} für einen Reduktionsfaktor von {}".format(
        columns[column], reduction[:1] + "." + reduction[1:])
    return fig, title