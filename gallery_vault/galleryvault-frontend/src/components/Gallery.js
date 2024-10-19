// src/components/Gallery.js

import React, { useState, useEffect } from 'react';
import API from '../api';

function Gallery() {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    const fetchPhotos = async () => {
      try {
        const response = await API.get('photos/');
        setPhotos(response.data);
      } catch (error) {
        console.error('Error fetching photos', error);
        alert('Error fetching photos');
      }
    };

    fetchPhotos();
  }, []);

  return (
    <div>
      <h2>Your Photo Gallery</h2>
      <div className="gallery">
        {photos.length > 0 ? (
          photos.map((photo, index) => (
            <div key={index} className="photo-item">
              <img
                src={`http://localhost:8000${photo.image}`}
                alt={`Uploaded on ${photo.uploaded_at}`}
                width="200"
                height="200"
              />
              <p>Uploaded on: {new Date(photo.uploaded_at).toLocaleString()}</p>
            </div>
          ))
        ) : (
          <p>No photos uploaded yet.</p>
        )}
      </div>
    </div>
  );
}

export default Gallery;
