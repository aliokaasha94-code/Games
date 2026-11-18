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
('all', 'الكل', '🎲', 'جميع ألعاب الكافيه المتاحة'),
('comedy', 'ضحك ومقالب', '😂', 'ألعاب كسر الملل والتوريط والضحك العالي'),
('bluffing', 'شك وبلف', '🕵️', 'استنتاج، تمثيل، وكشف الكدابين في القعدة'),
('cinema', 'سينما وإيفيهات', '🎬', 'أفلام ومسرحيات وإيفيهات مصرية كلاسيك'),
('football', 'كورة ورزع', '⚽', 'أهلي وزمالك ورزع كروي تاريخي'),
('couples', 'كابلز وصراحة', '❤️', 'حوارات عميقة وتوافق للكابلز والمخطوبين'),
('girls', 'بنات فقط', '👑', 'جلسات بنات وأسرار وسوالف بدون فلاتر'),
('mystery', 'تحقيقات وجرائم', '🔍', 'ملفات قضايا وألغاز ذكاء عميقة'),
('strategy', 'استثمار وتخطيط', '📈', 'بزنس، تداول، وألعاب استراتيجية وبناء'),
('quick', 'كروت وتسالي سريعة', '⚡', 'ألعاب جيب خاطفة من 15-20 دقيقة'),
('classic', 'كلاسيك ومسابقات', '🏆', 'شطرنج، دومينو أصلي، وموسوعات ثقافية');

-- Indices for ultra-fast edge queries
CREATE INDEX idx_games_category ON games(category);
CREATE INDEX idx_games_players ON games(min_players, max_players);
