import React from 'react';
import { Users, Clock, ArrowLeft, Building2 } from 'lucide-react';
import { Game } from '../types';
import { CategoryIcon3D } from './CategoryIcon3D';

interface GameCardProps {
  game: Game;
  onSelect: (game: Game) => void;
}

export const GameCard: React.FC<GameCardProps> = ({ game, onSelect }) => {
  return (
    <div 
      onClick={() => onSelect(game)}
      className="group relative flex flex-col justify-between bg-[#120E0B] border border-gold/25 hover:border-gold/70 rounded-2xl overflow-hidden cursor-pointer transition-all duration-300 hover:-translate-y-1.5 hover:shadow-[0_8px_30px_rgba(212,175,55,0.22)] shadow-lg"
    >
      {/* Golden hairline hover illumination */}
      <div className="absolute inset-0 bg-gradient-to-b from-gold/10 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-20"></div>

      <div>
        {/* Unified Luxury Dark Studio Pedestal (Eliminates jarring white boxes completely) */}
        <div className="relative p-3.5 sm:p-4 bg-gradient-to-b from-[#1C1713] via-[#14100D] to-[#0D0A08] border-b border-gold/15 overflow-hidden">
          {/* Subtle warm golden radial spotlight behind the game box */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(212,175,55,0.18)_0%,rgba(28,23,19,0.05)_55%,transparent_75%)] pointer-events-none"></div>

          {/* Pedestal Container (Seamless dark backdrop with subtle ground reflection shadow) */}
          <div className="relative aspect-square w-full rounded-xl flex items-center justify-center p-3 overflow-hidden">
            <img 
              src={game.image} 
              alt={game.name}
              loading="lazy"
              className="w-full h-full object-contain filter drop-shadow-[0_12px_24px_rgba(0,0,0,0.85)] group-hover:scale-105 group-hover:-translate-y-1 transition-all duration-500 ease-out z-10"
            />
            {/* Soft oval ground shadow underneath the game box */}
            <div className="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-3/4 h-3 bg-black/70 rounded-full blur-md pointer-events-none"></div>
          </div>

          {/* Floating Category Pill with mini 3D icon */}
          <span className="absolute top-4 right-4 flex items-center gap-1.5 text-[11px] font-bold bg-[#0B0806]/90 text-gold-light border border-gold/40 px-2.5 py-1 rounded-full backdrop-blur-md shadow-md z-20">
            <CategoryIcon3D categoryId={game.category} className="w-3.5 h-3.5 object-contain" />
            <span>{game.category_ar}</span>
          </span>

          {/* Age Rating Pill */}
          <span className="absolute top-4 left-4 text-[10px] font-bold bg-[#0B0806]/80 text-neutral-300 border border-neutral-700/80 px-2 py-0.5 rounded-md backdrop-blur-md z-20">
            {game.age_rating}
          </span>
        </div>

        {/* Card Content */}
        <div className="p-4 sm:p-5">
          {/* Publisher Badge */}
          {game.publisher && (
            <div className="flex items-center gap-1.5 text-[11px] text-gold/80 font-medium mb-1.5">
              <Building2 className="w-3 h-3 text-gold flex-shrink-0" />
              <span className="truncate">{game.publisher}</span>
            </div>
          )}

          {/* Title */}
          <h3 className="text-lg sm:text-xl font-bold font-kufi text-white group-hover:text-gold transition-colors mb-1 line-clamp-1">
            {game.name}
          </h3>
          
          {/* Tagline */}
          <p className="text-xs text-gold-light/90 font-medium mb-2.5 line-clamp-1">
            {game.tagline}
          </p>

          {/* Description */}
          <p className="text-xs text-neutral-400 line-clamp-2 leading-relaxed mb-4 min-h-[32px]">
            {game.description}
          </p>

          {/* Specs Grid */}
          <div className="grid grid-cols-2 gap-2 text-[11px] text-neutral-300 bg-[#0B0806]/80 p-2.5 rounded-xl border border-gold/10 mb-2">
            <div className="flex items-center gap-1.5">
              <Users className="w-3.5 h-3.5 text-gold flex-shrink-0" />
              <span className="truncate">{game.min_players} - {game.max_players} لاعبين</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Clock className="w-3.5 h-3.5 text-gold flex-shrink-0" />
              <span className="truncate">{game.duration_mins}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Card Action Button */}
      <div className="p-4 pt-0">
        <button className="w-full flex items-center justify-center gap-2 py-2.5 px-3 bg-gold/10 group-hover:bg-gold text-gold group-hover:text-[#0B0806] border border-gold/30 group-hover:border-gold rounded-xl text-xs sm:text-sm font-bold transition-all duration-200">
          <span>عرض اللعبة والقوانين</span>
          <ArrowLeft className="w-3.5 h-3.5 transition-transform group-hover:-translate-x-1" />
        </button>
      </div>

    </div>
  );
};
