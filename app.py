import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from jupyter_dash import JupyterDash


FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

compliance_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

colors = {0: "#000000"}
for i, color in zip(compliance_percentages[1:], px.colors.qualitative.Plotly):
    colors[i] = color


def update_dataframes(reduction):
    dataframes = dict()
    for i in compliance_percentages:
        df = pd.read_csv("../simdata/compliance/0218_NonCompl_reduction{}_earlyDet_pC{}.csv".format(reduction, i))
        df["days"] = ["Day {}".format(day) for day in range(-91, 36)]
        # Need to change df to dict for json serialization
        dataframes[i] = df[14:].to_dict()
    return dataframes


dataframes = update_dataframes("025")


# Create first graph
# Change dataframes back to pandas dfs
for df in dataframes:
    dataframes[df] = pd.DataFrame.from_dict(dataframes.pop(df))

initial_fig = go.Figure()
# 0% compliance
initial_fig.add_trace(
    go.Scatter(
        x=dataframes[0]["days"],
        y=dataframes[0]["It"],
        line=dict(color="black"),
        name="0%", meta="0%",
        hovertemplate=
        "%{x}<br>%{y:.3s}" +
        "<extra>%{meta} compliance</extra>"
    )
)
for p in [30, 50, 70, 100]:
    name = "{}%".format(p)
    initial_fig.add_trace(
        go.Scatter(
            x=dataframes[p]["days"][92-14:],
            y=dataframes[p]["It"][92-14:],
            line=dict(color=colors[p]),
            name=name, meta=name,
            hovertemplate=
            "%{x}<br>%{y:.3s}" +
            "<extra>%{meta} compliance</extra>"
        )
    )
# Vertical line
initial_fig.add_shape(
    xref="x", x0=91-14, x1=91-14,
    yref="paper", y0=0, y1=1,
    type="line", line=dict(color="grey", dash="dash")
)
# "Begin measures" annotation
initial_fig.add_annotation(
    xref="x", x=91-14,
    text="<b>Start of<br>interventions</b>",
    align="left", xanchor="left",
    showarrow=False, font=dict(color="grey")
)
# Layout options
initial_fig.update_layout(
    height=500,
    legend=dict(title_text="Compliance"),
    margin=dict(l=0, r=0, t=30),
    yaxis_title="Cases"
)
# X axis
initial_fig.update_xaxes(
    tick0=91-14, dtick=7,
    autorange=False, range=[90-14, 126-14],
    ticks="outside", tickson="boundaries",
    tickangle=-45, ticklen=4
)


# Set dataframes back to json
dataframes = update_dataframes("025")


# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO, FONT_AWESOME])
app = JupyterDash(__name__, external_stylesheets=[dbc.themes.COSMO, FONT_AWESOME])
app.title = 'CoSiMo - Covid Simulation and Modeling Project'

server = app.server


import index