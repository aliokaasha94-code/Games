import React from 'react';
import { Sparkles, MessageSquare, Coffee } from 'lucide-react';

interface NavbarProps {
  onOpenAIChat: () => void;
  gameCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({ onOpenAIChat, gameCount }) => {
  return (
    <header className="sticky top-0 z-40 w-full glass-panel border-b border-gold/20 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
        
        {/* Logo and Brand Identity */}
        <div className="flex items-center gap-3.5">
          <div className="relative group">
            <div className="absolute -inset-1 bg-gradient-to-r from-gold to-gold-dark rounded-full blur opacity-30 group-hover:opacity-75 transition duration-300"></div>
            <img 
              src="/logo.webp" 
              alt="كافيه ومحمصة عماد أفندي" 
              className="relative h-12 w-auto object-contain drop-shadow-[0_2px_8px_rgba(212,175,55,0.4)]"
            />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl sm:text-2xl font-bold font-kufi text-white tracking-wide">
                ألعاب <span className="text-gold">عماد أفندي</span>
              </h1>
              <span className="hidden sm:inline-flex items-center gap-1 text-[11px] font-semibold bg-gold/15 text-gold-light border border-gold/30 px-2 py-0.5 rounded-full">
                <Coffee className="w-3 h-3 text-gold" />
                كفر الشيخ
              </span>
            </div>
            <p className="text-xs text-neutral-400 font-light hidden sm:block">
              الدليل التفاعلي الكامل لألعاب الطاولة والكروت في الكافيه
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2.5">
          <button
            onClick={onOpenAIChat}
            className="flex items-center gap-2 bg-gradient-to-r from-gold to-gold-dark hover:from-gold-light hover:to-gold text-[#0B0B0C] font-semibold text-xs sm:text-sm px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-full shadow-gold-glow transition-all active:scale-95 duration-200"
          >
            <Sparkles className="w-4 h-4 fill-current animate-pulse" />
            <span className="font-bold">كابتن الألعاب الذكي</span>
          </button>
        </div>

      </div>
    </header>
  );
};
