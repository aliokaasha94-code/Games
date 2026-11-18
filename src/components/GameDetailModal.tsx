import React, { useEffect } from 'react';
import { X, Users, Clock, ShieldCheck, Share2, ExternalLink, Sparkles, BookOpen, Trophy } from 'lucide-react';
import { Game } from '../types';

interface GameDetailModalProps {
  game: Game | null;
  onClose: () => void;
}

export const GameDetailModal: React.FC<GameDetailModalProps> = ({ game, onClose }) => {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (game) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => {
      document.body.style.overflow = 'auto';
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [game, onClose]);

  if (!game) return null;

  const handleShare = () => {
    if (navigator.share) {
      navigator.share({
        title: `لعبة ${game.name} في كافيه عماد أفندي`,
        text: `${game.tagline} - تعالى نلعبها سوا في عماد أفندي!`,
        url: window.location.href,
      }).catch(() => {});
    } else {
      navigator.clipboard.writeText(window.location.href);
      alert('تم نسخ رابط اللعبة بنجاح!');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/85 backdrop-blur-md animate-fade-in">
      
      {/* Click outside backdrop */}
      <div className="absolute inset-0" onClick={onClose}></div>

      {/* Modal Container */}
      <div className="relative w-full sm:max-w-2xl max-h-[90vh] sm:max-h-[85vh] bg-[#121214] border-t sm:border border-gold/40 rounded-t-3xl sm:rounded-3xl shadow-2xl overflow-hidden flex flex-col z-10 animate-slide-up">
        
        {/* Top Header / Close Bar */}
        <div className="relative h-48 sm:h-56 w-full bg-[#1A1612] flex items-center justify-center overflow-hidden border-b border-gold/20 flex-shrink-0">
          <img 
            src={game.image} 
            alt={game.name}
            className="w-full h-full object-cover object-center"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-[#121214] via-[#121214]/60 to-transparent"></div>

          {/* Close Button */}
          <button
            onClick={onClose}
            className="absolute top-4 left-4 p-2 rounded-full bg-[#0B0B0C]/80 text-neutral-300 hover:text-white border border-white/10 hover:border-gold transition-colors backdrop-blur-md"
          >
            <X className="w-5 h-5" />
          </button>

          {/* Share Button */}
          <button
            onClick={handleShare}
            className="absolute top-4 right-4 p-2 rounded-full bg-[#0B0B0C]/80 text-gold-light hover:text-white border border-gold/30 hover:border-gold transition-colors backdrop-blur-md"
            title="مشاركة اللعبة"
          >
            <Share2 className="w-5 h-5" />
          </button>

          {/* Header Title inside banner */}
          <div className="absolute bottom-4 right-5 left-5 text-right">
            <span className="inline-block text-xs font-bold text-gold-light bg-gold/15 border border-gold/30 px-3 py-0.5 rounded-full mb-1">
              {game.category_ar} • {game.publisher}
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold font-kufi text-white">
              {game.name}
            </h2>
            <p className="text-xs sm:text-sm text-gold/90 font-medium">
              {game.tagline}
            </p>
          </div>
        </div>

        {/* Scrollable Content Body */}
        <div className="p-5 sm:p-6 overflow-y-auto space-y-5 text-right flex-1">
          
          {/* Key Specs Matrix */}
          <div className="grid grid-cols-3 gap-2.5 bg-[#0B0B0C] p-3.5 rounded-2xl border border-gold/15 text-center">
            <div className="flex flex-col items-center justify-center">
              <span className="text-xs text-neutral-400 mb-0.5 flex items-center gap-1">
                <Users className="w-3.5 h-3.5 text-gold" />
                اللاعبين
              </span>
              <span className="text-sm font-bold text-white font-kufi">
                {game.min_players} - {game.max_players} أفراد
              </span>
            </div>

            <div className="flex flex-col items-center justify-center border-x border-white/10">
              <span className="text-xs text-neutral-400 mb-0.5 flex items-center gap-1">
                <Clock className="w-3.5 h-3.5 text-gold" />
                المدة
              </span>
              <span className="text-sm font-bold text-white font-kufi">
                {game.duration_mins}
              </span>
            </div>

            <div className="flex flex-col items-center justify-center">
              <span className="text-xs text-neutral-400 mb-0.5 flex items-center gap-1">
                <ShieldCheck className="w-3.5 h-3.5 text-gold" />
                السن والصعوبة
              </span>
              <span className="text-sm font-bold text-white font-kufi">
                {game.age_rating} • {game.difficulty}
              </span>
            </div>
          </div>

          {/* Description */}
          <div>
            <h4 className="text-xs font-bold text-neutral-400 uppercase tracking-wider mb-1.5">
              عن اللعبة
            </h4>
            <p className="text-sm text-neutral-200 leading-relaxed bg-[#1A1612]/50 p-3.5 rounded-xl border border-gold/10">
              {game.description}
            </p>
          </div>

          {/* How to Play Section */}
          <div>
            <h4 className="text-sm font-bold text-gold flex items-center gap-2 mb-2 font-kufi">
              <BookOpen className="w-4 h-4" />
              طريقة اللعب خطوة بخطوة
            </h4>
            <div className="bg-[#0B0B0C] p-4 rounded-2xl border border-gold/20 text-xs sm:text-sm text-neutral-200 leading-loose whitespace-pre-line">
              {game.how_to_play}
            </div>
          </div>

          {/* Rules and Victory Summary */}
          <div>
            <h4 className="text-sm font-bold text-amber-400 flex items-center gap-2 mb-2 font-kufi">
              <Trophy className="w-4 h-4" />
              قوانين الفوز والعقوبات
            </h4>
            <div className="bg-amber-950/20 border border-amber-500/30 p-3.5 rounded-xl text-xs sm:text-sm text-amber-200/90 leading-relaxed">
              {game.rules_summary}
            </div>
          </div>

          {/* Tags */}
          <div className="flex flex-wrap gap-1.5 pt-1">
            {game.tags.map((tag) => (
              <span key={tag} className="text-[11px] bg-[#1A1612] text-neutral-300 border border-white/5 px-2.5 py-1 rounded-lg">
                #{tag}
              </span>
            ))}
          </div>

        </div>

        {/* Footer Action Bar */}
        <div className="p-4 bg-[#0B0B0C] border-t border-gold/20 flex items-center justify-between gap-3 flex-shrink-0">
          <a
            href={game.publisher_url}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 text-xs text-neutral-400 hover:text-gold transition-colors"
          >
            <span>موقع الشركة الأصلية</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>

          <button
            onClick={onClose}
            className="flex-1 max-w-[200px] py-2.5 px-4 bg-gradient-to-r from-gold to-gold-dark hover:from-gold-light hover:to-gold text-[#0B0B0C] font-bold text-sm rounded-xl shadow-gold-glow transition-all active:scale-95"
          >
            فهمت، جاهزين نلعب!
          </button>
        </div>

      </div>
    </div>
  );
};
