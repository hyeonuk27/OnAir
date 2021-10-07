const SERVER_URL = 'https://j5a203.p.ssafy.io/api/v1'

export default {
  URL: SERVER_URL,
  ROUTES: {
    createLog: '/logs/',
    getAirlines: '/airlines/',
    getAirlineInfo: '/airlines/airline/info/',
    getArrivals: '/arrivals/',
    getMyReviews: '/profiles/',
    getProfile: '/auth/profile/',
    getSearchLogs: '/logs/',
    login: '/auth/login/',
    reviewDetail: '/reviews/',
    reviewList: '/reviews/airline/',
    updateProfile: '/auth/',
  }
}