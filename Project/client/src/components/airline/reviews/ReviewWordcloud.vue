// <template>
//   <div>
//     <img src="@/assets/test.png" style="width:100%" alt="">
//   </div>
// </template>

// <script src="https://d3js.org/d3.v3.min.js"></script>
// <script src="https://rawgit.com/jasondavies/d3-cloud/master/build/d3.layout.cloud.js" type="text/JavaScript"></script>
// <script>
// // import axios from "axios";
// // import API from "@/common/drf.js"
// var width = 960, height = 500
// var svg = d3.select("body").append("svg")
//             .attr("width", width)
//             .attr("height", height);
// d3.csv("worddata.csv", function (data) {
//   showCloud(data)
//   setInterval(function(){
//     showCloud(data)
//   },2000) 
// });

// wordScale = d3.scale.linear().domain([0, 100]).range([0, 150]).clamp(true);
// var keywords = ["자리야", "트레이서", "한조"]
// var svg = d3.select("svg")
//             .append("g")
//             .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")

// export default {
//   methods: {
//     showCloud: function(data) {
//       d3.layout.cloud().size([width, height])
//         .words(data)
//         .rotate(function (d) {
//           return d.text.length > 3 ? 0 : 90;
//           })
//         .fontSize(function (d) {
//           return wordScale(d.frequency);
//         })
//         .on("end", draw)
//         .start();
//     },
//     draw: function(words) { 
//       var cloud = svg.selectAll("text").data(words)
//       cloud.enter()
//           .append("text")
//           .style("font-family", "overwatch")
//           .style("fill", function (d) {
//             return (keywords.indexOf(d.text) > -1 ? "#fbc280" : "#405275");
//           })
//           .style("fill-opacity", .5)
//           .attr("text-anchor", "middle") 
//           .attr('font-size', 1)
//           .text(function (d) {
//             return d.text;
//           }); 
//       cloud
//         .transition()
//         .duration(600)
//         .style("font-size", function (d) {
//           return d.size + "px";
//         })
//         .attr("transform", function (d) {
//           return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
//         })
//         .style("fill-opacity", 1); 
//     }
//   },
//   created() {
//     this.showCloud();
//     this.draw();
//   },
// };

//   // name: "ReviewWordcloud",


//   // props: {
//   //   airlineId: String,
//   // },
//   // data() {
//   //   return {
//   //     keywordList: [],
//   //   };
//   // },
//   // methods: {
//   //   getKeyword: function () {
//   //     axios({
//   //       url: `${API.URL}${API.ROUTES.reviewDetail}wordcloud/${this.airlineId}/`,
//   //       method: "get",
//   //     })
//   //     .then((res) => {
//   //       this.keywordList = res.data;
//   //     })
//   //     .catch((err) => {
//   //       console.log(err);
//   //     });
//   //   },
//   // },


// </script>

// <style>
// /* @font-face {
//     font-family: 'overwatch';
//     src: url('fonts/koverwatch.woff2');
// } */
// </style>