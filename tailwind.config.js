/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        gold: {
          light: '#E5C378',
          DEFAULT: '#D4AF37',
          dark: '#AA7C11',
          heritage: '#C5A869',
        },
        espresso: {
          DEFAULT: '#0B0B0C',
          card: '#121214',
          hover: '#1A1612',
          border: 'rgba(212, 175, 55, 0.2)',
          borderHover: 'rgba(212, 175, 55, 0.5)',
        }
      },
      fontFamily: {
        arabic: ['"IBM Plex Sans Arabic"', 'system-ui', 'sans-serif'],
        kufi: ['"Noto Kufi Arabic"', 'sans-serif'],
        numbers: ['Bahnschrift', 'sans-serif'],
      },
      boxShadow: {
        'gold-glow': '0 0 25px -5px rgba(212, 175, 55, 0.25)',
        'gold-glow-lg': '0 0 40px -5px rgba(212, 175, 55, 0.4)',
      }
    },
  },
  plugins: [],
}
