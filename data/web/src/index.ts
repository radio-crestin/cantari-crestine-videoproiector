import { Hono } from 'hono'

const app = new Hono<{ Bindings: CloudflareBindings }>()

app.get('/', (c) => {
  return c.text('Hello Hono!')
})

export default appimport express from 'express';

// Serve static files from the static directory
app.use(express.static(path.join(__dirname, '../static')));

// Serve index.html as the default route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../static/index.html'));
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
