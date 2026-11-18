// ☕ كافيه ومحمصة عماد أفندي - Service Worker Offline Engine
// Generated automatically by sync_game_assets.py
const CACHE_NAME = 'emad-afandi-v202611181648';
const ASSETS_TO_CACHE = [
  "/",
  "/index.html",
  "/logo.webp",
  "/data/games.json",
  "/games/mesh-mertahlak.webp",
  "/games/el-joker.webp",
  "/games/kadab.webp",
  "/games/met7awech.webp",
  "/games/msh-hanbatel.webp",
  "/games/wala3a.webp",
  "/games/est7ala.webp",
  "/games/byegy-menno.webp",
  "/games/ana-mesh-arafny.webp",
  "/games/shake-me.webp",
  "/games/el-le3ba-el-qadya.webp",
  "/games/tala3-el-mostakhabby.webp",
  "/games/ew3a-weshak.webp",
  "/games/hareedy.webp",
  "/games/el-3awz.webp",
  "/games/2ool-aw-e3mel.webp",
  "/games/2oolameme-2.webp",
  "/games/casino-al3ab.webp",
  "/games/kataflam.webp",
  "/games/tasali-cinema.webp",
  "/games/raz3-el-gomhoor.webp",
  "/games/couples-walaken.webp",
  "/games/mawada-w-rahma.webp",
  "/games/qabl-el-hewar.webp",
  "/games/pick-a-date.webp",
  "/games/girls-walaken.webp",
  "/games/waraa-el-gareema.webp",
  "/games/khufu.webp",
  "/games/mansa.webp",
  "/games/kelmet-el-ser-mostathmer.webp",
  "/games/tomouhy.webp",
  "/games/skrew.webp",
  "/games/autobeez.webp",
  "/games/sahseh.webp",
  "/games/3arosty.webp",
  "/games/tasali-kelma-khatar.webp",
  "/games/tasali-3andalib.webp",
  "/games/tasali-haqeeqa.webp",
  "/games/tasali-system.webp",
  "/games/tasali-dehk.webp",
  "/games/tasali-ramadan.webp",
  "/games/starting-chess.webp",
  "/games/original-domino.webp",
  "/games/mawsoo3at.webp"
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[Service Worker] Caching all game assets for offline cafe experience...');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[Service Worker] Removing old cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        if (
          !networkResponse ||
          networkResponse.status !== 200 ||
          networkResponse.type !== 'basic'
        ) {
          return networkResponse;
        }
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      }).catch(() => {
        return caches.match('/index.html');
      });
    })
  );
});
