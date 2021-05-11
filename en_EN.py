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
    compliance_plot_explanation = f.read()
    
    
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
        {"label": "active", "value": "It"},
        {"label": "cumulative", "value": "cumCasT"},
        {"label": "recovered", "value": "knownRt"},
        {"label": "total cases (incl. undetected)", "value": "", "disabled": True},
        {"label": "active", "value": "actInfT"},
        {"label": "cumulative", "value": "cumInfT"},
        {"label": "recovered", "value": "Rt"},
    ],
    
    "config-title": "Modelling Scenario",
    "config-hint": "Please select the contact restriction severity to be introduced and the compliance level in the population.",
    "plot-config-title": "Plot Configuration",
    "plot-config-hint": "Please select simulation data to be visualized.",
    
    "plot-explanation": compliance_plot_explanation,
    
    "graph-tab": "Selected output",
    "barcharts-tab": "Corresponding daily incidence",
    
    "graph-title": "Visualize known active cases (for contact reduction factor 0.25)",
    "graph-tooltip": "Simulated data before and after introduction of control measures for selected intervention severity and compliance levels.",
    "graph-btn-1": "From start of intervention",
    "graph-btn-2": "From start of simulation"
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