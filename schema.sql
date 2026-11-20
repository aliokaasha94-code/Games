-- Cloudflare D1 Database Schema for Emad Afandi Games Hub
-- Database: emad-afandi-games-db

DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id TEXT PRIMARY KEY,
    name_ar TEXT NOT NULL,
    icon TEXT NOT NULL,
    desc TEXT
);

CREATE TABLE games (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    name_en TEXT,
    publisher TEXT NOT NULL,
    publisher_url TEXT,
    category TEXT NOT NULL,
    category_ar TEXT NOT NULL,
    min_players INTEGER NOT NULL,
    max_players INTEGER NOT NULL,
    age_rating TEXT NOT NULL,
    duration_mins TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    tagline TEXT,
    description TEXT NOT NULL,
    how_to_play TEXT NOT NULL,
    rules_summary TEXT,
    image TEXT NOT NULL,
    tags TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(category) REFERENCES categories(id)
);

-- Insert All 11 Official Categories
INSERT INTO categories (id, name_ar, icon, desc) VALUES
('all', 'الكل', '/categories-3d/all.png', 'جميع ألعاب الكافيه المتاحة'),
('comedy', 'ضحك', '/categories-3d/comedy.png', 'ألعاب كسر الملل والتوريط والضحك العالي'),
('bluffing', 'بلوف وتمثيل', '/categories-3d/bluffing.png', 'استنتاج، تمثيل، وكشف الكدابين في القعدة'),
('cinema', 'سينما', '/categories-3d/cinema.png', 'أفلام ومسرحيات وإيفيهات مصرية كلاسيك'),
('football', 'كورة', '/categories-3d/football.png', 'تحديات كروية وأسئلة تاريخية وجدال كروي'),
('couples', 'كابلز', '/categories-3d/couples.png', 'حوارات عميقة وتوافق للكابلز والمخطوبين'),
('girls', 'بنات', '/categories-3d/girls.png', 'جلسات بنات وأسرار وسوالف بدون فلاتر'),
('mystery', 'تحقيقات', '/categories-3d/mystery.png', 'ملفات قضايا وألغاز ذكاء عميقة'),
('strategy', 'ذكاء وتخطيط', '/categories-3d/strategy.png', 'بزنس، تداول، وألعاب استراتيجية وبناء'),
('quick', 'سريعة وتسالي', '/categories-3d/quick.png', 'ألعاب جيب خاطفة ومسابقات سريعة'),
('classic', 'كلاسيك', '/categories-3d/classic.png', 'شطرنج، دومينو أصلي، ومسابقات ثقافية');
