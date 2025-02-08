import { Hono } from 'hono'

type Bindings = {
  ASSETS: { get: (key: string) => Promise<Response | null> }
}

interface Song {
  pk: string;
  pptx_url: string;
}

const app = new Hono<{ Bindings: Bindings }>()

app.get('/', async (c) => {
  const html = await c.env.ASSETS.get('index.html')
  if (!html) {
    return c.notFound()
  }
  return new Response(html.body, {
    headers: { 'Content-Type': 'text/html' },
  })
})

app.get('/download/:pk', async (c) => {
  const pk = c.req.param('pk')
  
  // Get songs.json from static assets
  const songsResponse = await c.env.ASSETS.get('songs.json')
  if (!songsResponse) {
    return c.notFound()
  }
  
  // Parse songs data
  const songsText = await songsResponse.text()
  const songs = JSON.parse(songsText) as Song[]
  
  // Find matching song
  const song = songs.find(s => s.pk === pk)
  if (!song) {
    return c.notFound()
  }
  
  // Redirect to pptx_url
  return c.redirect(song.pptx_url)
})

export default app
