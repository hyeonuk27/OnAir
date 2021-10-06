<template>
  <div class="airline">
    <div class="airline-container">
      <AirlineInfo
        v-if="isInfoRendered"
        :airlineInfo="airlineInfo"
      />
      <div
        v-else
        style="height: 700px;"
      >
      </div>
      <div class="tab-container">
        <input class="airline-tabradio" id="tab-analysis" type="radio" name="tab-check" checked>
        <label class="airline-tablabel" for="tab-analysis">분석 리포트</label>
        <input class="airline-tabradio" id="tab-review" type="radio" name="tab-check">
        <label class="airline-tablabel" for="tab-review">항공사 리뷰</label>
        <section class="airline-tab" id="content-analysis">
          <AnalysisTab
            v-if="isStatisticsRendered"
            :report="report"
          />
          <div
            v-else
            id="loading"
            style="height: 700px;"
          ></div>
        </section>
        <section class="airline-tab" id="content-review">
          <ReviewTab 
            v-if="isInfoRendered & isChartRendered"
            :airlineInfo="airlineInfo"
            :airlineId="airlineId"
            :arrivalId="arrivalId"
            :arrivalName="arrivalName"
            :chartData="reviewTotalRateChartData"
          />
          <div
            v-else
            id="loading"
            style="height: 700px;"
          ></div>
        </section>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import API from '@/common/drf.js'
import AirlineInfo from '@/components/airline/statistics/AirlineInfo'
import AnalysisTab from '@/components/airline/statistics/AnalysisTab'
import ReviewTab from '@/components/airline/statistics/ReviewTab'

export default {
  name: 'AirlineDetail',
  components: {
    AirlineInfo,
    AnalysisTab,
    ReviewTab,
  },
  data () {
    return {
      isStatisticsRendered: false,
      isInfoRendered: false,
      isChartRendered: false,
      arrivalName: '',
      arrivalId: '',
      airlineId: '',
      airlineInfo: {},
      report: {},
      reviewTotalRateChartData: {},
    }
  },
  methods: {
    getAirlineStatistics: function () {
      this.$vs.loading({
        type: 'material'
      })
      axios({
        url: `${API.URL}${API.ROUTES.getAirlines}${this.arrivalId}/${this.airlineId}/`,
        method: 'get',
      })
      .then((res) => {
        const report = res.data.data
        this.report = report
        this.isStatisticsRendered = true
        this.$vs.loading.close()
        this.arrivalName = report.arrival_name
      })
      .catch(() => {
        this.$vs.loading.close()
        this.$router.replace({ name: 'NotFoundPage' })
      })
    },
    getAirlineInfo: function () {
      axios({
        url: `${API.URL}${API.ROUTES.getAirlineInfo}${this.airlineId}/`,
        method: 'get',
      })
      .then((res) => {
        const airlineInfo = res.data
        this.airlineInfo = airlineInfo
        this.isInfoRendered = true
      })
    },
    getAirlineTotalRates: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}score/${this.airlineId}/`,
        method: 'get',
      })
      .then((res) => {
        const chartData = res.data
        this.reviewTotalRateChartData = chartData
        this.isChartRendered = true
      })
    }
  },
  created() {
    this.arrivalId = this.$route.params.arrivalId
    this.airlineId = this.$route.params.airlineId
    this.getAirlineInfo()
    this.getAirlineStatistics()
    this.getAirlineTotalRates()
  }
}
</script>

<style>
.airline {
  display: flex;
  justify-content: center;
  margin-top: 150px;
}
.airline-container {
  min-width: 1000px;
  width: 1000px;
}
.airline-tab {
  border-top: 2px solid #3D2F6B;
  display: none;
  padding: 20px 0 0;
  text-align: center;
}
.airline-tablabel {
  border: 1px solid transparent;
  color: #bbb;
  display: inline-flex;
  font-weight: 600;
  margin: 0 0 -1px;
  padding: 15px 25px;
  text-align: center;
}
.airline-tablabel:hover {
  color: #3D2F6B;
  cursor: pointer;
}
.airline-tabradio {
  display: none;
}
.airline-tabradio:checked + .airline-tablabel {
  border: 1px solid #ddd;
  border-bottom: 2px solid #ffffff;
  border-top: 2px solid #3D2F6B;
  color: #555;
}
#tab-analysis:checked ~ #content-analysis,
#tab-review:checked ~ #content-review {
  display: block;
}
.tab-container {
  margin: 0 auto;
  max-width: 1000px;
  min-width: 1000px;
  padding-top: 40px;
  text-align: start;
}
</style>