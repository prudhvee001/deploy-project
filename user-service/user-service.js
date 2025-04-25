const express = require('express');
const app = express();
const port = 3001;

app.get('/users', (req, res) => {
  res.json({ name: 'John Doe', role: 'Student' });
});

app.listen(port, () => {
  console.log(`User service running on port ${port}`);
});
