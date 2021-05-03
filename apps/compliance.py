import dash_html_components as html

from layouts.compliance import compliance_content


children = [
    # Page content
    html.Div(
        compliance_content,
        id="compliance"
    )
]