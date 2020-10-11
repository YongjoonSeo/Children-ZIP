[<img src="../img/banner.JPG" width=100%>](http://childrenzip.site)

![Github](https://img.shields.io/badge/vue-2.6.11-%234FC08D?style=plastic&logo=Vue.js)  ![Github](https://img.shields.io/pypi/djversions/djangorestframework?color=green&label=django&logo=django&style=plastic)  ![Github](https://img.shields.io/badge/MySQL-8.0-%234479A1?style=plastic&logo=mysql)  ![Github](https://img.shields.io/badge/build-passing-brightgreen?style=plastic)

<br>

### Translation: [US](#) [KR](https://github.com/YongjoonSeo/Children-ZIP)

<br>

## 🏠 Daycare center recommendation platform, Children-ZIP

`Children-ZIP` is a web application that recommends a daycare center suitable for users.

Based on the user's location and activity within the website

It recommends daycare centers in a way that combines Content-Based Filtering and User-Based Collaborative Filtering techniques.

Click [here](http://childrenzip.site/) to check the site 🙂

<br>

### Motive

> Through interviews with parents with young children, I learned that when choosing a daycare center, people generally search for information using recommendations from acquaintances or Naver Cafe, but in the process, a lot of information is spread out, which makes them confused.
>
> The project was planned with the hope that parents would be able to see information about daycare centers at a glance, and that they would be able to alleviate the tiredness of exploring daycare centers by recommending centers to parents.

<br>

<br>

## 📌 Table of Contents

- [Tech Stacks](#-Tech-Stacks)
- [Project Structure](#-Project-Structure)
- [ERD](#-ERD)
- [Project Process](#-Project-Process)
- [Main Function](#-Main-Function)
- [Demonstration](#-Demonstration)
- [Browsers Supported](#-Browsers-Supported)
- [Developers](#-Developers)
- [References](#-References)

<br>

<br>

## 🔨 Tech Stacks

<img src="../img/skill_set.png" width=100%>

<br>

<br>

## 🧱 Project Structure

```
.
├── .gitignore # Files that specify a list of files to exclude from Git version management
├── README.md
├── img # Related images folder
├── members_docs # Documentation for team members
├── frontend
│   ├── assets # Uncomplied resource related folders such as style, image, and font
│   ├── pages # Includes application views and paths(routing)
│   │   ├── board # Related board pages
│   │   ├── community # Related community pages
│   │   ├── kinder # Related children and kindergarten pages
│   │   ├── signup # Related account pages
│   │   └── ... # Each page to be routed
│   ├── static # Static files do not change(favicon, robots.txt, sitemap.xml etc.)
│   ├── nuxt.config.js # config file for nuxt.js
│   ├── package.json # Dependencies and scripting
│   ├── layouts # Need to repeat the fixed layout on each page and put it in.
│   └── components # Nust.js scanned and automatically imported
│       ├── Common # Related Header, Footer, Common commponents UI
│       ├── Community # Related community UI
│       ├── Home # Related main UI
│       ├── Kinder # Related children, kindergarten UI
│       ├── Launcher # 런처페이지 Related launcher UI
│       └── Search # 검색 관련 Related search UI
└── backend
    ├── account # Account API
    ├── community # Board API
    ├── kindergartens # Kindergarten API
    ├── spc_pjt # Django setup file
    ├── templates
    ├── Dockerfile # Image file for containerizing Django
    ├── manage.py # Django run file
    ├── requirements.txt # dependency management
    └── bigdata
        ├── analyze.py # Formatting and saving infomation on the crawling kindergarten data
    	├── crawling.py # Code for crawling kindergarten data
    	├── recommend.py # Code for applying recommended algorithm
    	└── requriements.txt # dependency management
```

<br>

<br>

## 📜 ERD

<img src="../img/erd.PNG" width=100%>

[ERD Diagram link](https://www.erdcloud.com/d/a36xRNx6woXE7ukPk)

<br>

<br>

## 🔍 Project Process

<img src="../img/process_struct.png" width=100%>

<br>

<br>

## ✅ Main Function

- Recommended Daycare centers

  - Recommendation system based on user's preferred feature analysis and user's activity analysis
  - Filtering

   <img src="../img/recommend.gif" width=50%>

- Searching national Daycare centers

  - Bookmark
  - Visualization of information such as average number of years of service for teachers, number of infants per teacher, and number of CCTVs per 100m²
  - Write and view ratings and reviews of Daycare center

   <img src="../img/kinder_info.gif" width=50%>

- Community

  - Search and create the desired board

   <img src="../img/create_board.gif" width=50%>

  - Add and delete posts and comments

   <img src="../img/create_post.gif" width=50%>

<br>

<br>

## 🎥 Demonstration

> Click the image below to watch the demo video.

[![Children-ZIP Demo video](https://img.youtube.com/vi/qOEFXODnMOA/hqdefault.jpg)](https://youtu.be/qOEFXODnMOA)

<br>

<br>

## 🌏 Browsers Supported

| <img src='../img/chrome.png' width=60> | <img src='../img/firefox.png' width=60> | <img src='../img/edge.png' width=60> | <img src='../img/safari.png' width=60> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            latest                            |                            latest                            |                            latest                            |                            latest                            |

<br>

<br>

## 👩‍💻 Developers

- MyeongSeok KIM (https://github.com/msnodeve)
- Yeseul Heo (https://github.com/yeseul4072)
- Jihoon Seo (https://github.com/sjh7141)
- SungMin Ahn (https://github.com/asm9677)
- Yongjoon Seo (https://github.com/YongjoonSeo)

<br>

<br>

## 🔗 References

- [Our Development Story](https://www.notion.so/msnodeve/GG-ZIP-4755010382c943ec9444ecdb22ea01c5)