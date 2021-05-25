import dash
import pandas as pd
import plotly.graph_objects as go

from app import app, colors
from dash.dependencies import Input, Output, State


columns_de = {
    "It": "gemeldete aktive Fälle",
    "actInfT": "aktive Fälle (gesamt)",
    "cumCasT": "gemeldete kumulierte Fälle",
    "cumInfT": "kumulierte Fälle (gesamt)",
    "knownRt": "gemeldete genesene Fälle",
    "Rt": "genesene Fälle (gesamt)",
    "Dt": "kumulierte Anzahl Verstorbener ",
}

severity_de = {
    "025": "strikten",
    "05": "moderaten",
    "08": "minimalen"
}

columns_en = {
    "It": "reported active cases",
    "actInfT": "total active cases",
    "cumCasT": "reported cumulative cases",
    "cumInfT": "total cumulative cases",
    "knownRt": "reported cumulative recoveries",
    "Rt": "total cumulative recoveries",
    "Dt": "cumulative deaths",
}

severity_en = {
    "025": "strict",
    "05": "moderate",
    "08": "minimal"
}


for LANG in ["de", "en"]:
    @app.callback(
        Output(f"compliance-graph-btn-1-{LANG}", "active"),
        Output(f"compliance-graph-btn-2-{LANG}", "active"),
        Input(f"compliance-graph-btn-1-{LANG}", "n_clicks"),
        Input(f"compliance-graph-btn-2-{LANG}", "n_clicks"),
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
    Output(f"compliance-graph-title-{LANG}", "children"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value")
)
def update_chart_title_de(reduction, column):
    title = "Visualisiere {} (im Falle einer {} Intervention) ".format(
        columns_de[column], severity_de[reduction])
    return title


@app.callback(
    Output(f"compliance-graph-{LANG}", "figure"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value"),
    Input(f"compliance-dropdown-{LANG}", "value"),
    Input(f"dataframes-{LANG}", "data"),
    Input(f"compliance-graph-btn-1-{LANG}", "n_clicks"),
    Input(f"compliance-graph-btn-2-{LANG}", "n_clicks"),
    State(f"compliance-graph-{LANG}", "figure")
)
def update_chart_de(reduction, column, percentages, dataframes, btn1, btn2, fig):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Reset axes
    if "btn-1" in button_id:
        fig["layout"]["xaxis"]["range"] = [90-14, 126-14]
        return fig
    # Autoscale
    elif "btn-2" in button_id:
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
                             "<extra>%{meta} Compliance</extra>"))
    # Other selected % compliance
    for p in percentages:
        name = "{}%".format(p)
        fig.add_trace(go.Scatter(x=dataframes[p]["days"][(92-14):],
                                 y=dataframes[p][column][(92-14):],
                                 line=dict(color=colors[p]),
                                 name=name, meta=name,
                                 hovertemplate=
                                 "%{x}<br>%{y:.3s}" +
                                 "<extra>%{meta} Compliance</extra>"))

    # Vertical line
    fig.add_shape(xref="x", x0=91-14, x1=91-14,
                  yref="paper", y0=0, y1=1, type="line",
                  line=dict(color="grey", dash="dash"))
    # "Begin measures" annotation
    fig.add_annotation(xref="x", x=91-14,
                       text="<b>Start der<br>Intervention</b>",
                       align="left",
                       xanchor="left",
                       showarrow=False,
                       font=dict(color="grey"))

    # Layout options
    fig.update_layout(
        height=500,
        legend=dict(title_text="Compliance"),
        margin=dict(l=0, r=0, t=30),
        yaxis_title="Fälle"
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


###
# English exclusive callbacks
###
LANG = "en"

@app.callback(
    Output(f"compliance-graph-title-{LANG}", "children"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value")
)
def update_chart_title_en(reduction, column):
    title = "Visualize {} (for {} intervention)".format(
        columns_en[column], severity_en[reduction])
    return title


@app.callback(
    Output(f"compliance-graph-{LANG}", "figure"),
    Input(f"reduction-dropdown-{LANG}", "value"),
    Input(f"data-dropdown-{LANG}", "value"),
    Input(f"compliance-dropdown-{LANG}", "value"),
    Input(f"dataframes-{LANG}", "data"),
    Input(f"compliance-graph-btn-1-{LANG}", "n_clicks"),
    Input(f"compliance-graph-btn-2-{LANG}", "n_clicks"),
    State(f"compliance-graph-{LANG}", "figure")
)
def update_chart_en(reduction, column, percentages, dataframes, btn1, btn2, fig):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Reset axes
    if "btn-1" in button_id:
        fig["layout"]["xaxis"]["range"] = [90-14, 126-14]
        return fig
    # Autoscale
    elif "btn-2" in button_id:
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