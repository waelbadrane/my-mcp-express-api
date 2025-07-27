# my-mcp-express-api

This is a basic Node.js Express API repository.

## Getting Started

### Prerequisites
- Node.js installed on your machine
- npm (Node package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/waelbadrane/my-mcp-express-api.git
   cd my-mcp-express-api
   ```
2. Install dependencies:
   ```bash
   npm install express
   ```
3. Create an `index.js` file with your Express server code or use the existing one if present.
4. Start the server:
   ```bash
   node index.js
   ```
5. The API will run on http://localhost:3000 by default.

## Example Express Server (index.js)
```js
const express = require('express');
const app = express();
const port = 3000;
app.get('/', (req, res) => {
  res.send('Hello World!');
});
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```
