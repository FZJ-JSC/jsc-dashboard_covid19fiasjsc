import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import de_DE

from app import compliance_percentages, initial_fig
from layouts.compliance import *
from layouts.faq import *


LANG = "de"
TEXT = de_DE.compliance


# Faq
general_faq = create_faq("texts/faq/de/general.md", "general-faq", LANG)
compliance_faq = create_faq("texts/faq/de/compliance.md", "compliance-faq", LANG)
    
faq_modal = create_faq_modal(TEXT["general-faq-title"], general_faq,
                             TEXT["compliance-faq-title"], compliance_faq,
                             TEXT["faq-close-btn"], LANG)

# Model explanation
model_explanation = create_model_explanation(TEXT["page-title"], TEXT["model-text"], 
                                             TEXT["toggle-btn"], TEXT["faq-btn"], 
                                             faq_modal, LANG)

# Formgroups
reduction_dropdown = dcc.Dropdown(
    id=f"reduction-dropdown-{LANG}",
    clearable=False,
    options=TEXT["reduction-dropdown"],
    value="025"
)
reduction_formgroup = create_formgroup(TEXT["reduction-dropdown-label"],
                                       TEXT["reduction-dropdown-tooltip"],
                                       reduction_dropdown,
                                       "reduction-dropdown", LANG)

compliance_dropdown = dcc.Dropdown(
    id=f"compliance-dropdown-{LANG}",
    options=[
        {"label": "{}%".format(percentage), "value": percentage}
        for percentage in compliance_percentages[1:]
    ],
    value=[30, 50, 70, 100],
    multi=True
)
compliance_formgroup = create_formgroup(TEXT["compliance-dropdown-label"],
                                        TEXT["compliance-dropdown-tooltip"],
                                        compliance_dropdown,
                                        "compliance-dropdown", LANG)

data_dropdown = dcc.Dropdown(
    id=f"data-dropdown-{LANG}",
    clearable=False,
    searchable=False,
    options=TEXT["data-dropdown"],
    value="It",
    className="optgroup"
)
data_formgroup = create_formgroup(TEXT["data-dropdown-label"],
                                  TEXT["data-dropdown-tooltip"],
                                  data_dropdown,
                                  "data-dropdown", LANG)

# Compliance widgets
acc1 = create_config_accordion_item(TEXT["config-title"], TEXT["config-hint"],
                                    [reduction_formgroup, compliance_formgroup],
                                    "compliance-model-config", LANG)
acc2 = create_config_accordion_item(TEXT["plot-config-title"], TEXT["plot-config-hint"],
                                    [data_formgroup],
                                    "compliance-plot-config", LANG)

compliance_widgets = create_compliance_widgets(acc1, acc2)


# Plots
plot_explanation = create_compliance_plots_explanation("assets/compliance_line_charts_deutsch.svg", 
                                                       "assets/compliance_bar_charts_deutsch.svg",
                                                       TEXT["plot-explanation"], compliance_widgets, LANG)
graph_content = create_compliance_graph_content(TEXT["graph-title"], TEXT["graph-tooltip"],
                                                TEXT["graph-btn-1"], TEXT["graph-btn-2"],
                                                initial_fig, LANG)
barchart_content = create_compliance_barchart_content(TEXT["barcharts-btn-1"], TEXT["barcharts-btn-2"], LANG)

# Layout page
page = create_compliance_page(model_explanation, plot_explanation,
                              TEXT["graph-tab"], TEXT["barcharts-tab"], LANG)