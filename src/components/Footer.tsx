import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer className="w-full bg-[#070708] border-t border-gold/15 py-8 px-4 flex flex-col items-center justify-center mt-12">
      <div className="relative group flex items-center justify-center">
        <div className="absolute -inset-2 bg-gold/10 rounded-full blur-md opacity-40 group-hover:opacity-80 transition duration-300 pointer-events-none"></div>
        <img 
          src="/logo.webp" 
          alt="كافيه عماد أفندي" 
          className="relative h-11 sm:h-13 w-auto object-contain opacity-85 hover:opacity-100 transition-opacity drop-shadow-[0_2px_10px_rgba(212,175,55,0.25)]" 
        />
      </div>
    </footer>
  );
};
