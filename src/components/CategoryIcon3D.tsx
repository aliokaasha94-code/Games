import React from 'react';

interface CategoryIcon3DProps {
  categoryId: string;
  className?: string;
  alt?: string;
}

export const CATEGORY_3D_ASSETS: Record<string, string> = {
  all: '/categories-3d/all.png',
  comedy: '/categories-3d/comedy.png',
  bluffing: '/categories-3d/bluffing.png',
  cinema: '/categories-3d/cinema.png',
  football: '/categories-3d/football.png',
  couples: '/categories-3d/couples.png',
  girls: '/categories-3d/girls.png',
  mystery: '/categories-3d/mystery.png',
  strategy: '/categories-3d/strategy.png',
  quick: '/categories-3d/quick.png',
  classic: '/categories-3d/classic.png',
};

export const CategoryIcon3D: React.FC<CategoryIcon3DProps> = ({
  categoryId,
  className = 'w-5 h-5 object-contain',
  alt = '',
}) => {
  const iconSrc = CATEGORY_3D_ASSETS[categoryId] || CATEGORY_3D_ASSETS.all;

  return (
    <img
      src={iconSrc}
      alt={alt}
      loading="eager"
      draggable={false}
      className={`inline-block drop-shadow-[0_2px_4px_rgba(0,0,0,0.5)] select-none pointer-events-none transition-transform duration-200 ${className}`}
    />
  );
};
