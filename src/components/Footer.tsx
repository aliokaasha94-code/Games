import React from 'react';
import { Coffee, Phone, MapPin, Globe, Heart } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="w-full bg-[#070708] border-t border-gold/20 pt-12 pb-8 px-4 sm:px-6 lg:px-8 mt-16 text-neutral-400">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8 text-center md:text-right">
        
        {/* Brand Col */}
        <div className="flex flex-col items-center md:items-start gap-2.5">
          <div className="flex items-center gap-3">
            <img src="/logo.webp" alt="عماد أفندي" className="h-10 w-auto" />
            <span className="text-xl font-bold font-kufi text-white">
              كافيه ومحمصة <span className="text-gold">عماد أفندي</span>
            </span>
          </div>
          <p className="text-xs text-neutral-400 max-w-sm">
            أكبر وأرقى ملتقى لألعاب الطاولة والكروت والقهوة المختصة في كفر الشيخ.
          </p>
        </div>

        {/* Contact info */}
        <div className="flex flex-wrap items-center justify-center gap-6 text-xs text-neutral-300">
          <div className="flex items-center gap-2">
            <MapPin className="w-4 h-4 text-gold" />
            <span>كفر الشيخ، جمهورية مصر العربية</span>
          </div>
          <a 
            href="tel:+201034031919" 
            className="flex items-center gap-2 hover:text-gold transition-colors"
          >
            <Phone className="w-4 h-4 text-gold" />
            <span dir="ltr">+20 10 3403 1919</span>
          </a>
          <a 
            href="https://emadafandi.com" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="flex items-center gap-2 hover:text-gold transition-colors"
          >
            <Globe className="w-4 h-4 text-gold" />
            <span>emadafandi.com</span>
          </a>
        </div>

      </div>

      <div className="max-w-7xl mx-auto mt-8 pt-6 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between text-xs text-neutral-500 gap-2">
        <p>© {new Date().getFullYear()} كافيه ومحمصة عماد أفندي. جميع الحقوق محفوظة.</p>
        <p className="flex items-center gap-1">
          بُنيت بشغف بأيدي <span className="text-gold font-bold">علي عكاشة</span> وأحدث تقنيات الويب السحابية.
        </p>
      </div>
    </footer>
  );
};
