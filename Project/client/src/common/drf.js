const SERVER_URL = 'http://127.0.0.1:8000/api/v1'
// const SERVER_URL = 'https://j5a203.p.ssafy.io/api/v1'

export default {
  URL: SERVER_URL,
  ROUTES: {
    // 예시) login: '/accounts/login/',
    // 사용법) import API from '@/common/drf.js' 후, API.SERVER_URL + API.ROUTES.login
    login: '/auth/login/',
    get_arrivals: '/arrivals/',
    get_airlines: '/airlines/',
<<<<<<< HEAD
    get_airline_info: '/airlines/info/',
=======
    review_list: '/reviews/airline/',
>>>>>>> 31acce97a3955761a6fb7816547e6a22c912d530
  }
}