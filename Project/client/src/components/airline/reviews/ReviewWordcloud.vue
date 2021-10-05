<template>
  <div>
    <!-- <img src="@/assets/test.png" style="width:100%" alt=""> -->
    <figure class="highcharts-figure">
      <charts :options="wordCloud" />
    </figure>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: "ReviewWordcloud",
  props: {
    airlineId: String,
  },
  created() {
    this.getKeyword()
  },
  data() {
    return {
      data: [],
    };
  },
  computed: {
    wordCloud: function() {
      return {
        accessibility: {
            screenReaderSection: {
                beforeChartFormat: 
                    '<h5>{chartTitle}</h5>' +
                    '<div>{chartLongdesc}</div>' +
                    '<div>{viewTableButton}</div>'
            }
        },
        series: [{
            colors: [
              '#3D2F6B', '#B9A6C9', '#85456B'], 
              // '#3D2F6B', '#632A6D', '#85456B'], 
            rotation: {
                from: 0,
                to: 0,
            },
            // maxfontsize: 1000,
            minFontSize: 8,
            duration: 0,
            placementStrategy: 'random',
            spiral: 'archimedean',
            style: {"fontFamily":"sans-serif"},
            type: 'wordcloud',
            data: this.data,
            name: '빈도수'
        }],
        title: {
            text: ''
        }
      }
    }
  },
  methods: {
    getKeyword: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}wordcloud/${this.airlineId}/`,
        method: "get",
      })
      .then((res) => {
        this.data = res.data
      })
      .catch((err) => {
        console.log(err);
      })
    },
  }
}

</script>
<style>
.highcharts-figure, .highcharts-data-table table {
  width: 100%; 
  margin: 1em auto;
}

.highcharts-data-table table {
	font-family: Verdana, sans-serif;
	border-collapse: collapse;
	border: 1px solid #EBEBEB;
	margin: 10px auto;
	text-align: center;
	width: 100%;
	max-width: 500px;
}
.highcharts-data-table caption {
  padding: 1em 0;
  font-size: 1.2em;
  color: #555;
}
.highcharts-data-table th {
	font-weight: 600;
  padding: 0.5em;
}
.highcharts-data-table td, .highcharts-data-table th, .highcharts-data-table caption {
  padding: 0.5em;
}
.highcharts-data-table thead tr, .highcharts-data-table tr:nth-child(even) {
  background: #f8f8f8;
}
.highcharts-data-table tr:hover {
  background: #f1f7ff;
}
</style>
