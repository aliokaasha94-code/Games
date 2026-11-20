import React from 'react';

interface CategoryIcon3DProps {
  categoryId: string;
  className?: string;
  alt?: string;
}

export const CATEGORY_3D_ASSETS: Record<string, string> = {
  all: '/categories-3d/all.webp',
  comedy: '/categories-3d/comedy.webp',
  bluffing: '/categories-3d/bluffing.webp',
  cinema: '/categories-3d/cinema.webp',
  football: '/categories-3d/football.webp',
  couples: '/categories-3d/couples.webp',
  girls: '/categories-3d/girls.webp',
  mystery: '/categories-3d/mystery.webp',
  strategy: '/categories-3d/strategy.webp',
  quick: '/categories-3d/quick.webp',
  classic: '/categories-3d/classic.webp',
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
      loading="lazy"
      decoding="async"
      width={24}
      height={24}
      draggable={false}
      className={`inline-block select-none pointer-events-none transition-transform duration-200 ${className}`}
    />
  );
};
