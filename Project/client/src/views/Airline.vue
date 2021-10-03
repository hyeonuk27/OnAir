<template>
  <div class="airline">
    <div class="airline-container">
      <AirlineInfo 
      :airlineInfo="airlineInfo"
      />
      <div class="tab-container">
        <input class="airline-tabradio" id="tab-analysis" type="radio" name="tab-check" checked>
        <label class="airline-tablabel" for="tab-analysis">분석 리포트</label>
        <input class="airline-tabradio" id="tab-review" type="radio" name="tab-check">
        <label class="airline-tablabel" for="tab-review">리뷰 리포트</label>
        <section class="airline-tab" id="content-analysis">
          <AnalysisTab
          :report="report"
          :predictedDelayRate="predictedDelayRate"
          />
        </section>
        <section class="airline-tab" id="content-review">
          <ReviewTab 
          :airlineInfo="airlineInfo"
          />
        </section>
      </div>
    </div>
  </div>
</template>


<script>
import AirlineInfo from "@/components/airline/statistics/AirlineInfo"
import AnalysisTab from "@/components/airline/statistics/AnalysisTab"
import ReviewTab from "@/components/airline/statistics/ReviewTab"

import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: 'AirlineDetail',
  components: {
    AirlineInfo,
    AnalysisTab,
    ReviewTab,
  },
  data () {
    return {
      arrivalId: '',
      airlineId: '',
      predictedDelayRate: '',
      airlineInfo: {},
      report: {},
    }
  },
  methods: {
    getAirlineStatistics: function () {
      axios({
        url: API.URL + API.ROUTES.getAirlines + this.arrivalId + '/' + this.airlineId + '/',
        method: "get",
      })
        .then((res) => {
          const report = res.data.data
          this.report = report
          console.log(report)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getAirlineInfo: function () {
      axios({
        url: API.URL + API.ROUTES.getAirlineInfo + this.airlineId + '/',
        method: "get",
      })
        .then((res) => {
          const airlineInfo = res.data
          this.airlineInfo = airlineInfo
          console.log(airlineInfo)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.arrivalId = this.$route.params.arrivalId
    this.airlineId = this.$route.params.airlineId
    this.predictedDelayRate = this.$route.params.predictedDelayRate
    this.getAirlineInfo()
    this.getAirlineStatistics()
  }
}
</script>

<style>
  .airline {
    display: flex;
    justify-content: center;
    margin-top: 150px;
  }

  .tab-container {
    min-width: 1000px;
    max-width: 1000px;
    padding-top: 20px;
    margin: 0 auto;
  }

  .airline-container {
    width: 1000px;
    min-width: 1000px;
  }

  .airline-tab {
    display: none;
    padding: 20px 0 0;
    border-top: 1px solid #ddd
  }

  .airline-tabradio {
    display: none;
  }

  .airline-tablabel {
    display: inline-flex;
    justify-content: left;
    margin: 0 0 -1px;
    padding: 15px 25px;
    font-weight: 600;
    text-align: center;
    color: #bbb;
    border: 1px solid transparent;
  }

  .airline-tabradio:hover {
    color: #3D2F6B;
    cursor: pointer;
  }

  .airline-tabradio:checked + .airline-tablabel {
    color: #555;
    border: 1px solid #ddd;
    border-top: 2px solid #3D2F6B;
    border-bottom: 1px solid #ffffff
  }

  #tab-analysis:checked ~ #content-analysis,
  #tab-review:checked ~ #content-review {
    display: block;
  }
</style>