var width = 600,
			height = 600;
		var svgcanvas = d3.select("#chartContainer")
                        .append("svg")
                        .attr("width", width)
                        .attr("height", height)
                        .append("g");

		var x_values = d3.scale.linear()
					.range([0, width]);

		var y_values = d3.scale.linear()
					.range([0, height]);

		var xAxis = d3.svg.axis()
    				.scale(x_values)
    				.orient("bottom");

    	var yAxis = d3.svg.axis()
    				.scale(y)
    				.orient("left");

    	var line = d3.svg.line()
   	 				.x_values(function(d) { return x(d.max_enrollment); })
    				.y_values(function(d) { return y(d.act_enrollment); });

		d3.json("{% "graph_data" %}", function(error, data){
			data.forEach(function(d){
				d.max_enrollment = +d.max_enrollment;
				d.act_enrollment = +d.act_enrollment;
			})
		x_values.domain(d3.extent(data, function(d) { return d.max_enrollment; }));

  		y_values.domain(d3.extent(data, function(d) { return d.act_enrollment; }));

  		svg.append("g")
      		.attr("class", "x_axis")
      		.attr("transform", "translate(0," + height + ")")
      		.call(xAxis);

      	svg.append("g")
		      .attr("class", "y axis")
		      .call(yAxis)
		   .append("text")
		      .attr("transform", "rotate(-90)")
		      .attr("y", 6)
		      .attr("dy", ".71em")
		      .style("text-anchor", "end")
		      .text("Play count");

		svg.append("path")
      		.datum(data)
      		.attr("class", "line")
      		.attr("d", line);
		})	