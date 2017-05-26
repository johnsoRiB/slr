/**
 * Created by jakob on 5/16/2017.
 */

// Set leaflet map
var map = L.map("map").setView([50, 15], 4);
// construct the base map.
L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png').addTo(map);

// Initialize the SVG layer


// map._initPathRoot()


var svgLayer = L.svg().addTo(map);


// Setup svg element to work with
var svg = d3.select("#map").select("svg");
var linklayer = svg.append("g");
var nodelayer = svg.append("g");


//linklayer.attr("class", "leaflet-zoom-hide");
//nodelayer.attr("class", "leaflet-zoom-hide");

// Load data asynchronosuly
d3.json("assets/nodes.geojson", function(nodes) {
    d3.csv("assets/links.csv", function(links) {

        // Setup spatialsankey object
        var spatialsankey = d3.spatialsankey()
            .lmap(map)
            .nodes(nodes.features)
            .links(links);

        var mouseover = function(d){

            alert("321321");
            // Get link data for this node
            var nodelinks = spatialsankey.links().filter(function(link){
                return link.source == d.id;
            });

            // Add data to link layer
            var beziers = linklayer.selectAll("path").data(nodelinks);
            link = spatialsankey.link({'use_arcs': false, 'flip': false});

            // Draw new links
            beziers.enter()
                .append("path")
                .attr("d", link)
                .attr('id', function(d){return d.id})
                .style("stroke-width", spatialsankey.link().width());

            // Remove old links
            beziers.exit().remove();

            // Hide inactive nodes
            var circleUnderMouse = this;
            circs.transition().style('opacity',function () {
                return (this === circleUnderMouse) ? 0.7 : 0;
            });
        };

        var mouseout = function(d) {
            alert("321321");
            // Remove links
            linklayer.selectAll("path").remove();
            // Show all nodes
            circs.transition().style('opacity', 0.7);
        };

        // Draw nodes
        var node = spatialsankey.node()
        var circs = nodelayer.selectAll("circle")
            .data(spatialsankey.nodes())
            .enter()
            .append("circle")
            .attr("cx", node.cx)
            .attr("cy", node.cy)
            .attr("r", node.r)
            .style("fill", node.fill)
            .attr("opacity", 0.7)
            .on('mouseover', mouseover)
            .on('mouseout', mouseout);

        // Adopt size of drawn objects after leaflet zoom reset
        var zoomend = function(){
            linklayer.selectAll("path").attr("d", spatialsankey.link());

            circs.attr("cx", node.cx)
                .attr("cy", node.cy);
        };

        map.on("zoomend", zoomend);
    });
});

