import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// Automated Cache Buster & Migration Engine
const APP_VERSION = 'v2026.11.21-0605-luxury';
const storedVersion = localStorage.getItem('emad_afandi_version');

if (storedVersion !== APP_VERSION) {
  console.log('[App] Upgrading client version to', APP_VERSION);
  localStorage.setItem('emad_afandi_version', APP_VERSION);

  // Purge legacy caches on client to force immediate fresh assets
  if ('caches' in window) {
    caches.keys().then((names) => {
      names.forEach((name) => caches.delete(name));
    });
  }
}

// Service Worker Registration with Immediate Update Trigger
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/sw.js')
      .then((reg) => {
        reg.update(); // Always check for updated sw on reload
        reg.addEventListener('updatefound', () => {
          const newWorker = reg.installing;
          if (newWorker) {
            newWorker.addEventListener('statechange', () => {
              if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                // Instantly activate without waiting
                window.location.reload();
              }
            });
          }
        });
      })
      .catch((err) => {
        console.warn('SW registration bypassed:', err);
      });
  });
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
