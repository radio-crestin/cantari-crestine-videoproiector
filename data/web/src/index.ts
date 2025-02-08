import { Hono } from 'hono'
import { serveStatic } from '@hono/node-server/serve-static'

const app = new Hono()

// Serve static files from the static directory
app.use('/*', serveStatic({ root: './static' }))

// Serve index.html as the default route
app.get('/', (c) => {
  return c.html('./static/index.html')
})

export default app
