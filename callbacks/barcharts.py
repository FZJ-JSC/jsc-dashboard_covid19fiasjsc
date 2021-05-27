import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objects as go

from app import app, colors
from dash.dependencies import Input, Output
from math import ceil
from numpy import stack
from plotly.subplots import make_subplots


column_mappings = {
    "It": ["incC", "incN"],
    "actInfT": ["incInfC", "incInfN"],
    "cumCasT": ["incC", "incN"],
    "cumInfT": ["incInfC", "incInfN"],
    "knownRt": ["incKnownRc", "incKnownRn"],
    "Rt": ["incRc", "incRn"],
    "Dt": ["incDc", "incDn"],
}

columns_de = {
    "It": "täglich neu gemeldete Fälle",
    "actInfT": "täglich neue infizierte Fälle",
    "cumCasT": "täglich neu gemeldete Fälle",
    "cumInfT": "täglich neue infizierte Fälle",
    "knownRt": "täglich neue Genesungen (gemeldeter Fälle)",
    "Rt": "täglich neue Genesungen",
    "Dt": "täglich neue Tode",
}

severity_de = {
    "025": "strikten",
    "05": "moderaten",
    "08": "minimalen"
}

columns_en = {
    "It": "daily new reported cases",
    "actInfT": "daily new infections",
    "cumCasT": "daily new reported cases",
    "cumInfT": "daily new infections",
    "knownRt": "daily recoveries (from reported infections)",
    "Rt": "daily recoveries",
    "Dt": "daily new deaths",
}

severity_en = {
    "025": "strict",
    "05": "moderate",
    "08": "minimal"
}


for LANG in ["de", "en"]:
    @app.callback(
        Output(f"compliance-barchart-btns-{LANG}", "style"),
        Input(f"data-dropdown-{LANG}", "value")
    )
    def toggle_visibility(column):
        if column == "It":
            return {"display": "flex"}
        else:
            return {"display": "none"}
        
        
    @app.callback(
        Output(f"compliance-barchart-btn-1-{LANG}", "active"),
        Output(f"compliance-barchart-btn-2-{LANG}", "active"),
        Input(f"compliance-barchart-btn-1-{LANG}", "n_clicks"),
        Input(f"compliance-barchart-btn-2-{LANG}", "n_clicks"),
    )
    def toggle_active_button(btn1, btn2):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if "btn-1" in button_id:
            return True, False
        elif "btn-2" in button_id:
            return False, True
        return True, False


###
# German exclusive callbacks
###    
LANG = "de"

@app.callback(
    Output(f"compliance-barcharts-title-{LANG}", "children"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value")
)
def update_barcharts_title_de(reduction, column):
    title = "Number of {} for {} intervention".format(
        columns_de[column], severity_de[reduction])
    return title


@app.callback(
    Output(f"compliance-barcharts-{LANG}", "figure"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value"),
    Input(f"compliance-dropdown-{LANG}", "value"),
    Input(f"dataframes-{LANG}", "data"),
    Input(f"compliance-barchart-btn-2-{LANG}", "active")
)
def update_barcharts_de(reduction, column, percentages, dataframes, btn2):
    for df in dataframes:
        # Keys were changes to str for json, change back to int
        dataframes[int(df)] = pd.DataFrame.from_dict(dataframes.pop(df))
    percentages.append(0)
    percentages.sort()
    c = column_mappings[column]

    rows = ceil((len(percentages))/2)
    titles = ["{}% Compliance".format(p) for p in percentages]
    fig = make_subplots(rows=rows, cols=2, shared_yaxes='all',
                        subplot_titles=titles)

    for i in range(len(percentages)):
        p = percentages[i]
        row = i//2 + 1
        col = 1 if i % 2 == 0 else 2
        
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92-14:],
                   y=dataframes[p][c[0]][92-14:],
                   marker_color=colors[10],
                   name="Compliant",
                   hoverinfo='skip',  # Defined in total instead
                   showlegend=True if i == 0 else False),
            row=row, col=col)
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92-14:],
                   y=dataframes[p][c[1]][92-14:],
                   marker_color=colors[20],
                   name="Non-compliant",
                   hoverinfo='skip',  # Defined in total instead
                   showlegend=True if i == 0 else False),
            row=row, col=col)

        # Total c+n. Use this for custom hover template.
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92-14:],
                   y=dataframes[p][c[0]][92-14:]+dataframes[p][c[1]][92-14:],
                   marker_color="rgba(0,0,0,0)",  # transparent
                   name="Bevölkerung gesamt",
                   base=0,
                   showlegend=False,
                   customdata=stack(
                       (dataframes[p][c[0]][92-14:], dataframes[p][c[1]][92-14:]),
                       axis=-1),
                   # Do not remove white spaces in hovertemplate.
                   # They are there for spacing in the rendered template.
                   hovertemplate="""
Tägliche Inzidenz - %{x}<br>

<span style="color: #636EFA;">&#9724;</span>
 compliant: %{customdata[0]:.3s}<br>

<span style="color: #EF553B;">&#9724;</span>
 non-compliant:  %{customdata[1]:.3s}<br>

<span style="color: rgba(0,0,0,0);">&#9724;</span>
 gesamt: %{y:.3s}

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
            title_text="Fälle für Bevölkerungsanteil",
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
        spikethickness=2,
        # Disable panning in x axis
        fixedrange=True
    )
    fig.update_yaxes(
        title="Tägliche Inzidenz",
        # Outline
        mirror=True,
        showline=True,
        linewidth=2
    )
    return fig
    
    
###
# English exclusive callbacks
###    
LANG = "en"

@app.callback(
    Output(f"compliance-barcharts-title-{LANG}", "children"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value")
)
def update_barcharts_titl_en(reduction, column):
    title = "Number of {} for {} intervention".format(
        columns_en[column], severity_en[reduction])
    return title


@app.callback(
    Output(f"compliance-barcharts-{LANG}", "figure"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value"),
    Input(f"compliance-dropdown-{LANG}", "value"),
    Input(f"dataframes-{LANG}", "data"),
    Input(f"compliance-barchart-btn-2-{LANG}", "active")
)
def update_barcharts_en(reduction, column, percentages, dataframes, btn2):
    for df in dataframes:
        # Keys were changes to str for json, change back to int
        dataframes[int(df)] = pd.DataFrame.from_dict(dataframes.pop(df))
    percentages.append(0)
    percentages.sort()
    c = column_mappings[column]

    rows = ceil((len(percentages))/2)
    titles = ["{}% compliance".format(p) for p in percentages]
    fig = make_subplots(rows=rows, cols=2, shared_yaxes='all',
                        subplot_titles=titles)

    for i in range(len(percentages)):
        p = percentages[i]
        row = i//2 + 1
        col = 1 if i % 2 == 0 else 2

        if column=="It" and btn2==True:
            fig.add_trace(
                go.Bar(x=dataframes[p]["days"][92-14:],
                       y=dataframes[p][c[0]][92-14:]*7/830,
                       marker_color=colors[10],
                       name="compliant people",
                       hoverinfo='skip',  # Defined in total instead
                       showlegend=True if i == 0 else False),
                row=row, col=col)
        else:
            fig.add_trace(
                go.Bar(x=dataframes[p]["days"][92-14:],
                       y=dataframes[p][c[0]][92-14:],
                       marker_color=colors[10],
                       name="compliant people",
                       hoverinfo='skip',  # Defined in total instead
                       showlegend=True if i == 0 else False),
            row=row, col=col)
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92-14:],
                   y=dataframes[p][c[1]][92-14:],
                   marker_color=colors[20],
                   name="noncompliant people",
                   hoverinfo='skip',  # Defined in total instead
                   showlegend=True if i == 0 else False),
            row=row, col=col)

        # Total c+n. Use this for custom hover template.
        fig.add_trace(
            go.Bar(x=dataframes[p]["days"][92-14:],
                   y=dataframes[p][c[0]][92-14:]+dataframes[p][c[1]][92-14:],
                   marker_color="rgba(0,0,0,0)",  # transparent
                   name="total",
                   base=0,
                   showlegend=False,
                   customdata=stack(
                       (dataframes[p][c[0]][92-14:], dataframes[p][c[1]][92-14:]),
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
        spikethickness=2,
        # Disable panning in x axis
        fixedrange=True
    )
    fig.update_yaxes(
        title="Daily incidence",
        # Outline
        mirror=True,
        showline=True,
        linewidth=2
    )
    
    # 7 day incidence
    if column=="It" and btn2==True:
        for bar in fig.data:
            bar.y = bar.y * 3
    
    return fig