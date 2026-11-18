import React from 'react';
import { Search, Flame, Users, Sparkles, X } from 'lucide-react';

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
  totalGames,
}) => {
  const playerPresets = [
    { label: 'الكل', value: null },
    { label: '2 لعيبة (كابلز)', value: 2 },
    { label: '3 - 4 أفراد', value: 4 },
    { label: '5 - 6 أفراد', value: 6 },
    { label: 'شلة كبيرة (8+)', value: 8 },
  ];

  return (
    <section className="relative overflow-hidden pt-8 pb-6 px-4 sm:px-6 lg:px-8 border-b border-gold/15">
      {/* Background ambient lighting */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-gold/10 rounded-full blur-[100px] pointer-events-none -z-10"></div>

      <div className="max-w-4xl mx-auto text-center">
        
        {/* Banner Tag */}
        <div className="inline-flex items-center gap-2 bg-[#121214] border border-gold/30 px-3.5 py-1.5 rounded-full mb-4 shadow-sm">
          <Flame className="w-4 h-4 text-amber-400 fill-amber-400" />
          <span className="text-xs sm:text-sm font-medium text-gold-light">
            سهرتك في عماد أفندي متتنسيش • {totalGames} لعبة أصلية في خدمتك
          </span>
        </div>

        {/* Headline */}
        <h2 className="text-2xl sm:text-4xl font-extrabold font-kufi text-white tracking-tight mb-3">
          مش عارفين تلعبوا إيه؟ <span className="text-gold">اختاروا اللعبة المناسبة لقعدتكم!</span>
        </h2>
        <p className="text-sm sm:text-base text-neutral-300 max-w-2xl mx-auto mb-6 font-light">
          تصفح كتالوج الألعاب بالكامل، اعرف القوانين وطريقة اللعب خطوة بخطوة، أو اطلب من كابتن الألعاب الذكي يرشح لك اللعبة المثالية على طاولتك.
        </p>

        {/* Instant Search Bar */}
        <div className="relative max-w-xl mx-auto mb-5">
          <div className="absolute inset-y-0 right-0 pr-4 flex items-center pointer-events-none">
            <Search className="w-5 h-5 text-gold/70" />
          </div>
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder="ابحث باسم اللعبة، النوع (ضحك، كابلز، سينما)، أو عدد اللعيبة..."
            className="w-full pl-10 pr-12 py-3.5 bg-[#121214]/90 border border-gold/30 focus:border-gold rounded-2xl text-sm sm:text-base text-white placeholder-neutral-500 focus:outline-none focus:ring-2 focus:ring-gold/30 transition-all shadow-inner"
          />
          {searchQuery && (
            <button
              onClick={() => onSearchChange('')}
              className="absolute inset-y-0 left-0 pl-3 flex items-center text-neutral-400 hover:text-white"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* Player Count Quick Selector */}
        <div className="flex items-center justify-center flex-wrap gap-2 pt-1">
          <span className="text-xs text-neutral-400 flex items-center gap-1 font-medium ml-1">
            <Users className="w-3.5 h-3.5 text-gold" />
            عدد أفراد الطاولة:
          </span>
          {playerPresets.map((preset) => {
            const isSelected = selectedPlayerCount === preset.value;
            return (
              <button
                key={preset.label}
                onClick={() => onPlayerCountSelect(isSelected && preset.value !== null ? null : preset.value)}
                className={`text-xs px-3 py-1.5 rounded-full border transition-all active:scale-95 ${
                  isSelected
                    ? 'bg-gold text-[#0B0B0C] border-gold font-bold shadow-gold-glow'
                    : 'bg-[#121214] text-neutral-300 border-gold/20 hover:border-gold/50'
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
