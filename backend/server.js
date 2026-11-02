const express = require('express');
const app = express();
const port = Number(process.env.PORT || 3000);
app.get('/healthz', (_req, res) => res.json({status:'ok',service:'backend'}));
app.get('/api/status', (_req, res) => res.json({message:'online',service:'express-backend',timestamp:new Date().toISOString()}));
app.listen(port, '0.0.0.0', () => console.log(`Express backend listening on ${port}`));
