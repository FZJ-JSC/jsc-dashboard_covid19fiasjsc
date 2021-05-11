import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def create_page(title, file, component_name, LANG, margin=""):
    with open(file) as f:
        text = f.read()
        
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Center(
                    html.H2(title, id=f"{component_name}-title-{LANG}")
                )
            ),
            dbc.CardBody([
                dcc.Markdown(text, id=f"{component_name}-text-{LANG}")
            ]),
        ],
        className=margin
    )