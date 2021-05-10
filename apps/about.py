import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# from layouts.about import about_content

def create_about_page(title, markdown_file, margin=""):
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
        className=margin
    )

about = create_about_page("About", "texts/about/en/about.md", "mb-4")
team = create_about_page("Team", "texts/about/en/team.md", "mb-4")
contributions = create_about_page("Contributions", "texts/about/en/contributions.md")

children = [about, team, contributions]