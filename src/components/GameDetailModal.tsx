import React, { useState, useEffect } from 'react';
import { X, Users, Clock, ShieldCheck, Share2, Sparkles, BookOpen, Coffee, MessageCircle, Building2, Check, Award } from 'lucide-react';
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
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/85 backdrop-blur-md animate-fade-in">
      
      {/* Click outside backdrop */}
      <div className="absolute inset-0" onClick={onClose}></div>

      {/* Modal Container */}
      <div className="relative w-full sm:max-w-2xl max-h-[92vh] sm:max-h-[88vh] bg-[#14100D] border-t sm:border border-gold/40 rounded-t-3xl sm:rounded-3xl shadow-2xl overflow-hidden flex flex-col z-10 animate-slide-up">
        
        {/* Top Product Showcase Bar */}
        <div className="relative p-5 bg-gradient-to-b from-[#1E1813] to-[#120E0C] border-b border-gold/20 flex flex-col sm:flex-row items-center gap-5 flex-shrink-0">
          
          {/* 1:1 Clean Studio Product Pedestal (Replaces white box with dark luxury pedestal) */}
          <div className="relative w-32 h-32 sm:w-36 sm:h-36 rounded-2xl bg-gradient-to-b from-[#1C1713] via-[#14100D] to-[#0D0A08] p-3 flex items-center justify-center shadow-2xl border border-gold/30 flex-shrink-0 overflow-hidden">
            {/* Subtle radial spotlight */}
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(212,175,55,0.2)_0%,transparent_75%)] pointer-events-none"></div>
            <img 
              src={game.image} 
              alt={game.name}
              className="relative z-10 w-full h-full object-contain filter drop-shadow-[0_8px_16px_rgba(0,0,0,0.85)]"
            />
            {/* Ground shadow */}
            <div className="absolute bottom-1 left-1/2 -translate-x-1/2 w-3/4 h-2.5 bg-black/70 rounded-full blur-sm pointer-events-none"></div>
          </div>

          {/* Header Info */}
          <div className="flex-1 text-center sm:text-right">
            <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2 mb-1.5">
              <span className="flex items-center gap-1.5 text-xs font-bold bg-gold/15 text-gold border border-gold/30 px-2.5 py-0.5 rounded-full">
                <CategoryIcon3D categoryId={game.category} className="w-4 h-4 object-contain" />
                {game.category_ar}
              </span>
              <span className="text-xs font-bold bg-[#0B0806]/80 text-neutral-300 border border-neutral-700 px-2 py-0.5 rounded-md">
                {game.age_rating}
              </span>
              {game.publisher && (
                <span className="flex items-center gap-1 text-[11px] text-neutral-400">
                  <Building2 className="w-3 h-3 text-gold" />
                  {game.publisher}
                </span>
              )}
            </div>

            <h2 className="text-xl sm:text-2xl font-bold font-kufi text-white mb-1">
              {game.name}
            </h2>
            <p className="text-xs sm:text-sm text-gold-light/90 font-medium mb-2">
              {game.tagline}
            </p>

            {/* Quick Specs */}
            <div className="inline-flex items-center gap-4 text-xs text-neutral-300 bg-[#0B0806]/80 px-3 py-1.5 rounded-xl border border-gold/15">
              <span className="flex items-center gap-1">
                <Users className="w-3.5 h-3.5 text-gold" />
                {game.min_players} - {game.max_players} لاعبين
              </span>
              <span className="flex items-center gap-1">
                <Clock className="w-3.5 h-3.5 text-gold" />
                {game.duration_mins}
              </span>
            </div>
          </div>

          {/* Close & Share Buttons */}
          <div className="absolute top-4 left-4 flex items-center gap-2">
            <button
              onClick={handleShare}
              className="p-2 rounded-full bg-black/60 text-neutral-300 hover:text-gold hover:bg-black/90 border border-gold/20 transition-all"
              title="مشاركة اللعبة"
            >
              {isCopied ? <Check className="w-4 h-4 text-emerald-400" /> : <Share2 className="w-4 h-4" />}
            </button>
            <button
              onClick={onClose}
              className="p-2 rounded-full bg-black/60 text-neutral-300 hover:text-white hover:bg-black/90 border border-gold/20 transition-all"
              title="إغلاق"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Navigation Tabs */}
        <div className="flex border-b border-gold/20 bg-[#0E0A08] px-4 pt-2 gap-2 flex-shrink-0">
          <button
            onClick={() => setActiveTab('rules')}
            className={`flex items-center gap-2 py-2.5 px-4 text-xs sm:text-sm font-bold border-b-2 transition-all ${
              activeTab === 'rules'
                ? 'border-gold text-gold'
                : 'border-transparent text-neutral-400 hover:text-neutral-200'
            }`}
          >
            <BookOpen className="w-4 h-4" />
            <span>القوانين وطريقة اللعب</span>
          </button>

          <button
            onClick={() => setActiveTab('coffee')}
            className={`flex items-center gap-2 py-2.5 px-4 text-xs sm:text-sm font-bold border-b-2 transition-all ${
              activeTab === 'coffee'
                ? 'border-gold text-gold'
                : 'border-transparent text-neutral-400 hover:text-neutral-200'
            }`}
          >
            <Coffee className="w-4 h-4" />
            <span>المشروب المقترح</span>
          </button>

          <button
            onClick={() => setActiveTab('tips')}
            className={`flex items-center gap-2 py-2.5 px-4 text-xs sm:text-sm font-bold border-b-2 transition-all ${
              activeTab === 'tips'
                ? 'border-gold text-gold'
                : 'border-transparent text-neutral-400 hover:text-neutral-200'
            }`}
          >
            <Award className="w-4 h-4" />
            <span>نصائح الفوز</span>
          </button>
        </div>

        {/* Scrollable Tab Content */}
        <div className="p-5 sm:p-6 overflow-y-auto flex-1 space-y-4 text-neutral-200 text-sm leading-relaxed">
          
          {activeTab === 'rules' && (
            <div className="space-y-4 animate-fade-in">
              <div>
                <h4 className="text-gold font-bold font-kufi text-base mb-1.5 flex items-center gap-2">
                  <Sparkles className="w-4 h-4" />
                  نبذة عن اللعبة
                </h4>
                <p className="text-neutral-300 leading-relaxed bg-[#0B0806]/60 p-3.5 rounded-xl border border-white/5">
                  {game.description}
                </p>
              </div>

              {game.how_to_play && (
                <div>
                  <h4 className="text-gold font-bold font-kufi text-base mb-2">
                    🎯 كيف تبدأ اللعب؟
                  </h4>
                  <div className="bg-[#0B0806]/60 p-4 rounded-xl border border-white/5 space-y-2">
                    {Array.isArray(game.how_to_play) ? (
                      <ol className="list-decimal list-inside space-y-2">
                        {game.how_to_play.map((step, idx) => (
                          <li key={idx} className="text-neutral-300">{step}</li>
                        ))}
                      </ol>
                    ) : (
                      <p className="text-neutral-300 whitespace-pre-line">{game.how_to_play}</p>
                    )}
                  </div>
                </div>
              )}
            </div>
          )}

          {activeTab === 'coffee' && (
            <div className="bg-gradient-to-br from-[#1C1612] to-[#120E0C] p-5 rounded-2xl border border-gold/30 text-center space-y-3 animate-fade-in">
              <div className="w-12 h-12 rounded-full bg-gold/15 text-gold flex items-center justify-center mx-auto shadow-gold-glow">
                <Coffee className="w-6 h-6" />
              </div>
              <h4 className="text-lg font-bold font-kufi text-white">
                توليفة القهوة المثالية لهذه اللعبة ☕
              </h4>
              <p className="text-gold-light font-medium text-sm">
                {game.coffee_pairing || 'فلات وايت بالبن الإثيوبي المختص أو سبانش لاتيه بارد'}
              </p>
              <p className="text-xs text-neutral-400 max-w-md mx-auto">
                في عماد أفندي، بنختار لكل لعبة مشروب يضبط تركيزك أو يزود روقانك مع أصحابك على الطاولة.
              </p>
            </div>
          )}

          {activeTab === 'tips' && (
            <div className="bg-[#0B0806]/70 p-5 rounded-2xl border border-gold/20 space-y-3 animate-fade-in">
              <h4 className="text-gold font-bold font-kufi text-base flex items-center gap-2">
                <ShieldCheck className="w-5 h-5 text-gold" />
                سر الفوز وإشعال الجلسة 🔥
              </h4>
              <p className="text-neutral-300 leading-relaxed">
                {game.pro_tip || 'ركز في لغة جسد اللي قدامك، العب بهدوء ومتكشفش أوراقك بدري، واستغل اللحظة الصح للمفاجأة!'}
              </p>
            </div>
          )}

        </div>

        {/* Table Request Action Footer (Cafe Operations Flywheel) */}
        <div className="p-4 bg-[#0B0806] border-t border-gold/25 flex flex-col sm:flex-row items-center gap-3 flex-shrink-0">
          <div className="w-full sm:w-44 flex items-center bg-[#1A1410] border border-gold/30 rounded-xl px-3 py-2 text-xs">
            <span className="text-neutral-400 whitespace-nowrap ml-2">طاولة رقم:</span>
            <input 
              type="text" 
              placeholder="مثال: 5" 
              value={tableNumber}
              onChange={(e) => setTableNumber(e.target.value)}
              className="w-full bg-transparent text-white focus:outline-none font-bold"
            />
          </div>

          <button
            onClick={handleOrderToTable}
            className="w-full sm:flex-1 flex items-center justify-center gap-2 py-3 px-4 bg-gradient-to-r from-gold to-gold-dark hover:from-gold-light hover:to-gold text-[#0B0806] font-extrabold rounded-xl text-sm shadow-gold-glow transition-all active:scale-95 duration-200"
          >
            <MessageCircle className="w-4 h-4 fill-current" />
            <span>طلب استعارة اللعبة على طاولتي فوراً</span>
          </button>
        </div>

      </div>
    </div>
  );
};
