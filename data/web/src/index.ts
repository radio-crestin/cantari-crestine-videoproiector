import { Hono } from 'hono'
import { serveStatic } from 'hono/cloudflare-pages'

const app = new Hono()

// Serve static files
app.use('/*', serveStatic({ root: './public' }))

// Serve index.html as the default route
app.get('/', (c) => {
  return c.html(c.env.ASSETS.get('index.html'))
})

export default app
