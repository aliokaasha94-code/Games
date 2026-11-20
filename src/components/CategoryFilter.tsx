import React from 'react';
import { Category } from '../types';
import { CategoryIcon3D } from './CategoryIcon3D';

interface CategoryFilterProps {
  categories: Category[];
  selectedCategory: string;
  onSelectCategory: (catId: string) => void;
}

export const CategoryFilter: React.FC<CategoryFilterProps> = ({
  categories,
  selectedCategory,
  onSelectCategory,
}) => {
  return (
    <div className="w-full py-3.5 overflow-x-auto no-scrollbar border-b border-gold/15 bg-[#0D0A08]/60 backdrop-blur-md sticky top-20 z-30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center gap-2.5 sm:gap-3 min-w-max">
        {categories.map((cat) => {
          const isActive = selectedCategory === cat.id;
          return (
            <button
              key={cat.id}
              onClick={() => onSelectCategory(cat.id)}
              className={`group relative flex items-center gap-2.5 px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-xl text-xs sm:text-sm font-medium transition-all duration-300 active:scale-95 border ${
                isActive
                  ? 'bg-gradient-to-r from-gold via-gold-light to-gold-dark text-[#0B0806] font-bold border-gold shadow-[0_4px_20px_rgba(212,175,55,0.35)] scale-[1.02]'
                  : 'bg-[#14100D]/90 text-neutral-300 border-gold/20 hover:border-gold/50 hover:bg-[#1C1612] hover:text-white shadow-[0_2px_8px_rgba(0,0,0,0.4)]'
              }`}
            >
              <CategoryIcon3D
                categoryId={cat.id}
                className={`w-5 h-5 sm:w-6 sm:h-6 object-contain filter drop-shadow-[0_2px_6px_rgba(0,0,0,0.6)] transition-transform duration-300 ${
                  isActive ? 'scale-110 rotate-[-2deg]' : 'group-hover:scale-110 group-hover:-translate-y-0.5'
                }`}
                alt={cat.name_ar}
              />
              <span className="tracking-wide whitespace-nowrap">{cat.name_ar}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
