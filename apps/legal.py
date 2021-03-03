import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def create_legal_page(title, markdown_file):
    with open(markdown_file) as md_file:
        markdown = md_file.read()
    
    return dbc.Card(
        [
            dbc.CardHeader(            
                html.Center(html.H2(title))
            ),
            dbc.CardBody([
    #             html.Hr(),
                dcc.Markdown(markdown)
            ]),
        ],
        className="mb-4"
    )

# Disclaimer
disclaimer = create_legal_page("Disclaimer", "texts/disclaimer.md")

# Impressum
imp = create_legal_page("Impressum", "texts/impressum/impressum.md")
haftung = create_legal_page("Haftungsausschluss", "texts/impressum/haftungsausschluss.md")
hoster = create_legal_page("Hoster", "texts/impressum/hoster.md")
impressum = html.Div([imp, haftung, hoster])

# Datenschutzerklärung
privacy = create_legal_page("Datenschutzerklärung", "texts/datenschutzerklaerung.md")