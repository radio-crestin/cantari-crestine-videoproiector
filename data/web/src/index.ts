import { Hono } from 'hono'

type Bindings = {
  ASSETS: { get: (key: string) => Promise<Response | null> }
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

export default app
