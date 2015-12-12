 var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 1000 - margin.left - margin.right,
    height = 1100 - margin.top - margin.bottom;

var xValue = function(d) {return d.TERM_CODE;};

var xScale = d3.scale.ordinal()
          .rangeRoundBands([0, width-190], .1) // value -> display
    
var xMap = function(d) { return xScale((d.TERM_DESCRIPTION));} // data -> display

// var xAxis = d3.svg.axis()
//       .scale(xScale)
//       .orient("bottom")
      // .tickFormat(d3.format("d"))
      // .outerTickSize(0);

var xScale = d3.scale.ordinal()
          .rangeRoundBands([0, width-190], .1);
var y = d3.scale.linear().range([height/2 - 150, 0])

var xAxis = d3.svg.axis()
    .scale(xScale)
    .orient("bottom")
    .ticks(2)
    .outerTickSize(3);

var yValue = function(d) { return d.ACTUAL_ENROLLMENT;}, // data -> value
    yScale = d3.scale.linear().range([height/2 - 150, 0]).nice(), // value -> display
    yMap = function(d) { return yScale(yValue(d));}, // data -> display
    yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(16).outerTickSize(0);

// setup fill color
var cValue = function(d) { return d.TITLE;},
    color = d3.scale.category20();


// add the graph canvas to the body of the webpage
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);


d3.csv("CS_Actual_Enrollments.csv", function(error, data) {
  // change string (from CSV) into number format
  data.forEach(function(d) {
    d.TERM_CODE = +d.TERM_CODE;
    d["totaltime"] = +d["totaltime"];
    //console.log(d);
     });


  // don't want dots overlapping axis, so add in buffer to data domain
xScale.domain(data.map(function(d) { return d.TERM_DESCRIPTION; }));
yScale.domain([0, ymax])
  var term = [],
    num_students = [];
    
  data.map(function(d){
    term.push(d.TERM_DESCRIPTION)
    num_students.push(d.MAXIMUM_ENROLLMENT)
  })

var ymax = d3.max(num_students)
  // xScale.domain(data.map(function(d) { return d.TERM_DESCRIPTION; }));
  // console.log(d3.min(data, xValue)+1);
//1814491
  yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+1]);

//adding trend line
var line = d3.svg.line()
  .x(function(d) {return xScale(d['TERM_DESCRIPTION'])})
  .y(function(d) {return yScale(d['ACTUAL_ENROLLMENT'])});


// svg.append("path")
//   .datum(data)
//   .attr("class", "line")
//   .attr("d", line);

   //addint title
  svg.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top -15))
        .attr("class", "title")
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .style("text-decoration", "underline")  
        .text("Computer Science Classes");

    // x-axis
var svgXaxis = svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + (height/2 -90 )+ ")")
    .call(xAxis)
    .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", ".15em")
            .attr("transform", function(d) {
                return "rotate(-65)" 
                });


// y-axis
  var svgYaxis = svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Number of Students");

update();

function update () {
  // update the scales' domain
  // xScale.domain([d3.min(data, xValue)-1, d3.max(data, xValue)+1]);
  xScale.domain(data.map(function(d) { return d.TERM_DESCRIPTION; }))
        .rangeRoundBands([0, width-190], .1)
  yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+1]);
  
  svgXaxis.transition()
      .call(xAxis);
  svgYaxis.transition()
      .call(yAxis);
}

// draw dots
  // var dots=svg.selectAll(".dot")
  //     .data(data)
  //   .enter().append("circle")
  //     .attr("class", "dot")
  //     .attr("class", function(d){return d["TITLE"]})
  //     .attr("r", 2.5)
  //     .attr("cx", xMap)
  //     .attr("cy", yMap)
  //     .style("fill", function(d) { return color(cValue(d));}) 
  //     .on("mouseover", function(d) {
  //         tooltip.transition()
  //              .duration(200)
  //              .style("opacity", .9);
  //         tooltip.html(d["TITLE"] + ", " + d["SCHEDULE_DESC"]  + "<br/> (" + xValue(d) 
  //         + ", " + d['ACTUAL_ENROLLMENT'] + ")")
  //              .style("left", (d3.event.pageX + 5) + "px")
  //              .style("top", (d3.event.pageY - 28) + "px");
  //     })
  // // draw legend
  var legend = svg.selectAll(".legend")
      .data(color.domain())
    .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; 
    });

   // draw legend colored rectangles
  legend.append("rect")
      .attr("x", width)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

     // draw legend text
  legend.append("text")
      .attr("x", width - 20)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d;})

GrpByClass()
function GrpByClass(){
        //groups by class
      var byclass = d3.nest()
        .key(function(d) { return d.TITLE; })
        .entries(data);
        // console.log(byclass);
      // var byclassjson = JSON.stringify(byclass);
      // console.log(byclassjson)

      var bysem = d3.nest()
        .key(function(d) { return d.TERM_DESCRIPTION; })
        .entries(data);
        console.log(bysem.length);
      var data3 =[];
      
      var data3_OBJ =[];

        for (i = 0; i<bysem.length; i++){
          data3.push(bysem[i].values)
          // console.log(bysem[i].values)
        } 
        // console.log(data3)
        // console.log(data3[8][1].TITLE)
        for (i = 0; i<data3.length; i++){
          for (j = 0; j <data3[i].length; j++){
            data3_OBJ.push(data3[i][j])
          }
          
        }
        // console.log(data3) 
        // console.log(data3_OBJ)
        var act_enrol = [];
        var term_desc = [];

        var counter = 0; 

        var testdata =[];

      // console.log(data1)
      for(i = 0; i < data3_OBJ.length; i++){ 
        // console.log(data3_OBJ[i].TERM_DESCRIPTION)                      
        var className = data3_OBJ[i].TITLE;        
        var classType = data3_OBJ[i].SCHEDULE_DESC;

        if (classType == 'Lecture' ){
          var term = data3_OBJ[i].TERM_DESCRIPTION;
          var studentsEnrolled = parseInt(data3_OBJ[i].ACTUAL_ENROLLMENT);          
          
          if (className == previousClassName){
            counter--;
            act_enrol[counter] += studentsEnrolled;
            
          } else {
            act_enrol[counter] = studentsEnrolled;
          }   
          counter++;
          // console.log(act_enrol)      

          // console.log(studentsEnrolled);
          // testdata.push("semester" +":"+ term +","+ "Std_Num" +":"+studentsEnrolled)
          // console.log(studentsEnrolled +": " + className +": " + classType +": " +term);          
          // console.log('Current - ' + className + "     Previous - " + previousClassName);
          var previousClassName = className;
        } 
        // console.log(studentsEnrolled +": " + className +": " + classType +": " +term)
        // console.log(testdata)


        var sem1 = bysem[0]
        // console.log(sem1)

        var data2 = sem1.values
        // var data3 = data2.Object.values
        // console.log(data2)
      //get class from byclass
      var LivWthComp = byclass[0]
      // console.log(LivWthComp)
      //var class = byclass[i]
      
      var Gr_title = LivWthComp.key
      //byclass[i].key - gives the value of the key named key
      //console.log(Gr_title)

      var data1 = LivWthComp.values;
      // var act_enrol = [];
      // var term_desc = [];

      // var counter = 0; 

      // // console.log(data1)
      // for(i = 0; i < data2.length; i++){                       
      //   var className = data2[i].TITLE;        
      //   var classType = data2[i].SCHEDULE_DESC;

      //   if (classType == 'Lecture' ){
      //     var term = data2[i].TERM_DESCRIPTION;
      //     var studentsEnrolled = parseInt(data2[i].ACTUAL_ENROLLMENT);          
          
      //     if (className == previousClassName){
      //       counter--;
      //       act_enrol[counter] += studentsEnrolled;
      //     } else {
      //       act_enrol[counter] = studentsEnrolled;
      //     }   
      //     counter++;      

      //     console.log(data2[i]);          
      //     // console.log('Current - ' + className + "     Previous - " + previousClassName);
      //     var previousClassName = className;
      //   }        
        
          // act_enrol.push(data1[i].ACTUAL_ENROLLMENT)
          // term_desc.push(data1[i].TERM_DESCRIPTION)
          // console.log(data1[i].TERM_DESCRIPTION)

          // if(data2[i].TERM_DESCRIPTION == "Fall Semester 2005" && data2[i].SCHEDULE_DESC == "Lecture" && data2[i].TITLE== "Living with Computers"){
          //   // console.log(data1[i].TERM_DESCRIPTION + ":  " + data1[i].TITLE + ":  " + data1[i].SCHEDULE_DESC + ":  " + data1[i].ACTUAL_ENROLLMENT)
          //   // console.log(data1[i].TERM_DESCRIPTION + ":  " + data1[i].TITLE)
          //   // console.log(data1[i+1].TERM_DESCRIPTION + ":  " + data1[i+1].TITLE)
          //   // console.log(data1[i].TERM_DESCRIPTION + ":  " + data1[i].SCHEDULE_DESC)
          //   // console.log(data1[i+1].TERM_DESCRIPTION + ":  " + data1[i+1].SCHEDULE_DESC)

          //   // console.log(data1[i].TERM_DESCRIPTION + " " + data1[i+1].TERM_DESCRIPTION)
          //   var td = ("Fall Semester 2005")
          //   console.log(parseInt(data2[i].ACTUAL_ENROLLMENT) + parseInt(data2[i+1].ACTUAL_ENROLLMENT))
          //   console.log("hi")
          // }
      }

      // console.log(act_enrol);

      for (act_enrol in data2){
        // console.log(data2[act_enrol].ACTUAL_ENROLLMENT)
      }


      svg.append("g")
        .attr("class", "y axis");
    
      svg.append("g")
        .attr("class", "x axis");

      var xScale1 = d3.scale.ordinal()
        .rangeRoundBands([margin.left, width], .1);
    
      var yScale1 = d3.scale.linear()
        .range([height/2 - 150, 0]);
      
      var xAxis = d3.svg.axis()
        .scale(xScale1)
        .orient("bottom");
        
      var yAxis = d3.svg.axis()
        .scale(yScale1)
        .orient("left");
        
      //extract the x labels for the axis and scale domain
      var xLabels = data3_OBJ.map(function (d) {return d['TERM_DESCRIPTION']})
        xScale1.domain(xLabels)
        // console.log(xLabels+"hey")

        yScale1.domain([0, d3.max(data3_OBJ, function(d) {return parseInt(d['ACTUAL_ENROLLMENT'])})])

      //   //appending path
      // svg.append("path")
      //     .datum(data1)
      //     .attr("class", "line")
      //     .attr("d", line);

      svg.select(".x.axis")
              .attr("transform", "translate(0," + (height/2 - 150) + ")")
        //       .call(xAxis.tickValues(xLabels.filter(function(d, i) { 
        // if (i % 3 == 0)
        //   return d;
        // })))
              .selectAll("text")
              .style("text-anchor", "end")
              .attr("transform", function(d) {return "rotate(-45)";});

      svg.select(".y.axis")
              .attr("transform", "translate(0,0)")
              .call(yAxis);

      // draw dots
  var dots=svg.selectAll(".dot")
      .data(data3_OBJ)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("class", function(d){return d["TITLE"]})
      .attr("r", 2.5)
      .attr("cx", function(d) { return xScale((d.TERM_DESCRIPTION));}
)
      .attr("cy", function(d) {return yScale1(parseInt(d['ACTUAL_ENROLLMENT']))})
      .style("fill", function(d) { return color(cValue(d));}) 
      .on("mouseover", function(d) {
          tooltip.transition()
               .duration(200)
               .style("opacity", .9);
          tooltip.html(d["TITLE"] + ", " + d["SCHEDULE_DESC"]  + "<br/> (" + xValue(d) 
          + ", " + d['ACTUAL_ENROLLMENT'] + ")")
               .style("left", (d3.event.pageX + 5) + "px")
               .style("top", (d3.event.pageY - 28) + "px");
      })
//console.log(term_desc)

      //console.log(d3.values(LivWthComp))
      // console.log(d3.keys(LivWthComp))
       // // console.log(xdata[0].ACTUAL_ENROLLMENT)
      // // console.log(xdata[0].TERM_DESCRIPTION)
      // console.log(xdata.length)




  }
})
