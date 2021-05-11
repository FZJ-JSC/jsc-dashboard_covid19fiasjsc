import dash_html_components as html
from layouts.other_pages import create_page
import en_EN


LANG = "en"
TEXT = en_EN.other


# About
about = create_page(TEXT["about"], TEXT["about-path"], "about-main", LANG, "mb-4")
team = create_page(TEXT["team"], TEXT["team-path"], "about-team", LANG, "mb-4")
contributions = create_page(TEXT["contrib"], TEXT["contrib-path"], "about-contributions", LANG)
about_page = html.Div([about, team, contributions])


# Impressum
impressum = create_page(TEXT["impressum"], TEXT["impressum-path"], "impressum", LANG, "mb-4")
haftung = create_page(TEXT["disclaimer"], TEXT["disclaimer-path"], "disclaimer", LANG, "mb-4")
hoster = create_page(TEXT["hoster"], TEXT["hoster-path"], "hoster", LANG)
impressum_page = html.Div([impressum, haftung, hoster])


# Datenschutzerklärung
privavy = create_page(TEXT["privacy"], TEXT["privacy-path"], "data-protection", LANG)
privacy_page = html.Div([privavy])
