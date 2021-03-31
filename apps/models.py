import dash_html_components as html

from layouts.models import models_selection, models_explanation
from layouts.compliance import compliance_content


children = [
    # Navigation between models
#     models_selection,
    # Model explanation
    models_explanation,
    # Page content
    html.Div(
        compliance_content,
        id="model-content"
    )
]