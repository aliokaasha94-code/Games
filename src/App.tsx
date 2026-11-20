import React, { useState, useMemo, useEffect, useRef, Suspense, lazy } from 'react';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { CategoryFilter } from './components/CategoryFilter';
import { GameCard } from './components/GameCard';
import { Footer } from './components/Footer';
import { gamesData, categoriesData } from './data/games';
import { Game } from './types';
import { Sparkles, Frown, RotateCcw } from 'lucide-react';

// Code-split modals so the initial payload is ultra-light
const GameDetailModal = lazy(() =>
  import('./components/GameDetailModal').then((m) => ({ default: m.GameDetailModal }))
);
const AIChatConcierge = lazy(() =>
  import('./components/AIChatConcierge').then((m) => ({ default: m.AIChatConcierge }))
);

const INITIAL_BATCH_SIZE = 12;

export const App: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedPlayerCount, setSelectedPlayerCount] = useState<number | null>(null);
  const [selectedGame, setSelectedGame] = useState<Game | null>(null);
  const [isAIChatOpen, setIsAIChatOpen] = useState(false);
  const [visibleCount, setVisibleCount] = useState(INITIAL_BATCH_SIZE);

  const sentinelRef = useRef<HTMLDivElement>(null);

  // Filter games based on category, search query, and player count
  const filteredGames = useMemo(() => {
    return gamesData.filter((game) => {
      // 1. Category filter
      if (selectedCategory !== 'all' && game.category !== selectedCategory) {
        return false;
      }

      // 2. Player count filter (Smart Range inclusive)
      if (selectedPlayerCount !== null) {
        if (selectedPlayerCount === 8) {
          if (game.max_players < 8) return false;
        } else if (selectedPlayerCount === 2) {
          if (game.min_players > 2 || game.max_players < 2) return false;
        } else if (selectedPlayerCount === 4) {
          if (game.max_players < 3 || game.min_players > 4) return false;
        } else if (selectedPlayerCount === 6) {
          if (game.max_players < 5 || game.min_players > 6) return false;
        }
      }

      // 3. Search query
      if (searchQuery.trim() !== '') {
        const query = searchQuery.trim().toLowerCase();
        const matchesName = game.name.toLowerCase().includes(query);
        const matchesEn = game.name_en.toLowerCase().includes(query);
        const matchesDesc = game.description.toLowerCase().includes(query);
        const matchesTagline = game.tagline.toLowerCase().includes(query);
        const matchesCategory = game.category_ar.toLowerCase().includes(query);
        const matchesTags = game.tags.some((tag) => tag.toLowerCase().includes(query));

        if (!matchesName && !matchesEn && !matchesDesc && !matchesTagline && !matchesCategory && !matchesTags) {
          return false;
        }
      }

      return true;
    });
  }, [searchQuery, selectedCategory, selectedPlayerCount]);

  // Reset pagination batch when filters change
  useEffect(() => {
    setVisibleCount(INITIAL_BATCH_SIZE);
  }, [searchQuery, selectedCategory, selectedPlayerCount]);

  // Progressive slicing: show full list for small search/filters, or batch for browse
  const displayedGames = useMemo(() => {
    if (searchQuery.trim() !== '' || (selectedCategory !== 'all' && filteredGames.length <= INITIAL_BATCH_SIZE)) {
      return filteredGames;
    }
    return filteredGames.slice(0, visibleCount);
  }, [filteredGames, visibleCount, searchQuery, selectedCategory]);

  // Auto-load next batch on scroll using IntersectionObserver
  useEffect(() => {
    if (!sentinelRef.current || displayedGames.length >= filteredGames.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          setVisibleCount((prev) => Math.min(prev + INITIAL_BATCH_SIZE, filteredGames.length));
        }
      },
      { rootMargin: '300px' }
    );

    observer.observe(sentinelRef.current);
    return () => observer.disconnect();
  }, [displayedGames.length, filteredGames.length]);

  const handleResetFilters = () => {
    setSearchQuery('');
    setSelectedCategory('all');
    setSelectedPlayerCount(null);
  };

  return (
    <div className="min-h-screen bg-[#0B0B0C] text-[#F3F4F6] flex flex-col font-arabic">
      
      {/* Navigation Bar */}
      <Navbar 
        onOpenAIChat={() => setIsAIChatOpen(true)} 
        gameCount={gamesData.length} 
      />

      {/* Compact Search & Quick Filters */}
      <Hero
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        selectedPlayerCount={selectedPlayerCount}
        onPlayerCountSelect={setSelectedPlayerCount}
        totalGames={gamesData.length}
      />

      {/* Horizontal 3D Category Chips */}
      <CategoryFilter
        categories={categoriesData}
        selectedCategory={selectedCategory}
        onSelectCategory={setSelectedCategory}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-2.5 sm:px-6 lg:px-8 py-3.5 sm:py-6">
        
        {/* Results Counter & Active Filter Badge */}
        <div className="flex items-center justify-between mb-3 text-xs text-neutral-400 px-1">
          <div className="flex items-center gap-2">
            <span>متاح <strong className="text-gold font-bold">{filteredGames.length}</strong> لعبة</span>
            {selectedPlayerCount && (
              <span className="px-2 py-0.5 bg-gold/15 text-gold-light border border-gold/30 rounded-full text-[10px]">
                {selectedPlayerCount === 8 ? 'شلة ٨+' : `${selectedPlayerCount} لعيبة`}
              </span>
            )}
          </div>

          {(searchQuery || selectedCategory !== 'all' || selectedPlayerCount !== null) && (
            <button
              onClick={handleResetFilters}
              className="flex items-center gap-1 text-[11px] text-gold hover:text-gold-light transition-colors"
            >
              <RotateCcw className="w-3 h-3" />
              <span>إعادة ضبط</span>
            </button>
          )}
        </div>

        {/* 2-Column Mobile-First Games Grid */}
        {displayedGames.length > 0 ? (
          <>
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2.5 sm:gap-4">
              {displayedGames.map((game) => (
                <GameCard
                  key={game.id}
                  game={game}
                  onSelect={setSelectedGame}
                />
              ))}
            </div>

            {/* Scroll Sentinel for Smooth Infinite Progression */}
            {displayedGames.length < filteredGames.length && (
              <div ref={sentinelRef} className="flex justify-center mt-6 mb-4">
                <button
                  onClick={() => setVisibleCount((prev) => Math.min(prev + INITIAL_BATCH_SIZE, filteredGames.length))}
                  className="px-5 py-2 rounded-full bg-[#14100D] hover:bg-[#1A1410] text-gold border border-gold/30 hover:border-gold/60 text-xs font-bold transition-all active:scale-95 shadow-sm"
                >
                  عرض باقي الألعاب ({filteredGames.length - displayedGames.length} لعبة متبقية)
                </button>
              </div>
            )}
          </>
        ) : (
          <div className="py-16 text-center flex flex-col items-center justify-center">
            <Frown className="w-10 h-10 text-gold/40 mb-2.5" />
            <h3 className="text-base font-bold text-white mb-1">
              مفيش لعبة مطابقة لبحثك دلوقتي!
            </h3>
            <p className="text-xs text-neutral-400 max-w-xs mx-auto mb-4">
              جرب تغير كلمة البحث أو امسح الفلاتر عشان تشوف كل الألعاب.
            </p>
            <button
              onClick={handleResetFilters}
              className="py-1.5 px-4 bg-gold text-[#0B0806] font-bold text-xs rounded-xl shadow-gold-glow hover:bg-gold-light transition-all"
            >
              عرض كل الألعاب ({gamesData.length})
            </button>
          </div>
        )}

      </main>

      {/* Floating AI Concierge Button (Mobile friendly) */}
      <div className="fixed bottom-5 left-5 z-40">
        <button
          onClick={() => setIsAIChatOpen(true)}
          className="relative group flex items-center gap-2 bg-gradient-to-r from-gold to-gold-dark text-[#0B0806] p-3 sm:px-4 sm:py-3 rounded-full font-bold text-xs sm:text-sm shadow-[0_4px_20px_rgba(212,175,55,0.4)] hover:scale-105 active:scale-95 transition-all duration-300"
          title="تحدث مع كابتن الألعاب الذكي"
        >
          <div className="absolute -inset-1 bg-gradient-to-r from-gold-light to-gold rounded-full blur-md opacity-70 group-hover:opacity-100 transition duration-300"></div>
          <Sparkles className="relative w-4 h-4 sm:w-5 sm:h-5 fill-current animate-spin [animation-duration:6s]" />
          <span className="relative hidden sm:inline">كابتن الألعاب الذكي</span>
        </button>
      </div>

      {/* Lazy-loaded Game Details Modal */}
      {selectedGame && (
        <Suspense fallback={null}>
          <GameDetailModal
            game={selectedGame}
            onClose={() => setSelectedGame(null)}
          />
        </Suspense>
      )}

      {/* Lazy-loaded AI Concierge Drawer */}
      {isAIChatOpen && (
        <Suspense fallback={null}>
          <AIChatConcierge
            isOpen={isAIChatOpen}
            onClose={() => setIsAIChatOpen(false)}
            games={gamesData}
            onSelectGame={(game) => {
              setSelectedGame(game);
            }}
          />
        </Suspense>
      )}

      {/* Footer */}
      <Footer />

    </div>
  );
};

export default App;
