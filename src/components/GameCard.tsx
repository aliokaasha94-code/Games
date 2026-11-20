import React from 'react';
import { Users, Clock } from 'lucide-react';
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
      className="group relative flex flex-col bg-[#120E0B] border border-gold/20 hover:border-gold/60 rounded-xl sm:rounded-2xl overflow-hidden cursor-pointer transition-all duration-200 active:scale-[0.97] hover:-translate-y-1 shadow-md hover:shadow-[0_8px_25px_rgba(212,175,55,0.2)] select-none"
    >
      {/* Studio Pedestal Image Display */}
      <div className="relative aspect-square w-full bg-gradient-to-b from-[#1C1713] via-[#14100D] to-[#0D0A08] border-b border-gold/15 flex items-center justify-center p-2 sm:p-4 overflow-hidden">
        {/* Subtle warm golden radial spotlight */}
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(212,175,55,0.18)_0%,transparent_75%)] pointer-events-none"></div>

        {/* Game Box Image */}
        <img 
          src={game.image} 
          alt={game.name}
          loading="lazy"
          className="relative z-10 w-full h-full object-contain filter drop-shadow-[0_8px_16px_rgba(0,0,0,0.8)] group-hover:scale-105 transition-transform duration-300 ease-out"
        />

        {/* Soft ground shadow underneath the game box */}
        <div className="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-3/4 h-2 bg-black/70 rounded-full blur-sm pointer-events-none"></div>

        {/* Floating Category Pill with mini 3D icon */}
        <span className="absolute top-2 right-2 sm:top-2.5 sm:right-2.5 flex items-center gap-1 text-[10px] sm:text-[11px] font-bold bg-[#0B0806]/85 text-gold-light border border-gold/30 px-2 py-0.5 rounded-full backdrop-blur-md shadow-sm z-20">
          <CategoryIcon3D categoryId={game.category} className="w-3 h-3 sm:w-3.5 sm:h-3.5 object-contain" />
          <span className="leading-tight">{game.category_ar}</span>
        </span>
      </div>

      {/* Card Info (Ultra-Clean, Zero Fluff) */}
      <div className="p-2 sm:p-3 flex flex-col flex-1 justify-between gap-1 sm:gap-1.5">
        <h3 className="text-xs sm:text-sm md:text-base font-bold font-kufi text-white group-hover:text-gold transition-colors truncate">
          {game.name}
        </h3>

        {/* Specs row: Players & Duration */}
        <div className="flex items-center justify-between text-[10px] sm:text-xs text-neutral-300 bg-[#0B0806]/70 px-2 py-1 rounded-lg border border-gold/10">
          <span className="flex items-center gap-1">
            <Users className="w-3 h-3 text-gold flex-shrink-0" />
            <span>{game.min_players}-{game.max_players}</span>
          </span>
          <span className="text-neutral-500">•</span>
          <span className="flex items-center gap-1">
            <Clock className="w-3 h-3 text-gold flex-shrink-0" />
            <span className="truncate">{game.duration_mins}</span>
          </span>
        </div>
      </div>
    </div>
  );
};
