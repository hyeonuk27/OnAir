<template>
  <div>
    <img src="@/assets/test.png" style="width:100%" alt="">
    <!-- <div id="word-cloud"> -->
    <!-- </div> -->
  </div>
</template>
<script>
// import axios from "axios";
// import API from "@/common/drf.js"
// import * as d3 from "d3";
// export default {
//   name: "ReviewWordcloud",
//   props: {
//     airlineId: String,
//   },
//   data() {
//     return {
//       keywordList: [],
//     };
//   },
//   mounted() {
//     this.getKeyword();
//   },
//   methods: {
//     getKeyword: function () {
//       axios({
//         url: `${API.URL}${API.ROUTES.reviewDetail}wordcloud/${this.airlineId}/`,
//         method: "get",
//       })
//       .then((res) => {
//         this.keywordList = res.data
//         for (var keyword in this.keywordList) {
//           this.showCloud(keyword)
//           setInterval(function(){
//             this.showCloud(keyword)
//           }, 2000)
//         }
//       })
//       .catch((err) => {
//         console.log(err);
//       });
//     },
//     showCloud: function(keyword) {
//       d3.layout.cloud().size([960, 500])
//         .words(keyword)
//         .rotate(function (d) {
//           return d[0].length > 3 ? 0 : 90;
//           })
//         .fontSize(function (d) {
//           return d[1];
//         })
//         .on("end", this.draw)
//         .start();
//     },
//     draw: function(words) {
//       d3.select("#word-cloud")    
//         .append("svg")
//         .attr("width", 960)
//         .attr("height", 500)
//         .append("g")
//         .attr("transform", "translate(" + 960 / 2 + "," + 500 / 2 + ")")
//         .selectAll("text")
//         .data(words)
//         .enter()
//         .append("text")
//         .style("font-family", "overwatch")
//         .style("fill", function (d) {
//           var keywords = ["자리야", "트레이서", "한조"];
//           return (keywords.indexOf(d.text) > -1 ? "#fbc280" : "#405275");
//         })
//         .style("fill-opacity", .5)
//         .attr("text-anchor", "middle") 
//         .attr('font-size', 1)
//         .text(function (d) {
//           return d.text;
//         })
//         .transition()
//         .duration(600)
//         .style("font-size", function (d) {
//           return d[1] + "px";
//         })
//         .attr("transform", function (d) {
//           return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
//         })
//         .style("fill-opacity", 1); 
//     },
//   }
// };
</script>