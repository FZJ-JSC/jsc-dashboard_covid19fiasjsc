var HEIGHT = 300;

function relayout_barcharts() {
    
    let graphs = document.getElementsByClassName('js-plotly-plot');
    if (graphs.length == 0) {
        // No plots on page
        return;
    }
    let graph = graphs[0];
    let graph_data = graph.data;
    let graph_layout = graph.layout;    
    let barcharts = graphs[1];
    let data = barcharts.data;
    let layout = barcharts.layout;
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
        
        // Change legend to horizontal 
        // and move to above plots for both graphs
        layout.legend.orientation = "h";
        layout.legend.xanchor = "right";
        layout.legend.x = 1;
        layout.legend.yanchor = "bottom";
        layout.legend.y = 1.02;
        graph_layout.legend.orientation = "h";
        graph_layout.legend.xanchor = "right";
        graph_layout.legend.x = 1;
        graph_layout.legend.yanchor = "bottom";
        graph_layout.legend.y = 1.02;
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
        
        // Change legend to vertical 
        // and move next to plots for both graphs
        layout.legend.orientation = "v";
        layout.legend.xanchor = "left";
        layout.legend.x = 1.02;
        layout.legend.yanchor = "auto";
        layout.legend.y = 1;
        graph_layout.legend.orientation = "v";
        graph_layout.legend.xanchor = "left";
        graph_layout.legend.x = 1.02;
        graph_layout.legend.yanchor = "auto";
        graph_layout.legend.y = 1;
    }
    
    Plotly.newPlot(barcharts, data, layout, config);
    Plotly.newPlot(graph, graph_data, graph_layout, config);
}

window.onresize = relayout_barcharts;