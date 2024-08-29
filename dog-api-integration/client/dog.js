// 獲取並顯示來自 API 的圖片
async function fetchDogImages() {
  try {
    const response = await fetch('http://127.0.0.1:8000/dog?limit=2');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const images = await response.json();
    const container = document.getElementById('dog-images');

    images.forEach(image => {
      const imageContainer = document.createElement('div');
      imageContainer.className = 'image-container';

      const img = document.createElement('img');
      img.src = image.url;
      img.alt = `Dog image ${image.id}`;
      img.style.maxWidth = '200px';
      img.style.maxHeight = '200px';
      img.style.objectFit = 'contain';


      imageContainer.appendChild(img);
      container.appendChild(imageContainer);
    });
  } catch (error) {
    console.error('Error fetching dog images:', error);
  }
}

// 處理文件上傳並顯示圖片
function handleFileUpload(event) {
  const files = event.target.files;
  const container = document.getElementById('dog-images');

  Array.from(files).forEach(file => {
    const reader = new FileReader();

    reader.onload = (e) => {
      const imageContainer = document.createElement('div');
      imageContainer.className = 'image-container';

      const img = document.createElement('img');
      img.src = e.target.result;
      img.alt = file.name;
      img.style.maxWidth = '200px';
      img.style.maxHeight = '200px';
      img.style.objectFit = 'contain';
      imageContainer.appendChild(img);
      container.appendChild(imageContainer);
    };

    reader.readAsDataURL(file);
  });
}

module.exports = { fetchDogImages, handleFileUpload };

