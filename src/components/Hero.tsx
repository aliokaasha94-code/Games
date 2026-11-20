import React from 'react';
import { Search, Users, X } from 'lucide-react';

interface HeroProps {
  searchQuery: string;
  onSearchChange: (q: string) => void;
  selectedPlayerCount: number | null;
  onPlayerCountSelect: (count: number | null) => void;
  totalGames: number;
}

export const Hero: React.FC<HeroProps> = ({
  searchQuery,
  onSearchChange,
  selectedPlayerCount,
  onPlayerCountSelect,
}) => {
  const playerPresets = [
    { label: 'الكل', value: null },
    { label: '٢ لاعبين', value: 2 },
    { label: '٣ - ٤ أفراد', value: 4 },
    { label: '٥ - ٦ أفراد', value: 6 },
    { label: 'شلة ٨+', value: 8 },
  ];

  return (
    <section className="relative px-3 sm:px-6 pt-3 pb-2.5 bg-[#0D0A08]/40 border-b border-gold/15">
      <div className="max-w-4xl mx-auto flex flex-col gap-2.5">
        
        {/* Compact Search Bar */}
        <div className="relative w-full">
          <div className="absolute inset-y-0 right-0 pr-3.5 flex items-center pointer-events-none">
            <Search className="w-4 h-4 text-gold/70" />
          </div>
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder="ابحث عن لعبة (مثلاً: ضحك، شلة، كابلز)..."
            className="w-full pl-9 pr-10 py-2 sm:py-2.5 bg-[#14100D] border border-gold/25 focus:border-gold rounded-xl text-xs sm:text-sm text-white placeholder-neutral-500 focus:outline-none focus:ring-1 focus:ring-gold/30 transition-all shadow-inner"
          />
          {searchQuery && (
            <button
              onClick={() => onSearchChange('')}
              className="absolute inset-y-0 left-0 pl-3 flex items-center text-neutral-400 hover:text-white"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>

        {/* Player Count Chips (Horizontally Scrollable on Mobile) */}
        <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-0.5">
          <span className="text-[11px] text-neutral-400 flex items-center gap-1 font-medium ml-1 whitespace-nowrap">
            <Users className="w-3 h-3 text-gold" />
            اللعيبة:
          </span>
          {playerPresets.map((preset) => {
            const isSelected = selectedPlayerCount === preset.value;
            return (
              <button
                key={preset.label}
                onClick={() => onPlayerCountSelect(isSelected && preset.value !== null ? null : preset.value)}
                className={`text-[11px] sm:text-xs px-2.5 py-1 rounded-lg border whitespace-nowrap transition-all active:scale-95 duration-150 ${
                  isSelected
                    ? 'bg-gradient-to-r from-gold to-gold-dark text-[#0B0806] border-gold font-bold shadow-[0_2px_8px_rgba(212,175,55,0.3)]'
                    : 'bg-[#14100D] text-neutral-300 border-gold/15 hover:border-gold/40 hover:text-white'
                }`}
              >
                {preset.label}
              </button>
            );
          })}
        </div>

      </div>
    </section>
  );
};
