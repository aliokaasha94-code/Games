import React, { useState, useEffect } from 'react';
import { X, Users, Clock, ShieldCheck, Share2, Sparkles, BookOpen, Coffee, MessageCircle, Check } from 'lucide-react';
import { Game } from '../types';
import { CategoryIcon3D } from './CategoryIcon3D';

interface GameDetailModalProps {
  game: Game | null;
  onClose: () => void;
}

export const GameDetailModal: React.FC<GameDetailModalProps> = ({ game, onClose }) => {
  const [activeTab, setActiveTab] = useState<'rules' | 'coffee' | 'tips'>('rules');
  const [tableNumber, setTableNumber] = useState('');
  const [isCopied, setIsCopied] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (game) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleKeyDown);
      setActiveTab('rules');
      setTableNumber('');
      setIsCopied(false);
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
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000);
    }
  };

  const handleOrderToTable = () => {
    const table = tableNumber.trim() || 'داخل الكافيه';
    const text = encodeURIComponent(
      `مساء الخير يا عماد أفندي! ☕🎲\nحابين نطلب لعبة "${game.name}" على طاولة رقم (${table}).\nشكراً ليكم!`
    );
    window.open(`https://wa.me/201034031919?text=${text}`, '_blank');
  };

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/80 backdrop-blur-sm animate-fade-in">
      
      {/* Click outside backdrop */}
      <div className="absolute inset-0" onClick={onClose}></div>

      {/* Modal Container */}
      <div className="relative w-full sm:max-w-xl max-h-[90vh] sm:max-h-[85vh] bg-[#14100D] border-t sm:border border-gold/30 rounded-t-2xl sm:rounded-2xl shadow-2xl overflow-hidden flex flex-col z-10 animate-slide-up">
        
        {/* Mobile Drag Indicator */}
        <div className="w-10 h-1 bg-neutral-700/80 rounded-full mx-auto mt-2 sm:hidden flex-shrink-0"></div>

        {/* Top Product Showcase Bar */}
        <div className="relative p-3.5 sm:p-5 bg-gradient-to-b from-[#1E1813] to-[#120E0C] border-b border-gold/15 flex items-center gap-3.5 sm:gap-5 flex-shrink-0">
          
          {/* Studio Pedestal Image */}
          <div className="relative w-20 h-20 sm:w-28 sm:h-28 rounded-xl bg-gradient-to-b from-[#1C1713] via-[#14100D] to-[#0D0A08] p-2 flex items-center justify-center shadow-lg border border-gold/25 flex-shrink-0 overflow-hidden">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(212,175,55,0.2)_0%,transparent_75%)] pointer-events-none"></div>
            <img 
              src={game.image} 
              alt={game.name}
              className="relative z-10 w-full h-full object-contain filter drop-shadow-[0_4px_12px_rgba(0,0,0,0.85)]"
            />
          </div>

          {/* Header Info */}
          <div className="flex-1 min-w-0 pr-1">
            <div className="flex items-center gap-1.5 mb-1">
              <span className="flex items-center gap-1 text-[11px] font-bold bg-gold/15 text-gold border border-gold/30 px-2 py-0.5 rounded-full">
                <CategoryIcon3D categoryId={game.category} className="w-3.5 h-3.5 object-contain" />
                {game.category_ar}
              </span>
              <span className="text-[10px] font-bold bg-[#0B0806]/80 text-neutral-300 border border-neutral-700 px-1.5 py-0.5 rounded">
                {game.age_rating}
              </span>
            </div>

            <h2 className="text-base sm:text-xl font-bold font-kufi text-white truncate">
              {game.name}
            </h2>
            <p className="text-xs text-gold-light/90 font-medium truncate mb-1.5">
              {game.tagline}
            </p>

            {/* Quick Specs */}
            <div className="inline-flex items-center gap-2.5 text-[11px] text-neutral-300 bg-[#0B0806]/80 px-2.5 py-0.5 rounded-lg border border-gold/15">
              <span className="flex items-center gap-1">
                <Users className="w-3 h-3 text-gold" />
                {game.min_players} - {game.max_players} لعيبة
              </span>
              <span className="text-neutral-500">•</span>
              <span className="flex items-center gap-1">
                <Clock className="w-3 h-3 text-gold" />
                {game.duration_mins}
              </span>
            </div>
          </div>

          {/* Close & Share Buttons */}
          <div className="flex items-center gap-1.5 self-start">
            <button
              onClick={handleShare}
              className="p-1.5 rounded-full bg-black/60 text-neutral-300 hover:text-gold hover:bg-black/90 border border-gold/20 transition-all"
              title="مشاركة اللعبة"
            >
              {isCopied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Share2 className="w-3.5 h-3.5" />}
            </button>
            <button
              onClick={onClose}
              className="p-1.5 rounded-full bg-black/60 text-neutral-300 hover:text-white hover:bg-black/90 border border-gold/20 transition-all"
              title="إغلاق"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>

        {/* Navigation Tabs */}
        <div className="flex border-b border-gold/15 bg-[#0E0A08] px-3 pt-1.5 gap-1.5 flex-shrink-0">
          <button
            onClick={() => setActiveTab('rules')}
            className={`flex items-center gap-1.5 py-2 px-3 text-xs font-bold border-b-2 transition-all ${
              activeTab === 'rules'
                ? 'border-gold text-gold'
                : 'border-transparent text-neutral-400 hover:text-neutral-200'
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>طريقة اللعب</span>
          </button>

          <button
            onClick={() => setActiveTab('coffee')}
            className={`flex items-center gap-1.5 py-2 px-3 text-xs font-bold border-b-2 transition-all ${
              activeTab === 'coffee'
                ? 'border-gold text-gold'
                : 'border-transparent text-neutral-400 hover:text-neutral-200'
            }`}
          >
            <Coffee className="w-3.5 h-3.5" />
            <span>مشروبك ☕</span>
          </button>

          <button
            onClick={() => setActiveTab('tips')}
            className={`flex items-center gap-1.5 py-2 px-3 text-xs font-bold border-b-2 transition-all ${
              activeTab === 'tips'
                ? 'border-gold text-gold'
                : 'border-transparent text-neutral-400 hover:text-neutral-200'
            }`}
          >
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>سر الفوز 🔥</span>
          </button>
        </div>

        {/* Scrollable Tab Content */}
        <div className="p-3.5 sm:p-5 overflow-y-auto flex-1 space-y-3 text-neutral-200 text-xs sm:text-sm leading-relaxed">
          
          {activeTab === 'rules' && (
            <div className="space-y-3 animate-fade-in">
              <p className="text-neutral-300 leading-relaxed bg-[#0B0806]/60 p-3 rounded-xl border border-white/5">
                {game.description}
              </p>

              {game.how_to_play && (
                <div>
                  <h4 className="text-gold font-bold font-kufi text-xs sm:text-sm mb-1.5 flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5" />
                    خطوات اللعب:
                  </h4>
                  <div className="bg-[#0B0806]/60 p-3 rounded-xl border border-white/5 space-y-1.5">
                    {Array.isArray(game.how_to_play) ? (
                      <ol className="list-decimal list-inside space-y-1.5 text-neutral-300">
                        {game.how_to_play.map((step, idx) => (
                          <li key={idx} className="leading-relaxed">{step}</li>
                        ))}
                      </ol>
                    ) : (
                      <p className="text-neutral-300 whitespace-pre-line leading-relaxed">{game.how_to_play}</p>
                    )}
                  </div>
                </div>
              )}
            </div>
          )}

          {activeTab === 'coffee' && (
            <div className="bg-gradient-to-br from-[#1C1612] to-[#120E0C] p-4 rounded-xl border border-gold/25 text-center space-y-2 animate-fade-in">
              <div className="w-10 h-10 rounded-full bg-gold/15 text-gold flex items-center justify-center mx-auto shadow-gold-glow">
                <Coffee className="w-5 h-5" />
              </div>
              <h4 className="text-sm sm:text-base font-bold font-kufi text-white">
                توليفة القهوة المثالية للعبة
              </h4>
              <p className="text-gold-light font-bold text-xs sm:text-sm">
                {game.coffee_pairing || 'فلات وايت بالبن الإثيوبي المختص أو سبانش لاتيه بارد'}
              </p>
              <p className="text-[11px] text-neutral-400 max-w-sm mx-auto">
                مشروب يضبط تركيزك أو يزود روقان القعدة مع أصحابك في عماد أفندي.
              </p>
            </div>
          )}

          {activeTab === 'tips' && (
            <div className="bg-[#0B0806]/70 p-4 rounded-xl border border-gold/20 space-y-2 animate-fade-in">
              <h4 className="text-gold font-bold font-kufi text-xs sm:text-sm flex items-center gap-1.5">
                <ShieldCheck className="w-4 h-4 text-gold" />
                نصيحة الفوز:
              </h4>
              <p className="text-neutral-300 leading-relaxed text-xs sm:text-sm">
                {game.pro_tip || 'ركز في لغة جسد اللي قدامك، العب بهدوء ومتكشفش أوراقك بدري، واستغل اللحظة الصح للمفاجأة!'}
              </p>
            </div>
          )}

        </div>

        {/* Table Request Action Footer */}
        <div className="p-3 sm:p-4 bg-[#0B0806] border-t border-gold/20 flex items-center gap-2 sm:gap-3 flex-shrink-0">
          <div className="w-28 sm:w-36 flex items-center bg-[#1A1410] border border-gold/25 rounded-xl px-2.5 py-2 text-xs">
            <span className="text-neutral-400 whitespace-nowrap ml-1.5 text-[11px]">طاولة:</span>
            <input 
              type="text" 
              placeholder="مثال: 5" 
              value={tableNumber}
              onChange={(e) => setTableNumber(e.target.value)}
              className="w-full bg-transparent text-white focus:outline-none font-bold text-xs"
            />
          </div>

          <button
            onClick={handleOrderToTable}
            className="flex-1 flex items-center justify-center gap-1.5 py-2 sm:py-2.5 px-3 bg-gradient-to-r from-gold to-gold-dark hover:from-gold-light hover:to-gold text-[#0B0806] font-bold rounded-xl text-xs sm:text-sm shadow-gold-glow transition-all active:scale-95 duration-200"
          >
            <MessageCircle className="w-4 h-4 fill-current flex-shrink-0" />
            <span className="truncate">اطلب اللعبة على طاولتك</span>
          </button>
        </div>

      </div>
    </div>
  );
};
