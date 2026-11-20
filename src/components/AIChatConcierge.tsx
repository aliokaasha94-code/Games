import React, { useState, useRef, useEffect } from 'react';
import { X, Send, Sparkles, Bot, User, ArrowLeft, RefreshCw, MessageSquare, Coffee, ExternalLink } from 'lucide-react';
import { Game, AIChatMessage } from '../types';

interface AIChatConciergeProps {
  isOpen: boolean;
  onClose: () => void;
  games: Game[];
  onSelectGame: (game: Game) => void;
}

export const AIChatConcierge: React.FC<AIChatConciergeProps> = ({
  isOpen,
  onClose,
  games,
  onSelectGame,
}) => {
  const [messages, setMessages] = useState<AIChatMessage[]>([
    {
      id: 'welcome',
      sender: 'bot',
      text: 'يا هلا بيك في كافيه ومحمصة عماد أفندي! ☕👑\nأنا "كابتن الألعاب الذكي".. قولي عددكم كام ونوع القعدة (صحاب، كابلز، عيلة، بنات، ولا شلة كروية)، وأنا هطلعلك أنسب لعبة من الـ 44 لعبة المتاحين وأشرحلك طريقتها فوراً!',
      timestamp: 'الآن',
    },
  ]);
  const [inputText, setInputText] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const quickPrompts = [
    'إحنا 4 شباب وعايزين لعبة ضحك',
    'شلة وعايزين نضحك مع إياد الموجي',
    'إحنا كابلز ومقبلين على الجواز وعايزين لعبة رايقة',
    'قعدة بنات وعايزين أسرار وسوالف',
    'شلة كروية وتحديات كورة',
    'عايزين لعبة ذكاء وتخطيط وبزنس زي مانسا',
    'عايزين دور شطرنج أو دومينو كلاسيك رايق',
  ];

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  if (!isOpen) return null;

  // Local fallback smart matcher
  const matchGameLocally = (text: string): { reply: string; gameId?: string } => {
    const lower = text.toLowerCase();
    if (lower.includes('بنات') || lower.includes('بنت') || lower.includes('سوالف')) {
      return {
        reply: 'على طول ومن غير تفكير.. ملكمش غير لعبة "Girls ولكن"! 👑\nدي اللعبة المخصوصة لقعدات البنات في الكافيه؛ أسرار وسوالف بدون فلاتر!',
        gameId: 'girls-walaken'
      };
    }
    if (lower.includes('رباط') || lower.includes('مودة') || lower.includes('رحمة') || lower.includes('حوار') || lower.includes('زواج')) {
      return {
        reply: 'جلسة راقية جداً للمتزوجين والمقبلين على الزواج! ☕❤️\nمرشحلك لعبة "مودة ورحمة" من شركة رباط.. حوارات عميقة وهادفة لتقوية الروابط مع فنجان قهوة تركي بوش.',
        gameId: 'mawada-w-rahma'
      };
    }
    if (lower.includes('كابلز') || lower.includes('مخطوبين') || lower.includes('حب') || lower.includes('رومانسية') || lower.includes('2')) {
      return {
        reply: 'أحلى قعدة رايقة مع فنجانين قهوة عماد أفندي! ☕❤️\nمرشحلك لعبة "Couples ولكن" أو "قبل الحوار".. أسئلة ذكية بتقرب المسافات وتفتح مواضيع ممتعة جداً بينكم.',
        gameId: 'couples-walaken'
      };
    }
    if (lower.includes('إياد') || lower.includes('الموجي') || lower.includes('استحالة') || lower.includes('إستحالة')) {
      return {
        reply: 'التريند الكوميدي الأحدث في عماد أفندي! 😂🔥\nلعبة "إستحالة (مع إياد الموجي)".. مواقف وسيناريوهات مجنونة والضحك هيملى الكافيه!',
        gameId: 'est7ala'
      };
    }
    if (lower.includes('مانسا') || lower.includes('استثمار') || lower.includes('بزنس') || lower.includes('فلوس') || lower.includes('مستثمر')) {
      return {
        reply: 'عايزين سهرة بزنس وتداول وذهب؟ 📈💰\nمرشحلك لعبة "مانسا (MANSA)" أو "كلمة السر: مستثمر".. صفقات وتجارة ذكية على الطاولة.',
        gameId: 'mansa'
      };
    }
    if (lower.includes('شطرنج') || lower.includes('chess')) {
      return {
        reply: 'عشاق التكتيك والهدوء الملكي! ♟️👑\nطقم شطرنج البداية متاح في الكافيه.. خطط وافتح دور تكتيكي رايق مع فنجان إسبريسو كولومبي هادئ.',
        gameId: 'starting-chess'
      };
    }
    if (lower.includes('دومينو') || lower.includes('قفلة') || lower.includes('سد')) {
      return {
        reply: 'كلاسيكية القهوة المصرية الأصيلة! 🎲☕\nطقم دومينو أصلي عاجي.. العب قفلة وسد الطاولة على صحابك مع كباية شاي خمسينة مظبوطة!',
        gameId: 'original-domino'
      };
    }
    if (lower.includes('كورة') || lower.includes('أهلي') || lower.includes('زمالك') || lower.includes('ماتش')) {
      return {
        reply: 'سهرة كروية على أصولها في كفر الشيخ! ⚽🔥\nلعبتكم هي "رزع الجمهور".. كروت جدال كروي وأهلي وزمالك ومقارنات أساطير!',
        gameId: 'raz3-el-gomhoor'
      };
    }
    if (lower.includes('سينما') || lower.includes('أفلام') || lower.includes('إيفيه')) {
      return {
        reply: 'روشتة علاج فورية لمدمني السينما المصرية! 🎬💊\nلعبة "كاتا أفلام (Kataflam)" مصممة كعلبة دواء حقيقية وبداخلها كروت إيفيهات من الأبيض والأسود للزعيم وهنيدي!',
        gameId: 'kataflam'
      };
    }
    if (lower.includes('سكرو') || lower.includes('skrew') || lower.includes('ورق')) {
      return {
        reply: 'اللعبة الأكثر طلباً وسرعة في قعدات الشباب! ⚡🃏\nلعبة "سكرو (SKREW)".. العب ذكاء واستراتيجية وتخلص من الأرقام العالية بأسرع وقت.',
        gameId: 'skrew-pocket'
      };
    }
    return {
      reply: 'يا هلا بيك! منور عماد أفندي ☕👑\nمرشحلك لعبة "مش مرتاحلك" أو "ولاعة".. أكتر لعبتين بيعملوا ضحك وتحديات في الكافيه! افتح الكارت وشوف القوانين فوراً.',
      gameId: 'mesh-mertahlak'
    };
  };

  const findMatchingGameId = (text: string): string | undefined => {
    for (const g of games) {
      if (text.includes(g.name) || text.toLowerCase().includes(g.name_en.toLowerCase()) || text.includes(g.id)) {
        return g.id;
      }
    }
    return undefined;
  };

  const handleSend = async (textToSend?: string) => {
    const text = (textToSend || inputText).trim();
    if (!text) return;

    const userMsg: AIChatMessage = {
      id: Date.now().toString(),
      sender: 'user',
      text,
      timestamp: new Date().toLocaleTimeString('ar-EG', { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!textToSend) setInputText('');
    setIsTyping(true);

    try {
      // 1. Try real Cloudflare Pages API endpoint with Gemini
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: text }),
      });

      if (res.ok) {
        const data = await res.json();
        const replyText = data.reply || data.text || '';
        const detectedGameId = findMatchingGameId(replyText) || findMatchingGameId(text);

        const botMsg: AIChatMessage = {
          id: (Date.now() + 1).toString(),
          sender: 'bot',
          text: replyText,
          timestamp: new Date().toLocaleTimeString('ar-EG', { hour: '2-digit', minute: '2-digit' }),
          suggestedGameId: detectedGameId,
        };
        setMessages((prev) => [...prev, botMsg]);
        setIsTyping(false);
        return;
      }
    } catch {
      // Network failed or offline - fall through to smart matcher
    }

    // 2. Fallback to local smart matcher
    setTimeout(() => {
      const local = matchGameLocally(text);
      const botMsg: AIChatMessage = {
        id: (Date.now() + 1).toString(),
        sender: 'bot',
        text: local.reply,
        timestamp: new Date().toLocaleTimeString('ar-EG', { hour: '2-digit', minute: '2-digit' }),
        suggestedGameId: local.gameId,
      };
      setMessages((prev) => [...prev, botMsg]);
      setIsTyping(false);
    }, 600);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-end bg-black/60 backdrop-blur-sm animate-fade-in">
      <div className="absolute inset-0" onClick={onClose}></div>

      {/* Drawer */}
      <div className="relative w-full sm:max-w-md h-full bg-[#130F0D] border-r sm:border-l border-gold/30 shadow-2xl flex flex-col z-10">
        
        {/* Drawer Header */}
        <div className="p-4 bg-[#0B0807] border-b border-gold/20 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="relative">
              <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-gold to-gold-dark flex items-center justify-center text-[#0B0B0C] font-bold shadow-gold-glow">
                <Bot className="w-5 h-5" />
              </div>
              <span className="absolute bottom-0 right-0 w-3 h-3 bg-emerald-500 border-2 border-[#0B0B0C] rounded-full"></span>
            </div>
            <div>
              <h3 className="text-sm sm:text-base font-bold font-kufi text-white flex items-center gap-1.5">
                كابتن الألعاب الذكي
                <Sparkles className="w-3.5 h-3.5 text-gold fill-gold" />
              </h3>
              <p className="text-[11px] text-neutral-400">
                مساعد الترشيحات الذكي في عماد أفندي
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-full text-neutral-400 hover:text-white hover:bg-white/10 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Messages Body */}
        <div className="flex-1 p-4 overflow-y-auto space-y-4 text-xs sm:text-sm">
          {messages.map((msg) => {
            const isBot = msg.sender === 'bot';
            const suggestedGame = msg.suggestedGameId
              ? games.find((g) => g.id === msg.suggestedGameId)
              : null;

            return (
              <div
                key={msg.id}
                className={`flex flex-col ${isBot ? 'items-start' : 'items-end'}`}
              >
                <div
                  className={`max-w-[85%] rounded-2xl p-3.5 sm:p-4 leading-relaxed shadow-md ${
                    isBot
                      ? 'bg-[#1C1613] text-neutral-200 border border-gold/20 rounded-tr-none'
                      : 'bg-gradient-to-r from-gold to-gold-dark text-[#0B0B0C] font-semibold rounded-tl-none'
                  }`}
                >
                  <p className="whitespace-pre-line">{msg.text}</p>
                </div>

                {/* Suggested Game Interactive Card */}
                {suggestedGame && (
                  <div
                    onClick={() => {
                      onSelectGame(suggestedGame);
                    }}
                    className="mt-2.5 w-full max-w-[85%] bg-[#1A1411] border border-gold/40 hover:border-gold rounded-xl p-2.5 flex items-center gap-3 cursor-pointer shadow-gold-glow transition-all active:scale-95 group"
                  >
                    <div className="w-12 h-12 rounded-lg bg-gradient-to-b from-[#1C1713] to-[#0D0A08] border border-gold/30 p-1 flex-shrink-0 flex items-center justify-center overflow-hidden">
                      <img
                        src={suggestedGame.image}
                        alt={suggestedGame.name}
                        className="w-full h-full object-contain filter drop-shadow"
                      />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="text-xs font-bold text-white group-hover:text-gold transition-colors truncate">
                        {suggestedGame.name}
                      </div>
                      <div className="text-[11px] text-neutral-400 truncate">
                        {suggestedGame.tagline}
                      </div>
                    </div>
                    <ArrowLeft className="w-4 h-4 text-gold group-hover:-translate-x-1 transition-transform" />
                  </div>
                )}

                <span className="text-[10px] text-neutral-500 mt-1 px-1">
                  {msg.timestamp}
                </span>
              </div>
            );
          })}

          {isTyping && (
            <div className="flex items-center gap-2 text-xs text-neutral-400 bg-[#1C1613] p-3 rounded-2xl w-fit border border-gold/15">
              <Sparkles className="w-3.5 h-3.5 text-gold animate-spin" />
              <span>كابتن الألعاب بيفكرلك في أحسن لعبة...</span>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Quick Suggestion Chips */}
        <div className="px-4 py-2 bg-[#0E0A08] border-t border-gold/15 overflow-x-auto no-scrollbar flex items-center gap-2">
          {quickPrompts.map((prompt) => (
            <button
              key={prompt}
              onClick={() => handleSend(prompt)}
              className="whitespace-nowrap text-[11px] bg-[#1A1411] hover:bg-gold/20 text-neutral-300 hover:text-gold border border-gold/25 px-3 py-1.5 rounded-full transition-all active:scale-95"
            >
              {prompt}
            </button>
          ))}
        </div>

        {/* Input Bar */}
        <div className="p-3 bg-[#0B0807] border-t border-gold/20 flex items-center gap-2">
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            placeholder="اكتب مواصفات قعدتكم هنا..."
            className="flex-1 bg-[#1A1411] border border-gold/25 focus:border-gold rounded-xl px-3.5 py-2.5 text-xs sm:text-sm text-white placeholder-neutral-500 focus:outline-none"
          />
          <button
            onClick={() => handleSend()}
            disabled={!inputText.trim()}
            className="p-2.5 bg-gradient-to-r from-gold to-gold-dark hover:from-gold-light hover:to-gold text-[#0B0B0C] font-bold rounded-xl shadow-gold-glow disabled:opacity-50 transition-all active:scale-95"
          >
            <Send className="w-4 h-4 rotate-180" />
          </button>
        </div>

      </div>
    </div>
  );
};
