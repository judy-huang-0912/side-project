async function fetchDogImages() {
  try {
    const response = await fetch('http://127.0.0.1:3000/dog?limit=2');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const images = await response.json();
    const container = document.getElementById('dog-images');
    images.forEach(image => {
      const img = document.createElement('img');
      img.src = image.url;
      img.alt = `Dog image ${image.id}`;
      img.width = image.width / 4;
      img.height = image.height / 4;
      container.appendChild(img);
    });
  } catch (error) {
    console.error('Error fetching dog images:', error);
  }
}

module.exports = { fetchDogImages };
