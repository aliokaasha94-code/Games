import React from 'react';
import { Users, Clock, ArrowLeft, Sparkles, Building2 } from 'lucide-react';
import { Game } from '../types';

interface GameCardProps {
  game: Game;
  onSelect: (game: Game) => void;
}

export const GameCard: React.FC<GameCardProps> = ({ game, onSelect }) => {
  return (
    <div 
      onClick={() => onSelect(game)}
      className="group relative flex flex-col justify-between bg-[#13100D] border border-gold/25 hover:border-gold/70 rounded-2xl overflow-hidden cursor-pointer transition-all duration-300 hover:-translate-y-1.5 hover:shadow-gold-glow"
    >
      {/* Golden hairline hover illumination */}
      <div className="absolute inset-0 bg-gradient-to-b from-gold/10 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-10"></div>

      <div>
        {/* E-Commerce Studio Display Pedestal (1:1 Ratio with clean white background) */}
        <div className="relative p-3.5 bg-gradient-to-b from-[#1C1713] to-[#120E0C] border-b border-gold/15">
          <div className="relative aspect-square w-full rounded-xl bg-white p-3 flex items-center justify-center shadow-inner overflow-hidden">
            <img 
              src={game.image} 
              alt={game.name}
              loading="lazy"
              className="w-full h-full object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500"
            />
          </div>

          {/* Floating Category Pill */}
          <span className="absolute top-5 right-5 text-[11px] font-bold bg-[#0B0B0C]/90 text-gold border border-gold/40 px-2.5 py-1 rounded-full backdrop-blur-md shadow-sm">
            {game.category_ar}
          </span>

          {/* Age Rating Pill */}
          <span className="absolute top-5 left-5 text-[10px] font-bold bg-black/80 text-neutral-300 border border-neutral-700 px-2 py-0.5 rounded-md backdrop-blur-md">
            {game.age_rating}
          </span>
        </div>

        {/* Card Content */}
        <div className="p-4 sm:p-5">
          {/* Publisher Badge */}
          {game.publisher && (
            <div className="flex items-center gap-1.5 text-[11px] text-gold/80 font-medium mb-1.5">
              <Building2 className="w-3 h-3 text-gold" />
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
          <div className="grid grid-cols-2 gap-2 text-[11px] text-neutral-300 bg-[#0B0B0C]/80 p-2.5 rounded-xl border border-gold/10 mb-2">
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
        <button className="w-full flex items-center justify-center gap-2 py-2.5 px-3 bg-gold/10 group-hover:bg-gold text-gold group-hover:text-[#0B0B0C] border border-gold/30 group-hover:border-gold rounded-xl text-xs sm:text-sm font-bold transition-all duration-200">
          <span>عرض اللعبة والقوانين</span>
          <ArrowLeft className="w-3.5 h-3.5 transition-transform group-hover:-translate-x-1" />
        </button>
      </div>

    </div>
  );
};
