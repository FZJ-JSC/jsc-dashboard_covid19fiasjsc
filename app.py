import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

compliance_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

colors = dict()
for i, color in zip(compliance_percentages[1:], px.colors.qualitative.Plotly):
    colors[i] = color

columns = {
    "It": "Aktive Fälle",
    "actInfT": "Tatsächliche Anzahl aktiver Fälle",
    "cumCasT": "Kumulierte Fälle",
    "cumInfT": "Tatsächliche Anzahl kumulierter Fälle",
    "knownRt": "Bekannte genesene Fälle",
    "Rt": "Tatsächliche genesene Fälle",
    "Dt": "Verstorbene",
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

columns_incidence_titles = {
    "It": "aktiven Fällen",
    "actInfT": "tatsächlichen aktiven Fällen",
    "cumCasT": "kumulierten Fällen",
    "cumInfT": "tatsächlichen kumulierten Fällen",
    "knownRt": "bekannten genesenen Fällen",
    "Rt": "tatsächlichen genesenen Fällen",
    "Dt": "verstorbenen Fällen",
}


def update_dataframes(reduction):
    dataframes = dict()
    for i in compliance_percentages:
        df = pd.read_csv("./large_csv/0218_NonCompl_reduction{}_earlyDet_pC{}.csv".format(reduction, i))
        df["days"] = ["Tag {}".format(day) for day in range(-92,35)]
        # Need to change df to dict for json serialization
        dataframes[i] = df.to_dict()
    return dataframes


dataframes = update_dataframes("025")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO, FONT_AWESOME])
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