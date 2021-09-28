const SERVER_URL = process.env.VUE_APP_SERVER_URL + '/api/v1'

export default {
  URL: SERVER_URL,
  ROUTES: {
    // 예시) login: '/accounts/login/',
    // 사용법) import API from '@/common/drf.js' 후, API.SERVER_URL + API.ROUTES.login
    get_arrivals: '/arrivals/',
    get_airlines: '/airlines/'
  }
}