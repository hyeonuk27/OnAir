<template>
  <div>
    <h1>리뷰 작성</h1>

    <!-- 리뷰 -->
    <input 
      type="text"
      v-model="title"
      placeholder="제목을 입력하세요."
      required
    >

    <!-- 내용 -->
    <input 
      type="text"
      v-model="content"
      placeholder="내용을 입력하세요."
      required
    >

    <!-- 평점 -->
    <input 
      type="number"
      min="0"
      max="5"
      v-model="score"
      required
    >
    <input 
      type="number"
      min="1"
      max="5"
      v-model="seatScore"
    >
    <input 
      type="number"
      min="1"
      max="5"
      v-model="serviceScore"
    >    
    <input 
      type="number"
      min="1"
      max="5"
      v-model="checkinScore"
    >
    <input 
      type="number"
      min="1"
      max="5"
      v-model="foodScore"
    >    
    <!-- 좌석 종류 선택 -->
    <select
      name="flightAt"
      id="flightAt"
      v-model="flightAt"
    >
      <option value="noValue" selected>좌석 선택</option>
      <option 
        v-for="seat in seatList"
        :key="seat"
        value="seat">
      </option>
    </select>
  </div>

</template>

<script>
export default {
  name: "ReviewCreate",
  data() {
    return {
      title: "",
      content: "",
      flightAt = "",
      seat = "",
      seatList = [퍼스트, 비즈니스, 이코노미],
      score = 0,
      seatScore = 0,
      serviceScore = 0,
      checkinScore = 0,
      foodScore = 0,
    }
  }
  method:
}
</script>

<style>

</style>