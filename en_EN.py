# For all elements that contain text which does not get set in callbacks: 
# Map id to English text

with open("./texts/compliance/en/model-short.md") as f:
    compliance_short = f.read()

with open("./texts/compliance/en/reduction-factor.md") as f:
    reduction_tooltip = f.read()
with open("./texts/compliance/en/compliance-level.md") as f:
    compliance_tooltip = f.read()
with open("./texts/compliance/en/plotted-data.md") as f:
    data_tooltip = f.read()
    
with open("./texts/compliance/en/plots-explanation.md") as f:
    compliance_config_explanation = f.read()
with open("./texts/compliance/en/line-plot.md") as f:
    line_plot_explanation = f.read()
with open("./texts/compliance/en/bar-charts.md") as f:
    bar_charts_explanation = f.read()
    
    
compliance = {
    "page-title" : "Compliance model",
    "model-text": compliance_short,
    "toggle-btn": "...more",
    
    "faq-btn": "FAQ",
    "faq-close-btn": "Close",
    "general-faq-title": "General FAQs",
    "compliance-faq-title": "Compliance Model FAQs",
    
    "reduction-dropdown-label": "Intervention Severity",
    "reduction-dropdown-tooltip": reduction_tooltip,
    "reduction-dropdown": [
        {"label": "strict", "value": "025"},
        {"label": "moderate", "value": "05"},
        {"label": "minimal", "value": "08"}
    ],
    "compliance-dropdown-label": "Compliance",
    "compliance-dropdown-tooltip": compliance_tooltip,
    "data-dropdown-label": "Plotted Data",
    "data-dropdown-tooltip": data_tooltip,
    "data-dropdown": [
        {"label": "deceased", "value": "Dt"},
        {"label": "reported cases", "value": "", "disabled": True},
        {"label": "reported active cases", "value": "It"},
        {"label": "reported cumulative cases", "value": "cumCasT"},
        {"label": "reported recovered cases", "value": "knownRt"},
        {"label": "total cases (incl. undetected)", "value": "", "disabled": True},
        {"label": "total active cases", "value": "actInfT"},
        {"label": "total cumulative cases", "value": "cumInfT"},
        {"label": "total recovered cases", "value": "Rt"},
    ],
    
    "config-title": "Modelling Scenario",
    "config-hint": "Please select the contact restriction severity to be introduced and the compliance level in the population.",
    "plot-config-title": "Plot Configuration",
    "plot-config-hint": "Please select simulation data to be visualized.",
    
    "plots-explanation": "Click the pictures for an interpretation guide:",
    "line-plot-explanation-title": "Line plots: state of the epidemic",
    "line-plot-explanation": line_plot_explanation,
    "bar-charts-explanation-title": "Bar plots: daily changes",
    "bar-charts-explanation": bar_charts_explanation,
    "config-explanation": compliance_config_explanation,
    
    "graph-tab": "Selected output",
    "barcharts-tab": "Corresponding daily incidence",
    
    "graph-title": "Visualize known active cases (for strict intervention)",
    "graph-tooltip": "Simulated data before and after introduction of control measures for selected intervention severity and compliance levels.",
    "graph-btn-1": "From start of intervention",
    "graph-btn-2": "From start of simulation",
    
    "barcharts-btn-1": "Daily incidence",
    "barcharts-btn-2": "7 day incidence"
}


other = {
    "about": "About",
    "about-path": "texts/about/en/about.md",
    "team": "Team",
    "team-path": "texts/about/en/team.md",
    "contrib": "Contributions",
    "contrib-path": "texts/about/en/contributions.md",
    
    "impressum": "Impressum",
    "impressum-path": "texts/impressum/en/impressum.md",
    "disclaimer": "Disclaimer",
    "disclaimer-path": "texts/impressum/en/disclaimer.md",
    "hoster": "Hoster",
    "hoster-path": "texts/impressum/en/hoster.md",
    
    "privacy": "Data Protection",
    "privacy-path": "texts/data-protection.md"
}


sidebar = {
    "compliance": "Compliance".upper(),
    "about": "About",
    "impressum": "Legal Disclosure",
    "privacy": "Data Protection"
}