import React from 'react';
import { Category } from '../types';

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
    <div className="w-full py-4 overflow-x-auto no-scrollbar border-b border-gold/10">
      <div className="max-w-7xl mx-auto px-4 flex items-center gap-2 sm:gap-3 min-w-max">
        {categories.map((cat) => {
          const isActive = selectedCategory === cat.id;
          return (
            <button
              key={cat.id}
              onClick={() => onSelectCategory(cat.id)}
              className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-medium transition-all active:scale-95 duration-200 border ${
                isActive
                  ? 'bg-gradient-to-r from-gold to-gold-dark text-[#0B0B0C] font-bold border-gold shadow-gold-glow'
                  : 'bg-[#121214] text-neutral-300 border-gold/20 hover:border-gold/50 hover:bg-[#1A1612]'
              }`}
            >
              <span className="text-base">{cat.icon}</span>
              <span>{cat.name_ar}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
