import dash
import pandas as pd
import plotly.graph_objects as go

from app import app, colors
from dash.dependencies import Input, Output, State


columns = {
    "It": "reported active cases",
    "actInfT": "total active cases",
    "cumCasT": "reported cumulative cases",
    "cumInfT": "total cumulative cases",
    "knownRt": "reported cumulative recoveries",
    "Rt": "total cumulative recoveries",
    "Dt": "cumulative deaths",
}

severity = {
    "025": "strict",
    "05": "moderate",
    "08": "minimal"
}


@app.callback(
    Output("compliance-graph-title", "children"),
    Input("reduction-dropdown", "value"),
    Input("data-dropdown", "value")
)
def update_chart_title(reduction, column):
    title = "Visualize {} (for {} intervention)".format(
        columns[column], severity[reduction])
    return title


@app.callback(
    Output("compliance-graph-btn-1", "active"),
    Output("compliance-graph-btn-2", "active"),
    Input("compliance-graph-btn-1", "n_clicks"),
    Input("compliance-graph-btn-2", "n_clicks"),
)
def toggle_active_button(btn1, btn2):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "compliance-graph-btn-1":
        return True, False
    elif button_id == "compliance-graph-btn-2":
        return False, True
    return True, False


@app.callback(
    Output("compliance-graph", "figure"),
    Input("reduction-dropdown", "value"),
    Input("data-dropdown", "value"),
    Input("compliance-dropdown", "value"),
    Input("dataframes", "data"),
    Input("compliance-graph-btn-1", "n_clicks"),
    Input("compliance-graph-btn-2", "n_clicks"),
    State("compliance-graph", "figure")
)
def update_chart(reduction, column, percentages, dataframes, btn1, btn2, fig):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Reset axes
    if button_id == "compliance-graph-btn-1":
        fig["layout"]["xaxis"]["range"] = [90-14, 126-14]
        return fig
    # Autoscale
    elif button_id == "compliance-graph-btn-2":
        fig["layout"]["xaxis"]["range"] = [0, 126-14]
        return fig

    for df in dataframes:
        # Keys were changed to str for json, change back to int
        dataframes[int(df)] = pd.DataFrame.from_dict(dataframes.pop(df))
    percentages.sort()

    fig = go.Figure()
    # 0% compliance
    fig.add_trace(go.Scatter(x=dataframes[0]["days"],
                             y=dataframes[0][column],
                             line=dict(color=colors[0]),
                             name="0%", meta="0%",
                             hovertemplate=
                             "%{x}<br>%{y:.3s}" +
                             "<extra>%{meta} compliance</extra>"))
    # Other selected % compliance
    for p in percentages:
        name = "{}%".format(p)
        fig.add_trace(go.Scatter(x=dataframes[p]["days"][(92-14):],
                                 y=dataframes[p][column][(92-14):],
                                 line=dict(color=colors[p]),
                                 name=name, meta=name,
                                 hovertemplate=
                                 "%{x}<br>%{y:.3s}" +
                                 "<extra>%{meta} compliance</extra>"))

    # Vertical line
    fig.add_shape(xref="x", x0=91-14, x1=91-14,
                  yref="paper", y0=0, y1=1, type="line",
                  line=dict(color="grey", dash="dash"))
    # "Begin measures" annotation
    fig.add_annotation(xref="x", x=91-14,
                       text="<b>Start of<br>interventions</b>",
                       align="left",
                       xanchor="left",
                       showarrow=False,
                       font=dict(color="grey"))

    # Layout options
    fig.update_layout(
        height=500,
        legend=dict(title_text="Compliance"),
        margin=dict(l=0, r=0, t=30),
        yaxis_title="Cases"
        # hovermode="x"
    )

    # X axis
    fig.update_xaxes(
        tick0=91-14,
        dtick=7,
        autorange=False,
        range=[90-14, 126-14],
        ticks="outside",
        tickangle=-45,
        ticklen=4
    )

    return fig


