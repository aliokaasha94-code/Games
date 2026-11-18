import React, { useState, useMemo } from 'react';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { CategoryFilter } from './components/CategoryFilter';
import { GameCard } from './components/GameCard';
import { GameDetailModal } from './components/GameDetailModal';
import { AIChatConcierge } from './components/AIChatConcierge';
import { Footer } from './components/Footer';
import { gamesData, categoriesData, cafeInfo } from './data/games';
import { Game } from './types';
import { Sparkles, Frown, RotateCcw } from 'lucide-react';

export const App: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedPlayerCount, setSelectedPlayerCount] = useState<number | null>(null);
  const [selectedGame, setSelectedGame] = useState<Game | null>(null);
  const [isAIChatOpen, setIsAIChatOpen] = useState(false);

  // Filter games based on category, search query, and player count
  const filteredGames = useMemo(() => {
    return gamesData.filter((game) => {
      // 1. Category filter
      if (selectedCategory !== 'all' && game.category !== selectedCategory) {
        return false;
      }

      // 2. Player count filter
      if (selectedPlayerCount !== null) {
        if (selectedPlayerCount === 8) {
          // Large party 8+
          if (game.max_players < 8) return false;
        } else {
          if (game.min_players > selectedPlayerCount || game.max_players < selectedPlayerCount) {
            return false;
          }
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

      {/* Hero Header with Search and Quick Filters */}
      <Hero
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        selectedPlayerCount={selectedPlayerCount}
        onPlayerCountSelect={setSelectedPlayerCount}
        totalGames={gamesData.length}
      />

      {/* Horizontal Category Tabs */}
      <CategoryFilter
        categories={categoriesData}
        selectedCategory={selectedCategory}
        onSelectCategory={setSelectedCategory}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        {/* Results Info & Active Filters */}
        <div className="flex items-center justify-between mb-6 text-xs text-neutral-400">
          <div>
            <span>عرض <strong className="text-gold font-bold">{filteredGames.length}</strong> من أصل {gamesData.length} لعبة</span>
            {selectedPlayerCount && (
              <span className="mr-2 px-2 py-0.5 bg-gold/15 text-gold-light border border-gold/30 rounded-full">
                {selectedPlayerCount === 8 ? '8+ أفراد' : `${selectedPlayerCount} لاعبين`}
              </span>
            )}
          </div>

          {(searchQuery || selectedCategory !== 'all' || selectedPlayerCount !== null) && (
            <button
              onClick={handleResetFilters}
              className="flex items-center gap-1 text-gold hover:text-gold-light transition-colors"
            >
              <RotateCcw className="w-3 h-3" />
              <span>إعادة ضبط الفلاتر</span>
            </button>
          )}
        </div>

        {/* Games Grid */}
        {filteredGames.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
            {filteredGames.map((game) => (
              <GameCard
                key={game.id}
                game={game}
                onSelect={setSelectedGame}
              />
            ))}
          </div>
        ) : (
          <div className="py-20 text-center flex flex-col items-center justify-center">
            <Frown className="w-12 h-12 text-gold/40 mb-3" />
            <h3 className="text-lg font-bold text-white mb-1">
              مفيش لعبة مطابقة لبحثك في الكافيه دلوقتي!
            </h3>
            <p className="text-xs text-neutral-400 max-w-md mx-auto mb-5">
              جرب تغير كلمة البحث أو تمسح الفلاتر عشان تشوف كل الألعاب المتاحة عندنا.
            </p>
            <button
              onClick={handleResetFilters}
              className="py-2 px-4 bg-gold text-[#0B0B0C] font-bold text-xs rounded-xl shadow-gold-glow hover:bg-gold-light transition-all"
            >
              عرض جميع الألعاب ({gamesData.length})
            </button>
          </div>
        )}

      </main>

      {/* Floating AI Concierge Button (Mobile friendly) */}
      <div className="fixed bottom-6 left-6 z-40">
        <button
          onClick={() => setIsAIChatOpen(true)}
          className="relative group flex items-center gap-2 bg-gradient-to-r from-gold to-gold-dark text-[#0B0B0C] p-3.5 sm:px-5 sm:py-3.5 rounded-full font-bold text-xs sm:text-sm shadow-gold-glow-lg hover:scale-105 active:scale-95 transition-all duration-300"
          title="تحدث مع كابتن الألعاب الذكي"
        >
          <div className="absolute -inset-1 bg-gradient-to-r from-gold-light to-gold rounded-full blur-md opacity-70 group-hover:opacity-100 transition duration-300"></div>
          <Sparkles className="relative w-5 h-5 fill-current animate-spin [animation-duration:6s]" />
          <span className="relative hidden sm:inline">كابتن الألعاب الذكي</span>
        </button>
      </div>

      {/* Game Details Bottom Sheet / Modal */}
      <GameDetailModal
        game={selectedGame}
        onClose={() => setSelectedGame(null)}
      />

      {/* AI Concierge Drawer */}
      <AIChatConcierge
        isOpen={isAIChatOpen}
        onClose={() => setIsAIChatOpen(false)}
        games={gamesData}
        onSelectGame={(game) => {
          setSelectedGame(game);
        }}
      />

      {/* Footer */}
      <Footer />

    </div>
  );
};

export default App;
