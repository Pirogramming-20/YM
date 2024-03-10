## 요즘MT
1분 안에 끝내는 레크레이션 준비<br>
개발기간: 2024.01.29 ~ 2024.02.20

## 🔗프로젝트 링크
www.yozmt.com

## 팀원소개표 🔎

<table>
  <tbody>
    <tr>
      <td align="center"><a href=""><img src="https://github.com/Pirogramming-20/YM/assets/121532823/aebaf1bf-491b-47e3-a92a-d4af72fd4ac3" width="100px;" alt=""/><br /><sub><b> PM : 석우진 </b></sub></a><br /></td>
      <td align="center"><a href=""><img src="https://github.com/Pirogramming-20/YM/assets/121532823/c7a1df57-911a-452d-82e4-69347c7f4fae" width="100px;" alt=""/><br /><sub><b> FE : 웨이 </b></sub></a><br /></td>
      <td align="center"><a href=""><img src="https://github.com/Pirogramming-20/YM/assets/121532823/ab545d7d-0c72-479f-9d3d-e6d3be012023" width="100px;" alt=""/><br /><sub><b> BE : 정현정</b></sub></a><br /></td>
      <td align="center"><a href=""><img src="https://github.com/Pirogramming-20/YM/assets/121532823/a550358f-576b-4fbe-b350-96153c06b967" width="100px;" alt=""/><br /><sub><b> BE : 최윤서</b></sub></a><br /></td>
      <td align="center"><a href=""><img src="https://github.com/Pirogramming-20/YM/assets/121532823/93db4d3c-f862-480f-8b9b-65f1964393de" width="100px;" alt=""/><br /><sub><b> BE : 오기택</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>


## 기술스택 

### ✔️Frond-end
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">

### ✔️Back-end
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

### ✔️Release
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 

## About 요즘MT
- 요즘MT는 레크레이션 PPT 준비를 웹서비스를 통해 획기적으로 단축하고자 기획되었습니다.
- 간단한 회원가입 후 게임방을 생성하여 최대 8종류의 레크레이션 전용 게임을 원하는 순서로 정하여 진행할 수 있으며, 동시에 게임을 진행하는 데 도움이 될 여러 사람이 동시에 참여할 수 있는 실시간 채팅방을 제공하고 있습니다.
- 단순히 게임만을 플레이 하고싶은 개인 유저들운 로그인 없이 다양한 게임을 진행할 수 있습니다.

## 아키텍쳐 설계도 🔧
<img width="614" alt="image" src="https://github.com/Pirogramming-20/YM/assets/121532823/9ad25ac8-f109-4720-a438-887a18696f38">

## 주요 기능⭐️
- 8가지 게임 (노래 전주 듣고 맞추기, 사진보고 인물 맞추기, 철가방 게임, 없는 게 없는 무한도전 대사 퀴즈, 영화 명장면 맞추기, 몸으로 말해요, 네글자 맞추기, 채팅 빨리보내기) 제공
- 8가지 게임 중 원하는 게임만 골라, 원하는 순서대로 진행 가능 (+ 사회자 정답지 제공, 동일한 문제들과 순서로 재시작 가능 )
- Socket 통신을 이용한 실시간 채팅방
- 로그인 없이 개인도 플레이할 수 있도록 6가지 게임 제공

## 화면 구성 및 API 📺

| 랜딩 페이지 | 이용방법 페이지 |
| :---:         |     :---:      |
| <img width="480px;" height="300px" alt="image" src="https://github.com/Pirogramming-20/YM/assets/121532823/1a8d421c-5825-404d-9aa5-5839704f60fc">  | <img width="480px;" height="300px" alt="image" src="https://github.com/Pirogramming-20/YM/assets/121532823/3266a76b-d102-46ae-ba5d-e3a10b15b403">     |
| <p>www.yozmt.com<br>부트스트랩을 사용해 개발하였으며, 사이트에 처음 입장하는 유저들이 해매지 않도록 설계한 페이지입니다.</p>  | <p>/help<br>요즘MT를 이용해 레크레이션을 진행하는 방법을 자세하게 설명해주는 페이지입니다.</p>     | 

| 회원가입 페이지 | 로그인 페이지 |
| :---:         |     :---:      |
| <img width="480px;" height="300px" alt="image" src="https://github.com/Pirogramming-20/YM/assets/121532823/68c4ae23-c765-403a-96ce-42777774da8b"> | <img src="https://github.com/Pirogramming-20/YM/assets/121532823/b019ce37-453f-417d-8a41-aa99c0df0181" width="480px;" height="300px" alt=""/>     |
| <p>/signup <br>회원가입을 진행할 수 있는 페이지로 유효성과 중복을 체크합니다. </p>     | <p>/login<br>가입한 아이디를 이용해 로그인할 수 있는 페이지입니다.</p>     | 

| 회원 전용 페이지 | 방 생성 페이지 |
| :---:         |     :---:      |
| <img width="480px;" height="300px" src="https://github.com/Pirogramming-20/YM/assets/121532823/6b1ff4bf-1bae-4df5-910a-e72819a74673" alt=""/>   | <img src="" width="350px;" height="350px" alt=""/>     |
| <p>/signup <br>회원가입을 진행할 수 있는 페이지로 유효성과 중복을 체크합니다. </p>     | <p>/login<br>가입한 아이디를 이용해 로그인할 수 있는 페이지입니다.</p>  | 




