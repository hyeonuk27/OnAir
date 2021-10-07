<template>
  <div v-if="isRendered" class="mx-2">
    <figure class="highcharts-figure">
      <charts :options="wordCloud" />
    </figure>
  </div>
  <div
    v-else
    style="display: flex; justify-content: center; align-items: center; height: 400px; font-weight: bold; color: #3D2F6B;">
    워드 클라우드 생성중입니다 ...
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'

export default {
  name: 'ReviewWordcloud',
  props: {
    airlineId: String,
  },
  data() {
    return {
      data: [],
      isRendered: false,
    }
  },
  methods: {
    getKeyword: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}wordcloud/${this.airlineId}/`,
        method: 'get',
      })
      .then((res) => {
        this.data = res.data
        this.isRendered = true
      })
    },
  },
  created() {
    this.getKeyword()
  },
  computed: {
    wordCloud: function () {
      return {
        series: [{
          colors: [
            '#3D2F6B', '#85456B', '#B9A6C9'
          ], 
          rotation: {
            from: 0,
            to: 0,
          },
          data: this.data,
          duration: 0,
          minFontSize: 8,
          name: '빈도수',
          placementStrategy: 'random',
          spiral: 'archimedean',
          style: {'fontFamily': 'sans-serif'},
          type: 'wordcloud',
        }],
        credits: {
          enabled: false
        },
        exporting: {
          enabled: false
        },
        title: {
          text: null
        }
      }
    }
  },
}
</script>

<style>
.highcharts-data-table caption {
  font-size: 1.2em;
  color: #555;
  padding: 1em 0;
}
.highcharts-data-table table {
  border: 1px solid rgba(180, 180, 180, 0.658);
	border-collapse: collapse;
	font-family: Verdana, sans-serif;
	margin: 10px auto;
	max-width: 500px;
	text-align: center;
	width: 100%;
}
.highcharts-data-table td, .highcharts-data-table th, .highcharts-data-table caption {
  padding: 0.5em;
}
.highcharts-data-table th {
	font-weight: 600;
  padding: 0.5em;
}
.highcharts-data-table tr:hover {
  background: #f1f7ff;
}
.highcharts-data-table thead tr, .highcharts-data-table tr:nth-child(even) {
  background: #f8f8f8;
}
.highcharts-figure, .highcharts-data-table table {
  margin: 1rem auto;
  width: 100%; 
}
</style>
