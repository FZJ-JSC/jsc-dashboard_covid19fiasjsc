import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go

from app import *
from dash.dependencies import Input, Output, State
from math import ceil
from plotly.subplots import make_subplots


@app.callback(
    [Output("barcharts", "children"),
     Output("barcharts-title", "children")],
    [Input("reduction-dropdown", "value"),
     Input("column-dropdown", "value"),
     Input("compliance-dropdown", "value")],
    State("dataframes", "data")
)
def update_barcharts(reduction, column, percentages, dataframes):
    for df in dataframes:
        # Keys were changes to str for json, change back to int
        dataframes[int(df)] = pd.DataFrame.from_dict(dataframes.pop(df))
    percentages.sort()
    c = columns_incidence[column]

    rows = ceil((len(percentages))/2)
    titles = ["{}% compliance".format(p) for p in percentages]
    fig = make_subplots(rows=rows, cols=2, shared_yaxes='all',
                        subplot_titles=titles)

    for i in range(len(percentages)):
        p = percentages[i]
        row = i//2 + 1
        col = 1 if i % 2 == 0 else 2
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92:],
                   y=dataframes[p][c[0]][92:],
                   marker_color=colors[10],
                   name="compliant population",
                   hovertemplate="%{y:.3s}",
                   showlegend=True if i == 0 else False),
            row=row, col=col)
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92:],
                   y=dataframes[p][c[1]][92:],
                   marker_color=colors[20],
                   name="noncompliant population",
                   hovertemplate="%{y:.3s}",
                   showlegend=True if i == 0 else False),
            row=row, col=col)
        # Total c+n. Add for total number in hover.
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92:],
                   y=dataframes[p][c[0]][92:]+dataframes[p][c[1]][92:],
                   marker_color="rgba(0,0,0,0)",  # transparent
                   name="total",
                   base=0,
                   hovertemplate="%{y:.3s}",
                   showlegend=False),
            row=row, col=col)

        # Set individual colors for border depending on percentage.
        rgb_tuple = tuple(int(colors[p][i:i+2], 16) for i in (1, 3, 5))
        rgba_color = "rgba({},{},{},0.8)".format(*rgb_tuple)
        fig.update_xaxes(linecolor=rgba_color, row=row, col=col)
        fig.update_yaxes(linecolor=rgba_color, row=row, col=col)

    # Layout
    fig.update_layout(
        height=300*rows,
        barmode="relative",
        legend=dict(
            title_text="Population",
            # yanchor="bottom", y=1.02,
            # xanchor="right", x=1,
            itemclick=False,
            itemdoubleclick=False,
        ),
        margin=dict(l=0, r=0, t=45),
        hovermode="x unified"
    )
    # Title colors
    for i in range(len(fig["layout"]["annotations"])):
        fig["layout"]["annotations"][i]["font"].update(
            color=colors[percentages[i]])
    # Axes
    fig.update_xaxes(
        dtick=7,
        ticks="outside",
        tickson="boundaries",
        tickangle=-45,
        ticklen=4,
        # Outline
        mirror=True,
        showline=True,
        linewidth=2,
    )
    fig.update_yaxes(
        # Outline
        mirror=True,
        showline=True,
        linewidth=2
    )

    # Title
    column_text = columns_incidence_titles[column]
    title = "Tägliche Zahl an {} für einen Reduktionsfaktor von {}".format(
        column_text, reduction[:1] + "." + reduction[1:])
    return dcc.Graph(figure=fig), title