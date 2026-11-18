export interface Game {
  id: string;
  name: string;
  name_en: string;
  publisher: string;
  publisher_url: string;
  category: string;
  category_ar: string;
  min_players: number;
  max_players: number;
  age_rating: string;
  duration_mins: string;
  difficulty: string;
  tagline: string;
  description: string;
  how_to_play: string;
  rules_summary: string;
  image: string;
  tags: string[];
  coffee_pairing?: string;
  pro_tip?: string;
}

export interface Category {
  id: string;
  name_ar: string;
  icon: string;
  desc: string;
}

export interface FilterState {
  category: string;
  searchQuery: string;
  playerCount: number | null;
  ageFilter: string | null;
}

export interface AIChatMessage {
  id: string;
  sender: 'user' | 'bot';
  text: string;
  timestamp: string;
  suggestedGameId?: string;
}
