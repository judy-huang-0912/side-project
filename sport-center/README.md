# API integration and simple fastapi server (frontend + api + unit test)

## Table of contents

- <a href="#tech-stack">使用的套件列表</a>
- <a href="#getting-started">如何開始</a>
- <a href="#system-architecture">架構圖</a>
- <a href="#prerequisite">背景知識</a>

<h2 id="tech-stack">使用的套件列表</h2>

- [Playwright](https://github.com/nodejs): Web 測試以及自動化的框架
- [python.env](https://hackmd.io/@ME1splK_SaS67P2I6U7h_w/HyScsMQ6h):設置環境變量，存放一些比較敏感的資訊
- [pytest](https://docs.pytest.org/en/stable/):python的測試框架


<h2 id="getting-started">Getting Started</h2>

#### 啟動虛擬環境
```bash
source ~/.bash_profile
pyenv activate myenv
```
#### 找到當前路徑
#### 執行程式
```bash
cd Desktop/jupyter/sport-center
python3 test.cookies.py
```

<h2 id="system-architecture">System Architecture</h2>


使用者訪問網站時的 Cookie 工作流程圖

![Cookies Test](screenshot/cookies%20test.png)


<h2 id="prerequisite">Prerequisite Knowledge</h2>

#### Basics of Next.js framework
- [Cookies的操作](https://playwright.dev/python/docs/api/class-browsercontext)
- [什麼是Cookies](https://blog.csdn.net/m0_62695120/article/details/124009940)
- [使用 HTTP Cookie](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Cookies)









