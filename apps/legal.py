import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

def create_legal_page( markdown_file):
    with open(markdown_file) as md_file:
        markdown = md_file.read()
    
    return dbc.Card(
        dbc.CardBody(dcc.Markdown(markdown))
    )

# Disclaimer
disclaimer = create_legal_page("texts/disclaimer.md")

# Impressum
impressum = create_legal_page("texts/impressum.md")

# Datenschutzerklärung
privacy = create_legal_page("texts/datenschutzerklaerung.md")