async function fetchDogImages() {
  try {
    const response = await fetch('http://127.0.0.1:8000/dog?limit=2');
    if (!response.ok) {
      throw new Error('response error');
    }
    const images = await response.json();
    const container = document.getElementById('dog-images');

    images.forEach(image => {
      const imageContainer = document.createElement('div');
      imageContainer.className = 'image-container';

      const img = document.createElement('img');
      img.src = image.url;
      img.alt = `dog-image ${image.id}`;
      img.style.maxWidth = '200px';
      img.style.maxHeight = '200px';
      img.style.objectFit = 'contain';

      imageContainer.appendChild(img);
      container.appendChild(imageContainer);
    });
  } catch (error) {
    console.error('request dog image error:', error);
  }
}

module.exports = { fetchDogImages };
fetchDogImages();


