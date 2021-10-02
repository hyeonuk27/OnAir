// const SERVER_URL = 'http://127.0.0.1:8000/api/v1'
const SERVER_URL = 'https://j5a203.p.ssafy.io/api/v1'

export default {
  URL: SERVER_URL,
  ROUTES: {
    // 예시) login: '/accounts/login/',
    // 사용법) import API from '@/common/drf.js' 후, API.SERVER_URL + API.ROUTES.login
    login: '/auth/login/',
    getArrivals: '/arrivals/',
    getAirlines: '/airlines/',
    getAirlineInfo: '/airlines/airline/info/',
    reviewList: '/reviews/airline/',
    reviewDetail: '/reviews/',
    getProfile: '/auth/profile/',
    updateProfile: '/auth/',
    getMyReviews: '/profiles/'
  }
}