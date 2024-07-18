// 引入 fetchMock 和 jsdom 环境
const fetchMock = require('fetch-mock');
const { JSDOM } = require('jsdom');

// 引入要测试的函数
const { fetchDogImages } = require('../../dog.js');

// 设置 jsdom 环境
const dom = new JSDOM('<!DOCTYPE html><div id="dog-images"></div>');
global.document = dom.window.document;
global.window = dom.window;

describe('fetchDogImages', () => {
  afterEach(() => {
    fetchMock.restore(); // 重置 fetchMock
  });

  test('fetches dog images and updates the DOM', async () => {
    // 模拟 API 响应
    fetchMock.mock('http://127.0.0.1:3000/dog?limit=2', {
      status: 200,
      body: [
        {
          id: '1',
          url: 'http://example.com/dog1.jpg',
          width: 800,
          height: 600,
        },
        {
          id: '2',
          url: 'http://example.com/dog2.jpg',
          width: 800,
          height: 600,
        },
      ],
    });

    // 调用 fetchDogImages
    await fetchDogImages();

    // 获取更新后的 DOM
    const container = document.getElementById('dog-images');
    const images = container.getElementsByTagName('img');

    // 验证 DOM 更新
    expect(images.length).toBe(2);
    expect(images[0].src).toBe('http://example.com/dog1.jpg');
    expect(images[0].alt).toBe('Dog image 1');
    expect(images[0].width).toBe(200);
    expect(images[0].height).toBe(150);
    expect(images[1].src).toBe('http://example.com/dog2.jpg');
    expect(images[1].alt).toBe('Dog image 2');
    expect(images[1].width).toBe(200);
    expect(images[1].height).toBe(150);
  });

  test('handles fetch errors', async () => {
    // 模拟 API 错误响应
    fetchMock.mock('http://127.0.0.1:3000/dog?limit=2', 500);

    // 捕获 console.error 输出
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    // 调用 fetchDogImages
    await fetchDogImages();

    // 验证 console.error 被调用
    expect(consoleSpy).toHaveBeenCalledWith('Error fetching dog images:', expect.any(Error));

    // 恢复 console.error
    consoleSpy.mockRestore();
  });
});
