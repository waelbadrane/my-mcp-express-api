'use strict';

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/getCardDetails', (req, res) => {
  const card = {
    number: '1234-5678-9012-3456',
    type: 'Visa'
  };
  const timestamp = new Date().toISOString();

  res.json({ card, timestamp });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
