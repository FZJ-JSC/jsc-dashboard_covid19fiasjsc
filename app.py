import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from jupyter_dash import JupyterDash

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

compliance_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

colors = dict()
for i, color in zip(compliance_percentages[1:], px.colors.qualitative.Plotly):
    colors[i] = color

columns = {
    "It": "know active cases",
    "actInfT": "total active cases (includes undetected)",
    "cumCasT": "known cumulative cases",
    "cumInfT": "total cumulative cases (includes undetected)",
    "knownRt": "known recovered cases",
    "Rt": "total recovered cases (includes undetected)",
    "Dt": "deceased",
}

columns_incidence = {
    "It": ["incC", "incN"],
    "actInfT": ["incInfC", "incInfN"],
    "cumCasT": ["incC", "incN"],
    "cumInfT": ["incInfC", "incInfN"],
    "knownRt": ["incKnownRc", "incKnownRn"],
    "Rt": ["incRc", "incRn"],
    "Dt": ["incDc", "incDn"],
}


def update_dataframes(reduction):
    dataframes = dict()
    for i in compliance_percentages:
        df = pd.read_csv("../simdata/compliance/0218_NonCompl_reduction{}_earlyDet_pC{}.csv".format(reduction, i))
        df["days"] = ["Day {}".format(day) for day in range(-92,35)]
        # Need to change df to dict for json serialization
        dataframes[i] = df.to_dict()
    return dataframes


dataframes = update_dataframes("025")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO, FONT_AWESOME])
# app = JupyterDash(__name__, external_stylesheets=[dbc.themes.COSMO, FONT_AWESOME])
app.title = 'Cosimo'

server = app.server

# app.renderer = '''
# var renderer = new DashRenderer({
#     request_pre: (payload) => {},
#     request_post: (payload, response) => {
#         relayout_barcharts();
#     }
# })
# '''

import index