const express = require('express');
const crypto = require("crypto");
const puppeteer = require('puppeteer');
const cookieParser = require('cookie-parser');
const app = express();
const PORT = 3000;
const delay = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
const FLAG = process.env.FLAG ?? "MJSEC{dummy}";
const cookies = [
  { name: 'flag', value: FLAG, domain: '127.0.0.1' },
];
const saved = new Map();

app.use(express.json());
app.use(cookieParser());

app.get("/", (req, res) => {
  res.sendFile(__dirname + '/views/index.html');
});

app.get("/music", (req, res) => {
  res.sendFile(__dirname + '/views/music.html');
});

app.post("/save", (req, res) => {
  const id = crypto.randomBytes(20).toString('hex');
  saved.set(id, req.body.age);
  res.send(`saved! Remember your id: ${id}`);
});

app.get("/saved", (req, res) => {
  res.sendFile(__dirname + '/views/saved.html');
});

app.post("/saved", (req, res) => {
  const age = saved.get(req.body.id);
  res.send(age ? age : 'false');
});

app.get("/report", (req, res) => {
  res.sendFile(__dirname + '/views/report.html');
});

app.post("/report", (req, res) => {
  (async () => {
    try {
      const browser = await puppeteer.launch({
        executablePath: '/usr/bin/google-chrome',
        args: ["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
      });
      const page = await browser.newPage();
      await page.setCookie(...cookies);

      // 페이지 방문
      await page.goto(req.body.url, { timeout: 60000 });  // 타임아웃을 60초로 설정
      await delay(500);

      await browser.close();
      res.send('Reported successfully!');
    } catch (error) {
      console.error("Error during Puppeteer operation:", error);
      res.status(500).send('An error occurred while processing your report.');
    }
  })();
});

// 서버가 3000 포트에서 실행되도록 설정
app.listen(PORT, () => {
  console.log('Running at ' + PORT);
});
