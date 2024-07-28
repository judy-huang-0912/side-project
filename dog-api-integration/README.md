# API integration and simple fastapi server (frontend + api + unit test)

## Table of contents

- <a href="#tech-stack">使用的套件列表</a>
- <a href="#getting-started">如何開始</a>
- <a href="#system-architecture">架構圖</a>
- <a href="#prerequisite">背景知識</a>

<h2 id="tech-stack">使用的套件列表</h2>


- [Postman](https://github.com/postmanlabs/postman-app-support): 測api的工具
- [FastApi](https://github.com/tiangolo/fastapi/blob/master/README.md): 建立api
- [FetcgMock](https://github.com/wheresrhys/fetch-mock): mock打http的request
- [JsDom](https://github.com/jsdom/jsdom): 建立虛擬的DOM環境
- [Jest](https://trpc.io): js測試Unittest的框架
- [node.js](https://github.com/nodejs): 在瀏覽器之外執行Js程式的工具
- [Playwright](https://github.com/nodejs):  Web 測試以及自動化的框架

<h2 id="getting-started">Getting Started</h2>


#### 啟動虛擬環境

```bash
source ~/.bash_profile
pyenv activate myenv
```
```bash
npm install -g serve
cd Desktop/dog-api-integration/client
serve
```

<h2 id="system-architecture">System Architecture</h2>
[TODO] Integration

前後端的溝通、資料流向，開API

![full-stack-architecture Overview](screenshot/full-stack-architecture-overview.png)

前端做了哪些測試以及使用哪些工具

![Frontend Architecture Overview](screenshot/frontend-architecture-overview.png)

後端 API Server 做了哪些測試以及使用哪些工具

![Backend Architecture Overview](screenshot/backend-architecture-overview.png)


<h2 id="prerequisite">Prerequisite Knowledge</h2>

- [網路運作原理](https://developer.mozilla.org/zh-TW/docs/Learn/Getting_started_with_the_web/How_the_Web_works)：網路如何運作
- [介紹HTML](https://developer.mozilla.org/zh-TW/docs/Learn/HTML/Introduction_to_HTML)：什麼是HTML
- [測試金字塔](https://medium.com/@nathankpeck/microservice-testing-unit-tests-d795194fe14e):

  unit test 測試函數是否按照預期運作

  E2E Test 測試是否正確顯示畫面
- [FastApi](https://github.com/tiangolo/fastapi/blob/master/README.md) :開API
- [Uvicorn](https://stackoverflow.com/questions/71435960/what-is-the-purpose-of-uvicorn):部署Api
- [Mock Api](https://ithelp.ithome.com.tw/m/articles/10270202):模擬 API request 和 response
- [Mock DOM](https://ithelp.ithome.com.tw/m/articles/10270202):不用打開瀏覽器，檢查函數是否按照預期運作








