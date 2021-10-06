<template>
  <div class="not-found">
    <div class="not-found-container">
      <div class="not-found-body">
        <img class="not-found-img img-fluid" src="@/assets/lost.png" alt="error-img">
      </div>
      <div class="not-found-text">
        <h1><i class="fas fa-exclamation-circle"></i> 잘못된 접근입니다!</h1>
        <h5>찾으시는 항공사 - 목적지 분석 결과가 아직 없어요. 곧 추가할게요!</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
}
</script>

<style>
.not-found {
  align-items: center;
  display: flex;
  justify-content: center;
  margin-top: 150px;
}
.not-found-body {
  margin: 60px 0px;
}
.not-found-container {
  min-height: 650px;
  width: 1000px;
}
.not-found-img {
  justify-content: center;
  object-fit: cover;
  width: 180px;
}
.not-found-text {
  text-align: center;
}
</style>