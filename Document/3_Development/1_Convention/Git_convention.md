## 1. Commit 컨벤션

```bash
<ISSUE_KEY> <optional COMMAND_ARGUMENTS>
```

- Git 컨벤션
  - feat : 새로운 기능 추가
  - fix : 버그 수정
  - docs : 문서
  - test : 테스트 코드
  - refactor : 코드 리팩토링(기능말고 성능개선)
  - style : 코드 의미에 영향을 주지 않는 변경사항
  - chore : 빌드, 설정 파일
- 규칙
  - 제목의 길이는 50글자를 넘기지 않는다
  - 제목의 마지막에 마침표를 사용하지 않는다
  - 본문을 작성할 때 한 줄에 72글자 넘기지 않는다
  - 마침표를 사용하지 않는다
  - 과거형을 사용하지 않는다
  - 커밋 메시지는 **영어**로 작성한다
- 예시

```bash
[S05P1A5075-39] feat: Summarize changes in around 50 characters or less

This is a body part. Please describe the details of commit.
```

## 2. 브랜치

- master : 배포

- develop : 개발된 기능(feature)을 통합하는 브랜치

- docs : 문서작업 브랜치

- feature/[function name] : 각 기능별 개발을 진행하는 브랜치

- release/[version] : 배포 전, 현재까지의 develop 상태를 가져와서 버그 픽스하고 지금 상태까지를 현재 개발 중인 버전으로.

- hotfix/[version] : 배포한 것을 급하게 수정

- 브랜치 흐름

  ![https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5149a740-16f0-475b-93fe-a9f06c54d1f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210910T023829Z&X-Amz-Expires=86400&X-Amz-Signature=78fa435022fab26bc93559064b7b1de8b2eca93873a805f70f1bf33e77536be9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5149a740-16f0-475b-93fe-a9f06c54d1f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210910T023829Z&X-Amz-Expires=86400&X-Amz-Signature=78fa435022fab26bc93559064b7b1de8b2eca93873a805f70f1bf33e77536be9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 3. 코딩

- 백엔드(Java기준, Django 미정)

  - 파일명: PascalCase (ex: UserRepository)
  - 패키지명: 소문자
  - 클래스: PascalCase (ex : ClassName)
  - 변수: camelCase (ex : getId, userPassword)
  - 메소드 : camelCase (ex : getId, userPassword)
  - 상수: snake_case (ex: FILE_NUMBER)

- 프론트엔드

  - 변수: camelCase

  - 함수: camelCase (ex. const functionName= function () {})

  - 상수: SNAKE_CASE

  - vue 파일명: PascalCase

  - js 파일명: kebab-case

  - template구조

    - router: PascalCase

  - style구조

    - css 클래스: kebab-case

    - css 스타일 가이드: 

      

      https://code-study.tistory.com/18

      - 선택자, 속성 전부 알파벳 순서

  - script구조(이하 리스트 순서대로 작성)

    - name
    - components
    - props
    - data : 단일 데이터를 상위에 명시,  form 구조를 하위에 명시
    - methods
    - Life Cycle Hook 순서 (beforeCreate → created → beforeMount → mounted → beforeUpdate → updated → beforeDestroy → destroyed)
    - computed
    - watch