const fetchMock = require('fetch-mock');
const { JSDOM } = require('jsdom');
const { fetchDogImages } = require('../../dog.js');
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="dog-images"></div></body></html>');
global.document = dom.window.document;
global.window = dom.window;

describe('fetchDogImages', () => {
  afterEach(() => {
    fetchMock.restore();
  });
  test('fetches dog images and updates the DOM with fake data', async () => {
    fetchMock.mock('http://127.0.0.1:8000/dog?limit=2', {
      status: 200,
      body: [
        {
          id: 'fake-id-1',
          url: 'https://example.com/fake-dog-image-1.jpg',
          width: 500,
          height: 500,
        },
        {
          id: 'fake-id-2',
          url: 'https://example.com/fake-dog-image-2.jpg',
          width: 500,
          height: 500,
        },
      ],
    });
    await fetchDogImages();

    const container = document.getElementById('dog-images');
    const images = container.getElementsByTagName('img');
    expect(images.length).toBe(2);
    expect(images[0].src).toBe('https://example.com/fake-dog-image-1.jpg');
    expect(images[0].alt).toBe('Dog image fake-id-1');
    expect(images[0].style.maxWidth).toBe('200px');
    expect(images[0].style.maxHeight).toBe('200px');
    expect(images[0].style.objectFit).toBe('contain');

    expect(images[1].src).toBe('https://example.com/fake-dog-image-2.jpg');
    expect(images[1].alt).toBe('Dog image fake-id-2');
    expect(images[1].style.maxWidth).toBe('200px');
    expect(images[1].style.maxHeight).toBe('200px');
    expect(images[1].style.objectFit).toBe('contain');
  });

  test('handles fetch errors', async () => {
    fetchMock.mock('http://127.0.0.1:8000/dog?limit=2', 500);
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
    await fetchDogImages();
    expect(consoleSpy).toHaveBeenCalledWith('Error fetching dog images:', expect.any(Error));
    consoleSpy.mockRestore();
  });
});

