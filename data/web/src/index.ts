import { Hono } from 'hono'

const app = new Hono()

app.get('/', (c) => {
  return c.html(c.env.ASSETS.get('public/index.html'))
})

export default app
