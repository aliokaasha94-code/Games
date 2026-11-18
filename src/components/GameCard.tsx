import React from 'react';
import { Users, Clock, ShieldAlert, ArrowLeft, ExternalLink } from 'lucide-react';
import { Game } from '../types';

interface GameCardProps {
  game: Game;
  onSelect: (game: Game) => void;
}

export const GameCard: React.FC<GameCardProps> = ({ game, onSelect }) => {
  return (
    <div 
      onClick={() => onSelect(game)}
      className="group relative flex flex-col justify-between bg-[#121214] border border-gold/20 hover:border-gold/60 rounded-2xl overflow-hidden cursor-pointer transition-all duration-300 hover:-translate-y-1 hover:shadow-gold-glow"
    >
      {/* 1px Golden hairline glow overlay on hover */}
      <div className="absolute inset-0 bg-gradient-to-b from-gold/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"></div>

      {/* Card Header & Badges */}
      <div>
        <div className="relative h-44 w-full bg-[#1A1612] flex items-center justify-center overflow-hidden border-b border-gold/15">
          <img 
            src={game.image} 
            alt={game.name}
            loading="lazy"
            className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-[#121214] via-transparent to-transparent"></div>
          
          {/* Category Badge */}
          <span className="absolute top-3 right-3 text-[11px] font-bold bg-[#0B0B0C]/85 text-gold-light border border-gold/30 px-2.5 py-1 rounded-full backdrop-blur-md">
            {game.category_ar}
          </span>

          {/* Age Rating Badge */}
          <span className="absolute top-3 left-3 text-[11px] font-bold bg-neutral-900/85 text-neutral-300 border border-neutral-700 px-2 py-0.5 rounded-md backdrop-blur-md">
            {game.age_rating}
          </span>
        </div>

        {/* Content Body */}
        <div className="p-4 sm:p-5">
          <div className="flex items-start justify-between gap-2 mb-1.5">
            <h3 className="text-lg sm:text-xl font-bold font-kufi text-white group-hover:text-gold transition-colors">
              {game.name}
            </h3>
          </div>
          
          <p className="text-xs text-gold-light/90 font-medium mb-3 line-clamp-1">
            {game.tagline}
          </p>

          <p className="text-xs text-neutral-400 line-clamp-2 leading-relaxed mb-4">
            {game.description}
          </p>

          {/* Metadata Grid */}
          <div className="grid grid-cols-2 gap-2 text-[11px] text-neutral-300 bg-[#0B0B0C]/60 p-2.5 rounded-xl border border-white/5 mb-2">
            <div className="flex items-center gap-1.5">
              <Users className="w-3.5 h-3.5 text-gold" />
              <span>{game.min_players} - {game.max_players} لاعبين</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Clock className="w-3.5 h-3.5 text-gold" />
              <span>{game.duration_mins}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Card Footer / Action */}
      <div className="p-4 pt-0">
        <button className="w-full flex items-center justify-center gap-2 py-2 px-3 bg-gold/10 group-hover:bg-gold text-gold group-hover:text-[#0B0B0C] border border-gold/30 group-hover:border-gold rounded-xl text-xs sm:text-sm font-bold transition-all duration-200">
          <span>شرح اللعبة والقوانين</span>
          <ArrowLeft className="w-3.5 h-3.5 transition-transform group-hover:-translate-x-1" />
        </button>
      </div>

    </div>
  );
};
