import React, { useState, useRef, useEffect } from 'react';
import { X, Send, Sparkles, Bot, User, ArrowLeft, RefreshCw, MessageSquare } from 'lucide-react';
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
      text: 'يا هلا بيك في كافيه ومحمصة عماد أفندي! ☕👑\nأنا "كابتن الألعاب الذكي".. قولي عددكم كام ونوع القعدة (صحاب، كابلز، عيلة، بنات، ولا شلة كروية)، وأنا هطلعلك أنسب لعبة وأشرحلك طريقتها فوراً!',
      timestamp: 'الآن',
    },
  ]);
  const [inputText, setInputText] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const quickPrompts = [
    'إحنا 4 شباب وعايزين ضحك ومقالب 😂',
    'شلة شباب وعايزين نضحك مع إياد الموجي 🎬',
    'إحنا كابلز ومقبلين على الجواز وعايزين مودة ورحمة ❤️',
    'قعدة بنات وعايزين أسرار وسوالف 👑',
    'شلة كروية وأهلي وزمالك ⚽',
    'عايزين لعبة بزنس وتجارة وذهب زي مانسا 📈',
    'عايزين لعبة سينما وإيفيهات مصرية 🎬',
    'عايزين لعبة ورق سريعة زي سكرو ⚡',
    'عايزين دور شطرنج أو دومينو قهاوي رايق ♟️',
  ];

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  if (!isOpen) return null;

  const handleSend = (textToSend?: string) => {
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

    // AI Recommendation Logic (Simulated intelligent concierge + function calling)
    setTimeout(() => {
      let replyText = '';
      let targetGameSlug: string | undefined = undefined;

      const lower = text.toLowerCase();

      if (lower.includes('بنات') || lower.includes('بنت') || lower.includes('سوالف')) {
        targetGameSlug = 'girls-walaken';
        replyText = 'على طول ومن غير تفكير.. ملكمش غير لعبة "Girls ولكن"! 👑\nدي اللعبة المخصوصة لقعدات البنات في الكافيه؛ أسرار، ومواقف محرجة، وسوالف بدون فلاتر. فتحتهالك على الشاشة عشان تشوفي تفاصيلها!';
      } else if (lower.includes('رباط') || lower.includes('مودة') || lower.includes('رحمة') || lower.includes('حوار') || lower.includes('زواج')) {
        targetGameSlug = 'mawada-w-rahma';
        replyText = 'جلسة راقية جداً للمتزوجين والمقبلين على الزواج! ☕❤️\nمرشحلك لعبة "مودة ورحمة" من شركة رباط.. بطاقات حوارية عميقة وهادفة لتقوية الروابط والتفاهم مع فنجان قهوة تركي بوش. اتفضل افتح تفاصيلها!';
      } else if (lower.includes('كابلز') || lower.includes('مخطوبين') || lower.includes('حب') || lower.includes('رومانسية') || lower.includes('2')) {
        targetGameSlug = 'couples-walaken';
        replyText = 'أحلى قعدة رايقة مع فنجانين قهوة عماد أفندي! ☕❤️\nمرشحلك لعبة "Couples ولكن" أو "قبل الحوار".. أسئلة ذكية بتقرب المسافات وتفتح مواضيع ممتعة جداً بينكم. اتفضل افتح كارت اللعبة قدامك!';
      } else if (lower.includes('إياد') || lower.includes('الموجي') || lower.includes('استحالة') || lower.includes('إستحالة')) {
        targetGameSlug = 'est7ala';
        replyText = 'التريند الكوميدي الأحدث في عماد أفندي! 😂🔥\nلعبة "إستحالة (مع إياد الموجي)".. مواقف وسيناريوهات مجنونة إستحالة تصدقها، والضحك هيملى الكافيه! فتحتهالك حالاً!';
      } else if (lower.includes('مانسا') || lower.includes('استثمار') || lower.includes('بزنس') || lower.includes('فلوس') || lower.includes('مستثمر')) {
        targetGameSlug = 'mansa';
        replyText = 'عايزين سهرة بزنس وتداول وذهب؟ 📈💰\nمرشحلك لعبة "مانسا (MANSA)" أو "كلمة السر: مستثمر".. صفقات وتجارة ذكية ومضاربات على الطاولة. فتحتهالك فوراً!';
      } else if (lower.includes('شطرنج') || lower.includes('chess')) {
        targetGameSlug = 'starting-chess';
        replyText = 'عشاق التكتيك والهدوء الملكي! ♟️👑\nطقم شطرنج البداية متاح في الكافيه.. خطط وافتح دور تكتيكي رايق مع فنجان إسبريسو كولومبي هادئ. كارت الشطرنج قدامك أهو!';
      } else if (lower.includes('دومينو') || lower.includes('قفلة') || lower.includes('سد')) {
        targetGameSlug = 'original-domino';
        replyText = 'كلاسيكية القهوة المصرية الأصيلة! 🎲☕\nطقم دومينو أصلي عاجي.. العب قفلة أو أمريكاني وسد الطاولة على صحابك مع كباية شاي خمسينة مظبوطة!';
      } else if (lower.includes('ضحك') || lower.includes('مقالب') || lower.includes('ولاعة') || lower.includes('صحاب') || lower.includes('4')) {
        targetGameSlug = 'wala3a';
        replyText = 'عايزين تولعوها ضحك ومقالب؟ يبقى مفيش غير لعبة "ولاعة"! 🔥😂\nاختبار حقيقي لغدر الصحاب وتصويت على أكتر واحد فيكم بيعمل حركات غريبة. كارت اللعبة فتح قدامك أهو!';
      } else if (lower.includes('كورة') || lower.includes('أهلي') || lower.includes('زمالك') || lower.includes('ماتش')) {
        targetGameSlug = 'raz3-el-gomhoor';
        replyText = 'سهرة كروية على أصولها في كفر الشيخ! ⚽🔥\nلعبتكم هي "رزع الجمهور".. كروت جدال كروي وأهلي وزمالك ومقارنات أساطير هتحسم مين بيفهم كورة ومين بيهبد في القعدة!';
      } else if (lower.includes('سينما') || lower.includes('أفلام') || lower.includes('إيفيه')) {
        targetGameSlug = 'kataflam';
        replyText = 'روشتة علاج فورية لمدمني السينما المصرية! 🎬💊\nلعبة "كاتا أفلام (Kataflam)" مصممة علبة دواء حقيقية وبداخلها كروت إيفيهات من أيام الأبيض والأسود لهنيدي والزعيم. فتحتهالك فوراً!';
      } else if (lower.includes('جريمة') || lower.includes('تحقيق') || lower.includes('ذكاء') || lower.includes('غموض')) {
        targetGameSlug = 'waraa-el-gareema';
        replyText = 'لو دماغكم رايقة وعايزين سهرة تفكير عميقة.. ملف قضية "وراء الجريمة: فندق الدم" مستنيكم! 🔍\nتقارير طب شرعي وبصمات وأدلة حقيقية للوصول للقاتل!';
      } else if (lower.includes('سكرو') || lower.includes('سريع') || lower.includes('كروت')) {
        targetGameSlug = 'skrew-pocket';
        replyText = 'لعبة التريند الأولى في مصر: "سكرو (نسخة الجيب)"! ⚡🃏\nلعبة كروت سريعة جداً وحماسية وتعتمد على الذاكرة ورمي الكروت في الوقت الصح. كارت اللعبة أهو!';
      } else {
        targetGameSlug = 'mesh-mertahlak';
        replyText = 'شكل القعدة محتاجة لعبة بلف وشك تكشف مين فيكم بيعرف يمثل! 😂\nمرشحلك لعبة "مش مرتاحلك".. شوف طريقة لعبها واستمتعوا!';
      }

      const botMsg: AIChatMessage = {
        id: (Date.now() + 1).toString(),
        sender: 'bot',
        text: replyText,
        timestamp: new Date().toLocaleTimeString('ar-EG', { hour: '2-digit', minute: '2-digit' }),
        suggestedGameId: targetGameSlug,
      };

      setMessages((prev) => [...prev, botMsg]);
      setIsTyping(false);

      // Function Calling: Automatically select and open the game on the main UI!
      if (targetGameSlug) {
        const found = games.find((g) => g.id === targetGameSlug);
        if (found) {
          setTimeout(() => {
            onSelectGame(found);
          }, 800);
        }
      }
    }, 900);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-end bg-black/60 backdrop-blur-sm animate-fade-in">
      <div className="absolute inset-0" onClick={onClose}></div>

      {/* Drawer */}
      <div className="relative w-full sm:max-w-md h-full bg-[#121214] border-r sm:border-l border-gold/30 shadow-2xl flex flex-col z-10">
        
        {/* Drawer Header */}
        <div className="p-4 bg-[#0B0B0C] border-b border-gold/20 flex items-center justify-between">
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
                مدعوم بنماذج Gemini من كافيه عماد أفندي
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

        {/* Messages Stream */}
        <div className="flex-1 overflow-y-auto p-4 space-y-3.5 text-right">
          {messages.map((msg) => {
            const isBot = msg.sender === 'bot';
            return (
              <div
                key={msg.id}
                className={`flex flex-col ${isBot ? 'items-start' : 'items-end'}`}
              >
                <div
                  className={`max-w-[85%] p-3.5 rounded-2xl text-xs sm:text-sm leading-relaxed whitespace-pre-line ${
                    isBot
                      ? 'bg-[#1A1612] text-neutral-200 border border-gold/20 rounded-tr-none'
                      : 'bg-gold text-[#0B0B0C] font-medium rounded-tl-none shadow-md'
                  }`}
                >
                  {msg.text}

                  {/* Action button if game suggested */}
                  {msg.suggestedGameId && (
                    <div className="mt-2.5 pt-2 border-t border-gold/20">
                      <button
                        onClick={() => {
                          const g = games.find((item) => item.id === msg.suggestedGameId);
                          if (g) onSelectGame(g);
                        }}
                        className="inline-flex items-center gap-1.5 text-xs font-bold text-gold-light hover:text-white transition-colors"
                      >
                        <span>فتح كارت اللعبة والقوانين</span>
                        <ArrowLeft className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  )}
                </div>
                <span className="text-[10px] text-neutral-500 mt-1 px-1">
                  {msg.timestamp}
                </span>
              </div>
            );
          })}

          {isTyping && (
            <div className="flex items-center gap-2 p-3 bg-[#1A1612] border border-gold/15 rounded-2xl w-24">
              <span className="w-2 h-2 bg-gold rounded-full animate-bounce"></span>
              <span className="w-2 h-2 bg-gold rounded-full animate-bounce [animation-delay:0.2s]"></span>
              <span className="w-2 h-2 bg-gold rounded-full animate-bounce [animation-delay:0.4s]"></span>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Quick Prompts */}
        <div className="p-3 bg-[#0B0B0C]/70 border-t border-white/5 overflow-x-auto no-scrollbar">
          <div className="flex items-center gap-1.5 min-w-max">
            {quickPrompts.map((p, idx) => (
              <button
                key={idx}
                onClick={() => handleSend(p)}
                className="text-[11px] bg-[#121214] hover:bg-[#1A1612] text-neutral-300 hover:text-gold border border-gold/20 px-2.5 py-1 rounded-full transition-all whitespace-nowrap active:scale-95"
              >
                {p}
              </button>
            ))}
          </div>
        </div>

        {/* Input Bar */}
        <div className="p-3 bg-[#0B0B0C] border-t border-gold/20 flex items-center gap-2">
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            placeholder="احكيلي عن قعدتكم، عددكم كام، وبتحبوا إيه؟"
            className="flex-1 bg-[#121214] border border-gold/20 focus:border-gold rounded-xl px-3.5 py-2.5 text-xs sm:text-sm text-white placeholder-neutral-500 focus:outline-none transition-colors"
          />
          <button
            onClick={() => handleSend()}
            disabled={!inputText.trim()}
            className="p-2.5 bg-gradient-to-r from-gold to-gold-dark disabled:opacity-40 text-[#0B0B0C] rounded-xl font-bold transition-all active:scale-95 shadow-gold-glow"
          >
            <Send className="w-4 h-4 transform rotate-180" />
          </button>
        </div>

      </div>
    </div>
  );
};
