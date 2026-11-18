// Cloudflare Pages Function: /api/games
interface Env {
  DB?: any; // Cloudflare D1 Database binding
}

export const onRequestGet = async (context: { env: Env; request: Request }) => {
  const url = new URL(context.request.url);
  const category = url.searchParams.get('category');
  const players = url.searchParams.get('players');

  // If D1 Database is bound in Cloudflare
  if (context.env.DB) {
    try {
      let query = 'SELECT * FROM games WHERE 1=1';
      const params: any[] = [];

      if (category && category !== 'all') {
        query += ' AND category = ?';
        params.push(category);
      }

      if (players) {
        const p = parseInt(players, 10);
        query += ' AND min_players <= ? AND max_players >= ?';
        params.push(p, p);
      }

      const { results } = await context.env.DB.prepare(query).bind(...params).all();
      return new Response(JSON.stringify({ games: results }), {
        headers: {
          'Content-Type': 'application/json',
          'Cache-Control': 'public, max-age=3600, s-maxage=86400',
        },
      });
    } catch (e: any) {
      return new Response(JSON.stringify({ error: e.message }), { status: 500 });
    }
  }

  // Fallback response with CORS & Edge Caching
  return new Response(JSON.stringify({ message: "D1 database ready or using client static bundle" }), {
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
