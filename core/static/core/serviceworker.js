// Service Worker for Sandeep Mishra Portfolio PWA
// Caches all critical assets for a fully offline experience

const CACHE_NAME = 'sandeep-portfolio-v1';

// All assets to pre-cache on install
const PRECACHE_ASSETS = [
  '/',
  '/static/core/style.css',
  '/static/core/app.js',
  '/static/core/manifest.json',
  '/static/core/icons/icon-192x192.png',
  '/static/core/icons/icon-512x512.png',
];

// ─── INSTALL ──────────────────────────────────────────────────────────────────
// Fired when the Service Worker is first installed.
// We pre-cache all critical assets so the app is ready for offline use immediately.
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW] Pre-caching assets...');
      return cache.addAll(PRECACHE_ASSETS);
    })
  );
  // Immediately take control without waiting for old SW to expire
  self.skipWaiting();
});

// ─── ACTIVATE ─────────────────────────────────────────────────────────────────
// Fired after install. We delete any old, stale caches here.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) =>
      Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => {
            console.log('[SW] Deleting old cache:', name);
            return caches.delete(name);
          })
      )
    )
  );
  // Take control of all open pages immediately
  self.clients.claim();
});

// ─── FETCH ────────────────────────────────────────────────────────────────────
// Intercepts every network request from the page.
// Strategy: Network First → Cache Fallback
//   - We always try to fetch fresh content from the network.
//   - If the network fails (offline), we serve the cached version.
//   - Any successful network response is stored in the cache for future offline use.
self.addEventListener('fetch', (event) => {
  // Only handle GET requests; skip POST/PUT/DELETE (admin forms, etc.)
  if (event.request.method !== 'GET') return;

  // Skip requests to the admin panel — always requires network
  const url = new URL(event.request.url);
  if (url.pathname.startsWith('/secure-admin-portal')) return;

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        // Clone the response before consuming it, so we can store it in cache
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      })
      .catch(() => {
        // Network failed — serve from cache
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            console.log('[SW] Serving from cache (offline):', event.request.url);
            return cachedResponse;
          }
          // If it's a navigation request (visiting a page) and not in cache,
          // serve the cached homepage as a fallback
          if (event.request.destination === 'document') {
            return caches.match('/');
          }
          // Nothing found — let the browser show its default error
          return new Response('Network error occurred', {
            status: 408,
            headers: { 'Content-Type': 'text/plain' },
          });
        });
      })
  );
});
