import React from 'react';
import { Sparkles, Coffee } from 'lucide-react';

interface NavbarProps {
  onOpenAIChat: () => void;
  gameCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({ onOpenAIChat }) => {
  return (
    <header className="sticky top-0 z-40 w-full glass-panel border-b border-gold/20 shadow-md">
      <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 h-14 sm:h-18 flex items-center justify-between">
        
        {/* Logo and Brand Identity */}
        <div className="flex items-center gap-2 sm:gap-3">
          <div className="relative group">
            <div className="absolute -inset-1 bg-gradient-to-r from-gold to-gold-dark rounded-full blur opacity-30 group-hover:opacity-75 transition duration-300"></div>
            <img 
              src="/logo.webp" 
              alt="كافيه عماد أفندي" 
              className="relative h-9 sm:h-11 w-auto object-contain drop-shadow-[0_2px_8px_rgba(212,175,55,0.4)]"
            />
          </div>
          <div className="flex items-center gap-1.5 sm:gap-2">
            <h1 className="text-base sm:text-xl font-bold font-kufi text-white tracking-wide">
              ألعاب <span className="text-gold">عماد أفندي</span>
            </h1>
            <span className="inline-flex items-center gap-1 text-[10px] sm:text-[11px] font-semibold bg-gold/15 text-gold-light border border-gold/30 px-2 py-0.5 rounded-full">
              <Coffee className="w-2.5 h-2.5 sm:w-3 sm:h-3 text-gold" />
              كفر الشيخ
            </span>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={onOpenAIChat}
            className="flex items-center gap-1.5 bg-gradient-to-r from-gold to-gold-dark hover:from-gold-light hover:to-gold text-[#0B0806] font-semibold text-xs sm:text-sm px-3 py-1.5 sm:px-4 sm:py-2 rounded-full shadow-gold-glow transition-all active:scale-95 duration-200"
          >
            <Sparkles className="w-3.5 h-3.5 fill-current animate-pulse" />
            <span className="font-bold">كابتن الألعاب</span>
          </button>
        </div>

      </div>
    </header>
  );
};
