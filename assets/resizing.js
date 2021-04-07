var HEIGHT = 300;

function relayout_plots() {    
    
    let graph = document.getElementById('compliance-graph');
    
    // Do not have upper plot
    if (graph == null) {
        // Check for barchart plot
        graph = document.getElementById('compliance-barcharts');
        // No barchart plot either
        if (graph == null) return;
        
        let plot = document.getElementsByClassName('js-plotly-plot')[0];        
        let data = plot.data;        
        let layout = plot.layout;
        let config = {responsive: true};
        
        var rows = data.length / 3;
        var i = 1;
        
        if (window.innerWidth < 992) {
            // Single column barcharts
            let vertical_spacing = 0.5 / rows;
            let height = (1 - vertical_spacing * (rows - 1)) / rows;
            let annotation_y_spacing = vertical_spacing + height;

            for (var key in layout) {
                // Move subtitles
                if (layout.hasOwnProperty(key) && key.startsWith('annotations')) {
                    for (let y in layout[key]) {
                        layout[key][y].x = 0.5;
                        layout[key][y].y = 1 - y * annotation_y_spacing;
                    }
                }
                // Change x and y positions of individual bar charts
                if (layout.hasOwnProperty(key) && key.startsWith('x')) {
                    layout[key].domain = [0,1];
                }
                if (layout.hasOwnProperty(key) && key.startsWith('y')) {
                    layout[key].domain = [i-height, i];
                    i = i - height - vertical_spacing;
                }
            }
            layout.height = HEIGHT * rows;
            layout.legend.orientation = "h";
            layout.legend.xanchor = "right";
            layout.legend.x = 1;
            layout.legend.yanchor = "bottom";
            layout.legend.y = 1.02;
            // Add padding
            document.getElementById('compliance-barcharts').className = "w-1 pt-3"
        }
        else {
            // 2 column barcharts
            rows = Math.ceil(rows/2);
            let vertical_spacing = 0.5 / rows;        
            let height = (1 - vertical_spacing * (rows - 1)) / rows;
            let annotation_y_spacing = vertical_spacing + height;
            let l = 0; let k = 0;

            for (var key in layout) {
                // Move subtitles
                if (layout.hasOwnProperty(key) && key.startsWith('annotations')) {
                    for (let y in layout[key]) {
                        layout[key][y].x = (y % 2 == 0) ? 0.225 : 0.775;
                        layout[key][y].y = 1 - Math.floor(y/2) * annotation_y_spacing;
                    }
                }
                // Change x and y positions of individual bar charts
                if (layout.hasOwnProperty(key) && key.startsWith('x')) {
                    layout[key].domain = (l % 2 == 0) ? [0,0.45] : [0.55, 1];
                    l++;
                }
                y = 0;
                if (layout.hasOwnProperty(key) && key.startsWith('y')) {
                    layout[key].domain = [i-height, i];
                    k++;
                    if (k % 2 == 0) {
                        i = i - height - vertical_spacing;
                    }
                }
            }
            layout.height = HEIGHT * rows;
            layout.legend.orientation = "v";
            layout.legend.xanchor = "left";
            layout.legend.x = 1.02;
            layout.legend.yanchor = "auto";
            layout.legend.y = 1;
            // Remove padding
            document.getElementById('compliance-barcharts').className = "w-1"
        }
        
        Plotly.newPlot(plot, data, layout, config);
    } 
    
    // Relayout upper plot
    else {
        let plot = document.getElementsByClassName('js-plotly-plot')[0];
        let data = plot.data; 
        let layout = plot.layout;
        let config = {responsive: true};
        
        if (window.innerWidth < 992) {
            layout.legend.orientation = "h";
            layout.legend.xanchor = "right";
            layout.legend.x = 1;
            layout.legend.yanchor = "bottom";
            layout.legend.y = 1.02;
            // Add padding
            document.getElementById('compliance-graph').className = "dash-graph w-1 pt-3"
        }
        else {
            layout.legend.orientation = "v";
            layout.legend.xanchor = "left";
            layout.legend.x = 1.02;
            layout.legend.yanchor = "auto";
            layout.legend.y = 1;
            // Remove padding
            document.getElementById('compliance-graph').className = "dash-graph w-1"
        }
        
        Plotly.newPlot(plot, data, layout, config);
    }
}

window.onresize = relayout_plots;

if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {
    resize: function(value) {
        window.dispatchEvent(new Event("resize"));
        return null;
    },
};