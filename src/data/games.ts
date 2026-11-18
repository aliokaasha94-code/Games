import gamesJson from '../../data/games.json';
import { Game, Category } from '../types';

export const gamesData: Game[] = gamesJson.games as Game[];
export const categoriesData: Category[] = gamesJson.categories as Category[];
export const cafeInfo = {
  name: gamesJson.cafe_name,
  nameEn: gamesJson.cafe_name_en,
  location: gamesJson.location,
  phone: gamesJson.phone,
  officialWebsite: gamesJson.official_website,
};
