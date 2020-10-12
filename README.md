[<img src="./img/banner.JPG" width=100%>](https://childrenzip.site)

![Github](https://img.shields.io/badge/vue-2.6.11-%234FC08D?style=plastic&logo=Vue.js)  ![Github](https://img.shields.io/pypi/djversions/djangorestframework?color=green&label=django&logo=django&style=plastic)  ![Github](https://img.shields.io/badge/MySQL-8.0-%234479A1?style=plastic&logo=mysql)  ![Github](https://img.shields.io/badge/build-passing-brightgreen?style=plastic)

<br>

### 번역: [KR](#) [US](./docs)

<br>

## 🏠 어린이집 추천 플랫폼, 어린이ZIP

`어린이zip`은 사용자에게 맞는 어린이집을 추천해주는 웹 애플리케이션입니다.

사용자의 지역과 웹사이트 내에서의 활동 내역을 기반으로 하여

Content-Based Filtering 기법과 User-Based Collaborative Filtering 기법을 혼합한 방식으로 어린이집을 추천해줍니다.

[여기](https://childrenzip.site/)를 클릭해 사이트를 확인하세요 🙂

<br>

### 개발 동기

> 어린 자녀를 둔 부모님과의 인터뷰를 통해 어린이집을 선택할 때 일반적으로 지인의 추천 혹은 네이버 카페 등을 이용해 정보를 탐색하지만 그 과정에서 많은 정보가 퍼져있어 곤혹을 겪는다는 사실을 알게되었습니다. 
>
> 어린이집 정보를 한 눈에 볼 수 있고, 또 자녀에게 꼭 맞는 어린이집을 추천해줌으로써 부모님들이 어린이집을 탐색할 때 느끼는 피곤함을 덜 수 있지 않을까? 라는 생각으로 프로젝트를 기획하였습니다. 

<br>

<br>

## 📌 목차 

- [사용된 기술](#-사용된-기술)
- [프로젝트 구조](#-프로젝트-구조)
- [ERD](#-erd)
- [프로젝트 프로세스](#-프로젝트-프로세스)
- [주요 기능](#-주요-기능)
- [시연 영상](#-시연-영상)
- [지원하는 브라우저](#-지원하는-브라우저)
- [개발자](#-개발자)
- [참고](#-참고)

<br>

<br>

## 🔨 사용된 기술

<img src="./img/skill_set.png" width=100%>

<br>

<br>

## 🧱 프로젝트 구조

```
.
├── .gitignore # Git 버전 관리에서 제외할 파일 목록을 지정하는 파일
├── README.md
├── img # 이미지 관련 폴더
├── members_docs # 팀원 문서화
├── frontend
│   ├── assets # style, image, font 등 컴파일 되지 않는 리소스 관련 폴더
│   ├── pages # 응용프로그램 보기 및 경로(라우팅)을 포함
│   │   ├── board # 게시판 관련 페이지
│   │   ├── community # 커뮤니티 관련 페이지
│   │   ├── kinder # 어린이집 관련 페이지
│   │   ├── signup # 계정관련 페이지
│   │   └── ... # 라우팅 될 각 페이지
│   ├── static # 변경되지 않는 정적 파일(favicon, robots.txt, sitemap.xml 등)
│   ├── nuxt.config.js # Nuxt.js 에 대한 config 파일
│   ├── package.json # Vue에서 사용하는 것과 동일하게 종속성 및 스크립트 작성
│   ├── layouts # 각 page에 고정된 레이아웃을 반복해서 설정해서 넣어줘야 할경우
│   └── components # Nuxt.js가 스캔해서 자동으로 가져옴
│       ├── Common # 헤더, 푸터, 공통 컴포넌트 관련
│       ├── Community # 커뮤니티 관련
│       ├── Home # 메인페이지 관련
│       ├── Kinder # 어린이집 관련
│       ├── Launcher # 런처페이지
│       └── Search # 검색 관련
└── backend
    ├── account # 계정 API
    ├── community # 게시판 API
    ├── kindergartens # 어린이집 API
    ├── spc_pjt # Django 설정 파일
    ├── templates
    ├── Dockerfile # Django 이미지 작업
    ├── manage.py # Django 실행 파일
    ├── requirements.txt # 의존성 관리
    └── bigdata
        ├── analyze.py # 크롤링해온 어린이집 정보 정형화 및 저장
    	├── crawling.py # 어린이집 정보 크롤링 할 코드
    	├── recommend.py # 추천알고리즘을 적용 할 코드
    	└── requriements.txt # 의존성 관리
    	
```

<br>

<br>

## 📜 ERD

<img src="./img/erd.PNG" width=100%>

[ERD Diagram link](https://www.erdcloud.com/d/a36xRNx6woXE7ukPk)

<br>

<br>

## 🔍 프로젝트 프로세스

<img src="./img/process_struct.png" width=100%>

<br>

<br>

## ✅ 주요 기능

- 어린이집 추천
  - 사용자가 선호하는 특징 분석, 사이트 내 활동 분석을 기반으로 한 추천 시스템 
  - 필터 기능
  # <img src="./img/recommend.gif" width=50%>  

- 전국 어린이집 조회 
  - 어린이집 찜 기능
  - 교사평균 근속연수, 교사 1인당 유아 수, 100m²당 CCTV수 등 정보 시각화
  - 어린이집 평점, 리뷰 작성 및 조회
  # <img src="./img/kinder_info.gif" width=50%>  

- 커뮤니티
  - 원하는 게시판 조회 및 생성
  # <img src="./img/create_board.gif" width=50%>  
  - 게시글 및 댓글 추가 삭제    
  # <img src="./img/create_post.gif" width=50%>

<br>

<br>

## 🎥 시연 영상

> 아래 이미지를 클릭하면 시연 영상을 시청할 수 있습니다.

[![어린이ZIP 시연영상](https://img.youtube.com/vi/qOEFXODnMOA/hqdefault.jpg)](https://youtu.be/qOEFXODnMOA)

<br>

<br>

## 🌏 지원하는 브라우저

| <img src='./img/chrome.png' width=60> | <img src='./img/firefox.png' width=60> | <img src='./img/edge.png' width=60> | <img src='./img/safari.png' width=60> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            latest                            |                            latest                            |                            latest                            |                            latest                            |

<br>

<br>

## 👩‍💻 개발자

- 김명석 (https://github.com/msnodeve)
- 허예슬 (https://github.com/yeseul4072)
- 서지훈 (https://github.com/sjh7141)
- 안성민 (https://github.com/asm9677)
- 서용준 (https://github.com/YongjoonSeo)

<br>

<br>

## 🔗 참고

- [우리들의 개발이야기](https://www.notion.so/msnodeve/GG-ZIP-4755010382c943ec9444ecdb22ea01c5)