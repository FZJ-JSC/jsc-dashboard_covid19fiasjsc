import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go

from app import *
from dash.dependencies import Input, Output, State
from math import ceil
from numpy import stack
from plotly.subplots import make_subplots


@app.callback(
    [Output("compliance-barcharts", "children"),
     Output("compliance-barcharts-title", "children")],
    [Input("reduction-dropdown", "value"),
     Input("data-dropdown", "value"),
     Input("compliance-dropdown", "value"),
     Input("dataframes", "data")],
    State("dataframes", "data")
)
def update_barcharts(reduction, column, percentages, data, dataframes):
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
                   name="compliant people",
                   hoverinfo='skip',  # Defined in total instead
                   showlegend=True if i == 0 else False),
            row=row, col=col)
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92:],
                   y=dataframes[p][c[1]][92:],
                   marker_color=colors[20],
                   name="noncompliant people",
                   hoverinfo='skip',  # Defined in total instead
                   showlegend=True if i == 0 else False),
            row=row, col=col)

        # Total c+n. Use this for custom hover template.
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92:],
                   y=dataframes[p][c[0]][92:]+dataframes[p][c[1]][92:],
                   marker_color="rgba(0,0,0,0)",  # transparent
                   name="total",
                   base=0,
                   showlegend=False,
                   customdata=stack(
                       (dataframes[p][c[0]][92:], dataframes[p][c[1]][92:]),
                       axis=-1),
                   # Do not remove white spaces in hovertemplate.
                   # They are there for spacing in the rendered template.
                   hovertemplate="""
Daily incidence - %{x}<br>

<span style="color: #636EFA;">&#9724;</span>
 compliant: %{customdata[0]:.3s}<br>

<span style="color: #EF553B;">&#9724;</span>
 non-compliant:  %{customdata[1]:.3s}<br>

<span style="color: rgba(0,0,0,0);">&#9724;</span>
 total: %{y:.3s}

<extra></extra>
"""
                  ),
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
            title_text="Cases among",
            itemclick=False,
            itemdoubleclick=False,
        ),
        margin=dict(l=0, r=0, t=45),
        hovermode="closest",
        hoverlabel=dict(bgcolor="white")
    )
    # Title colors
    for i in range(len(fig["layout"]["annotations"])):
        fig["layout"]["annotations"][i]["font"].update(
            color=colors[percentages[i]])
    # Axes
    fig.update_xaxes(
        # Ticks
        dtick=7,
        ticks="outside",
        tickson="boundaries",
        tickangle=-45,
        ticklen=4,
        # Outline
        mirror=True,
        showline=True,
        linewidth=2,
        # Spike line for hover
        showspikes=True,
        spikemode='across+toaxis',
        spikesnap='data',
        spikedash='dot',
        spikethickness=2
    )
    fig.update_yaxes(
        title="daily incidence",
        # Outline
        mirror=True,
        showline=True,
        linewidth=2
    )

    # Title
    title = "Daily new cases for contact reduction factor {}".format(
        reduction[:1] + "." + reduction[1:])
    return dcc.Graph(figure=fig), title