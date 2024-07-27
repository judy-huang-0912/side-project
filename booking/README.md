# booking ticket (end-to-end testing practice)

## Table of contents

- <a href="#tech-stack">使用的套件列表</a>
- <a href="#getting-started">如何開始</a>
- <a href="#system-architecture">架構圖</a>
- <a href="#prerequisite">背景知識</a>

<h2 id="tech-stack">使用的套件列表</h2>


- [Playwright](https://github.com/nodejs): Web 測試以及自動化的框架
- [line notify api](https://notify-bot.line.me/doc/en/): 呼叫API自動傳送訊息

<h2 id="getting-started">Getting Started</h2>

#### 啟動虛擬環境
```bash
source ~/.bash_profile
pyenv activate myenv
```
#### cd為切換到當前目錄
#### 執行程式
```bash
cd Desktop/jupyter/booking
python3 fly.py
```

<h2 id="system-architecture">System Architecture</h2>

E2E測試流程

![E2E Test](./screenshot/E2E%20Test%20.png)

<h2 id="prerequisite">Prerequisite Knowledge</h2>

- [測試金字塔](https://medium.com/@nathankpeck/microservice-testing-unit-tests-d795194fe14e)
- [Playwright官方文件](https://playwright.dev/python/)
- [Playwright操作文章](https://hackmd.io/@kY8Wpop3SHWnMmEn8sqGIA/SkDIi50th#1CSS%E5%AE%9A%E4%BD%8D)



