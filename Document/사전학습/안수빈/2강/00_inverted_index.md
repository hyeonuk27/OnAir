# Inverted Index

> 각 단어마다 그 단어가 나타나는 문서 아이디 doc와 그 문서에서 나오는 위치 position을 `doc:postition` 형태로 리스트를 만든다.

## 1. 알고리즘

- 각 머신에서 각 문서마다 Map 함수가 호출되고 문서를 스캔하면서 단어 하나마다 그 단어를 KEY로 하고 문서 아이디 DOC와 그 문서에서 나오는 위치 POSITION을 DOC:POSITION 형태로 VALUE를 만들어 (KEY, VALUE)로 출력한다.
- 셔플링 페이즈에서는 Map 함수가 출력한 (KEY, VALUE) 쌍에 대해서 같은 KEY를 가진 VALUE들의 리스트를 모은 뒤에 VALUE-LIST를 만들고 (KEY, VALUE-LIST) 쌍을 출력한다.
- 셔플링 페이즈가 끝나면 각각의 (KEY, VALUE-LIST) 쌍에 대해서 각각의 KEY마다 Reduce 함수가 호출되는데 VALUE-LIST에 있는 VALUE들을 다 합한 값을 (KEY, VALUE) 형태로 출력한다.



