Content is user-generated and unverified.


24
Learn about artifacts
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fraction Pizza Shop</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Nunito:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root{
    --crust:#c97a3d;
    --crust-dark:#8a4f24;
    --sauce:#ef4b3a;
    --sauce-dark:#c62f20;
    --cheese:#ffcf5c;
    --basil:#2fae66;
    --basil-dark:#1f8a4e;
    --teal:#22b8c8;
    --teal-dark:#1591a0;
    --purple:#9b5de5;
    --purple-dark:#7638c2;
    --pink:#ff5d9e;
    --pink-dark:#e0367c;
    --board:#fdf1de;
    --ink:#3a2a1a;
    --paper:#fffaf0;
    --shadow: 0 6px 0 rgba(0,0,0,0.12);
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    font-family:'Nunito', sans-serif;
    background:
      radial-gradient(circle at 12% 8%, #ffe08a 0%, transparent 40%),
      radial-gradient(circle at 92% 12%, #ff9fc7 0%, transparent 35%),
      radial-gradient(circle at 85% 90%, #8fe6d9 0%, transparent 40%),
      radial-gradient(circle at 8% 90%, #c9b6ff 0%, transparent 40%),
      var(--board);
    color:var(--ink);
    min-height:100vh;
    padding:20px;
    overflow-x:hidden;
  }
  .wrap{max-width:960px; margin:0 auto; position:relative;}

  header{
    display:flex; align-items:flex-start; justify-content:space-between;
    gap:16px; flex-wrap:wrap;
    margin-bottom:18px;
  }
  .title-block h1{
    font-family:'Baloo 2', sans-serif;
    font-size:clamp(24px,4vw,38px);
    margin:0;
    color:var(--sauce-dark);
    letter-spacing:0.5px;
    text-shadow: 2px 2px 0 #fff2d6;
  }
  .rainbow-underline{
    height:6px; width:150px; border-radius:6px; margin-top:4px;
    background: linear-gradient(90deg, var(--sauce), var(--cheese), var(--basil), var(--teal), var(--purple), var(--pink));
    background-size: 300% 100%;
    animation: slideRainbow 6s linear infinite;
  }
  @keyframes slideRainbow{
    0%{background-position:0% 0;}
    100%{background-position:300% 0;}
  }
  .subtitle{font-size:13px; color:#7a5c3a; font-weight:700; margin-top:8px;}

  .brand-badge{
    display:flex; align-items:center; gap:8px;
    background:linear-gradient(135deg, var(--purple), var(--pink));
    color:#fff;
    font-family:'Baloo 2'; font-weight:800; font-size:15px;
    padding:9px 16px 9px 12px;
    border-radius:999px;
    box-shadow: 0 5px 0 var(--purple-dark);
    white-space:nowrap;
  }
  .brand-badge .badge-icon{
    width:26px; height:26px; border-radius:50%;
    background:#fff; color:var(--purple);
    display:flex; align-items:center; justify-content:center;
    font-size:15px;
  }

  .stagebar{
    display:flex; gap:6px; align-items:center; flex-wrap:wrap;
    margin-bottom:16px;
  }
  .stage-dot{
    display:flex; align-items:center; gap:5px;
    font-family:'Baloo 2';
    font-weight:700;
    font-size:12px;
    padding:5px 10px 5px 6px;
    border-radius:999px;
    background:#fff;
    border:2px solid #e7d3a8;
    color:#b79766;
    transition:all .25s;
  }
  .stage-dot .num{
    width:18px; height:18px; border-radius:50%;
    background:#e7d3a8; color:#fff;
    display:flex; align-items:center; justify-content:center;
    font-size:11px;
  }
  .stage-dot.active{
    background:var(--teal); color:#fff; border-color:var(--teal-dark);
    box-shadow:var(--shadow);
    animation: pulseDot 1.4s ease-in-out infinite;
  }
  @keyframes pulseDot{
    0%,100%{ transform:scale(1); }
    50%{ transform:scale(1.06); }
  }
  .stage-dot.active .num{background:#fff; color:var(--teal-dark);}
  .stage-dot.done{background:var(--basil); color:#fff; border-color:var(--basil-dark);}
  .stage-dot.done .num{background:#fff; color:var(--basil-dark);}

  .card{
    background:var(--paper);
    border-radius:26px;
    border:3px solid #eddcb3;
    box-shadow: 0 10px 0 #e3cf9c, 0 14px 24px rgba(120,80,20,0.15);
    padding:26px;
    position:relative;
    overflow:hidden;
  }
  .card::before{
    content:"";
    position:absolute; top:-40px; right:-40px;
    width:150px; height:150px;
    background:radial-gradient(circle, #ffe6b0 0%, transparent 70%);
  }
  .confetti-layer{
    position:fixed; inset:0; pointer-events:none; z-index:999;
  }
  .confetti-piece{
    position:absolute; font-size:22px; top:-30px;
    animation: fall linear forwards;
  }
  @keyframes fall{
    to{ transform: translateY(105vh) rotate(360deg); opacity:0.9; }
  }

  .speech{
    display:flex; gap:14px; align-items:flex-start;
    margin-bottom:18px;
  }
  .avatar{
    width:56px; height:56px; border-radius:50%;
    background:var(--cheese);
    display:flex; align-items:center; justify-content:center;
    font-size:28px; flex-shrink:0;
    border:3px solid var(--crust-dark);
    box-shadow:var(--shadow);
    transition: transform .2s;
  }
  .avatar.bounce{ animation: bounce .6s ease; }
  .avatar.shake{ animation: shake .5s ease; }
  @keyframes bounce{
    0%,100%{ transform:translateY(0) rotate(0); }
    30%{ transform:translateY(-14px) rotate(-8deg); }
    60%{ transform:translateY(0) rotate(6deg); }
  }
  @keyframes shake{
    0%,100%{ transform:translateX(0); }
    25%{ transform:translateX(-8px); }
    75%{ transform:translateX(8px); }
  }
  .bubble{
    background:#fff;
    border:3px solid var(--ink);
    border-radius:16px 16px 16px 2px;
    padding:12px 16px;
    font-family:'Baloo 2';
    font-size:clamp(16px,2.6vw,20px);
    font-weight:600;
    max-width:620px;
  }
  .bubble .frac{
    color:var(--sauce-dark);
    font-weight:800;
  }

  .challenge-tag{
    display:inline-block;
    font-family:'Baloo 2'; font-weight:800; font-size:12px;
    color:#fff; background:var(--pink);
    padding:4px 12px; border-radius:999px;
    margin-bottom:12px;
    box-shadow: 0 3px 0 var(--pink-dark);
  }

  .main-row{
    display:flex; gap:30px; flex-wrap:wrap;
    align-items:center;
    justify-content:center;
  }

  .pizza-block{
    display:flex; flex-direction:column; align-items:center; gap:10px;
  }
  .pizza-label{
    font-family:'Baloo 2'; font-weight:700; font-size:14px;
    color:#8a6a3f;
    background:#fff2d6;
    padding:3px 12px;
    border-radius:999px;
  }
  svg.pizza{ width:220px; height:220px; cursor:pointer; touch-action:manipulation; }
  svg.pizza.static{ cursor:default; }
  svg.pizza.small{ width:140px; height:140px; }
  .slice{ transition: fill .12s, opacity .12s; }
  .slice.topped{ fill: var(--sauce); }
  .slice.untopped{ fill: var(--cheese); }
  .slice.eaten{ fill:#e6dcc3; opacity:0.55; }
  .slice:hover.interactive{ opacity:0.85; }
  .crust-ring{ fill:none; stroke:var(--crust-dark); stroke-width:6; }
  .slice-line{ stroke:var(--crust-dark); stroke-width:2.5; }
  .pizza-frame{
    border-radius:18px; padding:8px; transition: all .15s;
    border:3px solid transparent;
  }
  .pizza-frame.pickable{ cursor:pointer; }
  .pizza-frame.pickable:hover{ border-color:var(--teal); transform:translateY(-2px); }
  .pizza-frame.picked{ border-color:var(--purple); background:#f3e9ff; }
  .pizza-frame.order-tag{ position:relative; }
  .order-badge{
    position:absolute; top:-6px; left:-6px;
    width:26px; height:26px; border-radius:50%;
    background:var(--purple); color:#fff;
    font-family:'Baloo 2'; font-weight:800; font-size:14px;
    display:flex; align-items:center; justify-content:center;
    box-shadow: 0 3px 0 var(--purple-dark);
  }

  .controls{
    display:flex; flex-direction:column; gap:14px;
    min-width:260px;
  }
  .control-group label{
    font-family:'Baloo 2'; font-weight:700; font-size:14px;
    color:#7a5c3a; display:block; margin-bottom:6px;
  }
  .chip-row{ display:flex; flex-wrap:wrap; gap:8px; }
  .chip{
    font-family:'Baloo 2'; font-weight:700; font-size:15px;
    background:#fff; border:2.5px solid var(--crust);
    color:var(--crust-dark);
    padding:7px 14px; border-radius:12px;
    cursor:pointer; transition: all .15s;
  }
  .chip:hover{ background:#fff0d8; transform:translateY(-1px); }
  .chip.selected{ background:var(--crust); color:#fff; box-shadow:var(--shadow); }

  .status-line{
    font-family:'Baloo 2'; font-weight:700; font-size:16px;
    color:var(--ink);
    min-height:22px;
  }

  button.primary{
    font-family:'Baloo 2'; font-weight:800; font-size:17px;
    background:var(--basil); color:#fff;
    border:none; border-radius:14px;
    padding:12px 20px;
    cursor:pointer;
    box-shadow: 0 5px 0 var(--basil-dark);
    transition: transform .08s;
  }
  button.primary:active{ transform:translateY(4px); box-shadow:none; }
  button.primary:disabled{ background:#c9c1ac; box-shadow:0 5px 0 #a9a190; cursor:not-allowed; }
  button.primary.teal{ background:var(--teal); box-shadow:0 5px 0 var(--teal-dark); }
  button.primary.purple{ background:var(--purple); box-shadow:0 5px 0 var(--purple-dark); }
  button.primary.pink{ background:var(--pink); box-shadow:0 5px 0 var(--pink-dark); }

  button.ghost{
    font-family:'Baloo 2'; font-weight:700; font-size:14px;
    background:transparent; color:#8a6a3f;
    border:2px solid #d9c193; border-radius:12px;
    padding:8px 14px; cursor:pointer;
  }
  button.ghost:hover{ background:#fff2d6; }

  .feedback{
    font-family:'Baloo 2'; font-weight:700; font-size:16px;
    padding:10px 14px; border-radius:12px;
    margin-top:6px;
    display:none;
  }
  .feedback.show{ display:block; }
  .feedback.good{ background:#e3f4e0; color:var(--basil-dark); border:2px solid #b7dfae; }
  .feedback.bad{ background:#fde3df; color:var(--sauce-dark); border:2px solid #f5b8ac; }

  .footer-row{
    display:flex; justify-content:space-between; align-items:center;
    margin-top:20px; flex-wrap:wrap; gap:10px;
  }

  .score-pill{
    font-family:'Baloo 2'; font-weight:800; font-size:14px;
    background:var(--cheese); color:var(--crust-dark);
    border:2px solid var(--crust-dark);
    padding:6px 14px; border-radius:999px;
  }
  .streak-pill{
    font-family:'Baloo 2'; font-weight:800; font-size:14px;
    background:var(--teal); color:#fff;
    border:2px solid var(--teal-dark);
    padding:6px 14px; border-radius:999px;
  }
  .pills{ display:flex; gap:10px; flex-wrap:wrap; }

  .compare-pizzas{ display:flex; gap:36px; flex-wrap:wrap; justify-content:center; }
  .vs-badge{
    font-family:'Baloo 2'; font-weight:800; font-size:20px;
    color:var(--sauce-dark); align-self:center;
  }
  .choice-row{ display:flex; gap:10px; flex-wrap:wrap; justify-content:center; margin-top:10px;}
  .choice-btn{
    font-family:'Baloo 2'; font-weight:700; font-size:15px;
    background:#fff; border:2.5px solid var(--crust);
    color:var(--crust-dark); padding:10px 16px; border-radius:12px;
    cursor:pointer; transition: all .12s;
  }
  .choice-btn:hover{ background:#fff0d8; transform:translateY(-1px); }
  .choice-btn.picked{ background:var(--crust); color:#fff; }
  .choice-btn.tf-true{ border-color:var(--basil); color:var(--basil-dark); }
  .choice-btn.tf-true:hover{ background:#e3f4e0; }
  .choice-btn.tf-false{ border-color:var(--sauce); color:var(--sauce-dark); }
  .choice-btn.tf-false:hover{ background:#fde3df; }
  .choice-btn:disabled{ opacity:0.4; cursor:default; }

  .three-pizza-row{ display:flex; gap:24px; flex-wrap:wrap; justify-content:center; }

  /* Equivalent fractions equation row */
  .equation-row{
    display:flex; align-items:center; gap:10px; flex-wrap:wrap;
    justify-content:center; margin:18px 0;
    font-family:'Baloo 2'; font-weight:800; font-size:clamp(20px,4vw,28px);
  }
  .eq-frac{ color:var(--sauce-dark); background:#fff2d6; padding:5px 14px; border-radius:10px; }
  .eq-sign{ color:#8a6a3f; }
  .fold-row{ display:flex; gap:26px; justify-content:center; flex-wrap:wrap; margin:10px 0; }

  /* Number line */
  .token-tray{ display:flex; gap:12px; justify-content:center; margin-bottom:34px; flex-wrap:wrap; }
  .token-chip{
    font-family:'Baloo 2'; font-weight:800; font-size:16px;
    background:var(--purple); color:#fff;
    padding:9px 18px; border-radius:12px; cursor:pointer;
    box-shadow:0 4px 0 var(--purple-dark);
    transition: all .12s;
  }
  .token-chip:hover{ transform:translateY(-1px); }
  .token-chip.selected{ outline:3px solid var(--teal); outline-offset:2px; }
  .token-chip.used{ opacity:0.3; pointer-events:none; box-shadow:none; }
  .numberline-wrap{ position:relative; width:100%; max-width:540px; height:90px; margin:10px auto 20px; }
  .numberline-track{ position:absolute; top:40px; left:10px; right:10px; height:5px; background:var(--crust-dark); border-radius:4px; }
  .nl-tick{
    position:absolute; top:30px; width:5px; height:26px; border-radius:3px;
    background:#e2cf9f; transform:translateX(-2.5px); cursor:pointer;
  }
  .nl-tick:hover{ background:#c9ac6e; }
  .nl-tick.filled{ background:var(--basil); cursor:default; }
  .nl-endlabel{
    position:absolute; top:64px; transform:translateX(-50%);
    font-family:'Baloo 2'; font-weight:800; font-size:13px; color:#8a6a3f;
  }
  .nl-placed-label{
    position:absolute; top:-2px; transform:translate(-50%,-100%);
    font-family:'Baloo 2'; font-weight:800; font-size:13px;
    background:var(--basil); color:#fff; padding:4px 9px; border-radius:8px;
    box-shadow:0 3px 0 var(--basil-dark);
  }

  /* Butterfly */
  .butterfly-row{
    display:flex; align-items:center; justify-content:center; gap:40px;
    margin:14px 0 20px; flex-wrap:wrap;
  }
  .bfrac{
    display:flex; flex-direction:column; align-items:center; line-height:1.15;
    font-family:'Baloo 2'; font-weight:800; font-size:clamp(28px,6vw,40px);
    color:var(--ink);
  }
  .bfrac .bar{ width:50px; height:5px; background:var(--ink); margin:3px 0; border-radius:3px; }
  .bfly-emoji{ font-size:42px; animation: flutter 2.2s ease-in-out infinite; }
  @keyframes flutter{
    0%,100%{ transform: translateY(0) rotate(-4deg); }
    50%{ transform: translateY(-8px) rotate(4deg); }
  }
  .bstep{
    background:#fff2d6; border-radius:14px; padding:14px 18px;
    margin-top:10px; text-align:center;
  }
  .bstep .bstep-label{ font-family:'Baloo 2'; font-weight:800; font-size:15px; color:#8a6a3f; margin-bottom:8px; }

  @media (max-width:520px){
    svg.pizza{ width:180px; height:180px; }
    svg.pizza.small{ width:110px; height:110px; }
    .main-row{ gap:18px; }
    header{ flex-direction:column; }
    .butterfly-row{ gap:20px; }
  }
</style>
</head>
<body>
<div class="confetti-layer" id="confettiLayer"></div>
<div class="wrap">
  <header>
    <div class="title-block">
      <h1>🍕 Fraction Pizza Shop</h1>
      <div class="rainbow-underline"></div>
      <div class="subtitle">Day 2: Fraction Fun Factory — visualize, compare, and find equivalent fractions!</div>
    </div>
    <div class="brand-badge"><span class="badge-icon">📘</span>MyMasteryLab</div>
  </header>

  <div class="stagebar" id="stagebar"></div>

  <div class="card" id="cardArea"></div>

  <div class="footer-row">
    <div class="pills">
      <div class="score-pill" id="scorePill">⭐ Score: 0</div>
      <div class="streak-pill" id="streakPill">🔥 Streak: 0</div>
    </div>
    <button class="ghost" id="resetBtn">Start over</button>
  </div>
</div>

<script>
// ---------- fraction helpers ----------
function gcd(a,b){ return b===0 ? a : gcd(b, a%b); }
function lcm(a,b){ return (a*b)/gcd(a,b); }
function simplify(n,d){ const g = gcd(n,d); return {n:n/g, d:d/g}; }

// ---------- state ----------
const STAGES = ["Icebreaker","Order","Equivalent","Number Line","Butterfly","Challenges"];
let stageIndex = 0;
let score = 0;
let streak = 0;
let challengeRound = 1;
const TOTAL_CHALLENGE_ROUNDS = 4;

const orderPool = [
  {n:1,d:2},{n:1,d:3},{n:2,d:3},{n:1,d:4},{n:3,d:4},
  {n:1,d:6},{n:5,d:6},{n:1,d:8},{n:3,d:8},{n:5,d:8},{n:7,d:8},
  {n:2,d:5},{n:3,d:5},{n:1,d:5},{n:1,d:10},{n:3,d:10}
];
const denomChoices = [2,3,4,5,6,8,10,12];

function pick(arr){ return arr[Math.floor(Math.random()*arr.length)]; }
function shuffle(arr){ const a=[...arr]; for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }

// ---------- confetti ----------
const confettiEmojis = ["🎉","🍕","⭐","🧀","🎊","🍅","🦋"];
function burstConfetti(){
  const layer = document.getElementById('confettiLayer');
  for(let i=0;i<24;i++){
    const el = document.createElement('div');
    el.className = 'confetti-piece';
    el.textContent = pick(confettiEmojis);
    el.style.left = Math.random()*100 + "vw";
    el.style.fontSize = (16+Math.random()*14)+"px";
    el.style.animationDuration = (1.6+Math.random()*1.2)+"s";
    layer.appendChild(el);
    setTimeout(()=>el.remove(), 3000);
  }
}
function reactAvatar(good){
  const av = document.querySelector('.avatar');
  if(!av) return;
  av.classList.remove('bounce','shake');
  void av.offsetWidth;
  av.classList.add(good ? 'bounce' : 'shake');
}

// ---------- SVG pizza rendering ----------
function buildPizzaSVG(denom, filledSet, interactive, extraClass="", eatenSet=null){
  const cx=115, cy=115, r=100;
  let paths = "";
  for(let i=0;i<denom;i++){
    const a0 = (i/denom)*2*Math.PI - Math.PI/2;
    const a1 = ((i+1)/denom)*2*Math.PI - Math.PI/2;
    const x0 = cx + r*Math.cos(a0), y0 = cy + r*Math.sin(a0);
    const x1 = cx + r*Math.cos(a1), y1 = cy + r*Math.sin(a1);
    const large = (a1-a0) > Math.PI ? 1 : 0;
    let stateCls = "untopped";
    if(eatenSet && eatenSet.has(i)) stateCls = "eaten";
    else if(filledSet.has(i)) stateCls = "topped";
    const cls = `slice ${stateCls} ${interactive ? "interactive":""}`;
    paths += `<path data-idx="${i}" class="${cls}" d="M${cx},${cy} L${x0.toFixed(2)},${y0.toFixed(2)} A${r},${r} 0 ${large} 1 ${x1.toFixed(2)},${y1.toFixed(2)} Z"></path>`;
  }
  let lines = "";
  for(let i=0;i<denom;i++){
    const a0 = (i/denom)*2*Math.PI - Math.PI/2;
    const x0 = cx + r*Math.cos(a0), y0 = cy + r*Math.sin(a0);
    lines += `<line class="slice-line" x1="${cx}" y1="${cy}" x2="${x0.toFixed(2)}" y2="${y0.toFixed(2)}"></line>`;
  }
  return `<svg class="pizza ${interactive?'':'static'} ${extraClass}" viewBox="0 0 230 230" data-denom="${denom}">
    ${paths}
    ${lines}
    <circle class="crust-ring" cx="${cx}" cy="${cy}" r="${r}"></circle>
  </svg>`;
}

function wirePizzaClicks(svgEl, filledSet, onChange){
  svgEl.querySelectorAll('.slice.interactive').forEach(p=>{
    p.addEventListener('click', ()=>{
      const idx = parseInt(p.dataset.idx);
      if(filledSet.has(idx)) filledSet.delete(idx);
      else filledSet.add(idx);
      p.classList.toggle('topped');
      p.classList.toggle('untopped');
      onChange && onChange();
    });
  });
}

// ---------- stage bar ----------
function renderStageBar(){
  const bar = document.getElementById('stagebar');
  bar.innerHTML = STAGES.map((s,i)=>{
    let cls = "stage-dot";
    if(i < stageIndex) cls += " done";
    else if(i === stageIndex) cls += " active";
    const icon = i < stageIndex ? "✓" : (i+1);
    return `<div class="${cls}"><span class="num">${icon}</span>${s}</div>`;
  }).join("");
}

function updateScore(delta){
  score = Math.max(0, score+delta);
  document.getElementById('scorePill').textContent = `⭐ Score: ${score}`;
  if(delta > 0){ streak += 1; } else if(delta < 0){ streak = 0; }
  document.getElementById('streakPill').textContent = `🔥 Streak: ${streak}`;
}

function goTo(nextIndex, renderFn){
  stageIndex = nextIndex;
  renderStageBar();
  renderFn();
}

// =========================================================
// STAGE 0: ICEBREAKER
// =========================================================
function renderIcebreakerStage(){
  const denom = 8, eatenCount = 3;
  const eatenSet = new Set([0,1,2]);
  const remainingSet = new Set([3,4,5,6,7]);
  const correct = "5/8";
  const options = shuffle(["5/8","3/8","3/5","8/5"]);

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    <div class="challenge-tag">ICEBREAKER</div>
    <div class="speech">
      <div class="avatar">🍕</div>
      <div class="bubble">Here's a pizza cut into <b>8 slices</b>. I already ate <b>3</b> of them. What fraction of the pizza is left?</div>
    </div>
    <div class="main-row">
      <div class="pizza-block">
        ${buildPizzaSVG(denom, remainingSet, false, "", eatenSet)}
        <div class="pizza-label">🧀 = left &nbsp; 〰️ = eaten</div>
      </div>
      <div class="controls">
        <div class="choice-row" id="iceChoices">
          ${options.map(o=>`<button class="choice-btn" data-val="${o}">${o}</button>`).join("")}
        </div>
        <div class="feedback" id="feedback"></div>
      </div>
    </div>
  `;

  document.getElementById('iceChoices').addEventListener('click',(e)=>{
    const btn = e.target.closest('.choice-btn');
    if(!btn) return;
    document.querySelectorAll('#iceChoices .choice-btn').forEach(b=>b.classList.remove('picked'));
    btn.classList.add('picked');
    const feedback = document.getElementById('feedback');
    feedback.classList.add('show');
    if(btn.dataset.val === correct){
      feedback.className = "feedback show good";
      feedback.textContent = `Exactly! 5 slices are still there out of 8 total, so 5/8 is left.`;
      updateScore(10); reactAvatar(true); burstConfetti();
      document.querySelectorAll('#iceChoices .choice-btn').forEach(b=>b.disabled=true);
      const nextHolder = document.createElement('div');
      nextHolder.style.marginTop = '14px';
      nextHolder.innerHTML = `<button class="primary teal" id="nextBtn">Let's learn how fractions work →</button>`;
      card.appendChild(nextHolder);
      document.getElementById('nextBtn').addEventListener('click', ()=> goTo(1, renderOrderStage));
    } else {
      feedback.className = "feedback show bad";
      feedback.textContent = `Count the slices that are still whole (not eaten) out of the total slices.`;
      updateScore(-2); reactAvatar(false);
    }
  });

  renderStageBar();
}

// =========================================================
// STAGE 1: ORDER (numerator / denominator)
// =========================================================
function renderOrderStage(){
  const target = pick(orderPool);
  let chosenDenom = null;
  const filled = new Set();

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    <div class="challenge-tag">PART 1 — NUMERATOR & DENOMINATOR</div>
    <div class="speech">
      <div class="avatar">🧑‍🍳</div>
      <div class="bubble">I want <span class="frac">${target.n}/${target.d}</span> of a pizza, please!</div>
    </div>
    <div class="main-row">
      <div class="pizza-block">
        <div class="pizza-label">Your pizza</div>
        <div id="pizzaHolder">${buildPizzaSVG(1, new Set(), false)}</div>
      </div>
      <div class="controls">
        <div class="control-group">
          <label>Step 1 — Cut the pizza into how many slices? (the denominator)</label>
          <div class="chip-row" id="denomChips">
            ${denomChoices.map(d=>`<button class="chip" data-d="${d}">${d}</button>`).join("")}
          </div>
        </div>
        <div class="control-group">
          <label>Step 2 — Tap slices to top with sauce (the numerator)</label>
          <div class="status-line" id="statusLine">Pick a slice count first.</div>
        </div>
        <div class="feedback" id="feedback"></div>
        <button class="primary" id="serveBtn" disabled>Serve it up! 🍕</button>
      </div>
    </div>
  `;

  const holder = document.getElementById('pizzaHolder');
  const statusLine = document.getElementById('statusLine');
  const feedback = document.getElementById('feedback');
  const serveBtn = document.getElementById('serveBtn');

  function refreshPizza(){
    holder.innerHTML = buildPizzaSVG(chosenDenom, filled, true);
    const svg = holder.querySelector('svg');
    wirePizzaClicks(svg, filled, ()=>{
      statusLine.textContent = `Topped ${filled.size} of ${chosenDenom} slices.`;
      serveBtn.disabled = filled.size === 0;
    });
  }

  document.getElementById('denomChips').addEventListener('click',(e)=>{
    const btn = e.target.closest('.chip');
    if(!btn) return;
    document.querySelectorAll('#denomChips .chip').forEach(c=>c.classList.remove('selected'));
    btn.classList.add('selected');
    chosenDenom = parseInt(btn.dataset.d);
    filled.clear();
    statusLine.textContent = `Cut into ${chosenDenom}! Now tap slices to top them.`;
    feedback.className = "feedback";
    refreshPizza();
  });

  serveBtn.addEventListener('click', ()=>{
    const denomOK = chosenDenom === target.d;
    const numOK = filled.size === target.n;
    feedback.classList.add('show');
    if(denomOK && numOK){
      feedback.className = "feedback show good";
      feedback.textContent = `Perfect! The denominator (${target.d}) is the total slices, the numerator (${target.n}) is how many you topped. 🎉`;
      updateScore(10);
      reactAvatar(true); burstConfetti();
      showNextButton();
    } else if(!denomOK){
      feedback.className = "feedback show bad";
      feedback.textContent = `Hmm — the order needs ${target.d} equal slices total, you cut ${chosenDenom}. Try again!`;
      updateScore(-2);
      reactAvatar(false);
    } else {
      feedback.className = "feedback show bad";
      feedback.textContent = `Close! You need ${target.n} topped slices out of ${chosenDenom}, you have ${filled.size}. Try again!`;
      updateScore(-2);
      reactAvatar(false);
    }
  });

  function showNextButton(){
    serveBtn.outerHTML = `<button class="primary teal" id="nextBtn">Next: Equivalent Fractions →</button>`;
    document.getElementById('nextBtn').addEventListener('click', ()=> goTo(2, renderEquivalentStage));
  }

  renderStageBar();
}

// =========================================================
// STAGE 2: EQUIVALENT FRACTIONS (fold & discover, then quick check)
// =========================================================
const equivalentQuizBank = [
  {base:{n:1,d:3}, correct:{n:2,d:6}, distractors:[{n:1,d:6},{n:3,d:6}]},
  {base:{n:1,d:4}, correct:{n:2,d:8}, distractors:[{n:1,d:8},{n:3,d:8}]},
  {base:{n:2,d:3}, correct:{n:4,d:6}, distractors:[{n:3,d:6},{n:2,d:6}]},
  {base:{n:3,d:4}, correct:{n:6,d:8}, distractors:[{n:5,d:8},{n:4,d:8}]},
];

function renderEquivalentStage(){
  renderEquivalentDiscovery();
}

function renderEquivalentDiscovery(){
  let step = 0; // 0: 1/2, 1: 2/4, 2: 4/8
  const stepsData = [
    {d:2, n:1, label:"1/2"},
    {d:4, n:2, label:"2/4"},
    {d:8, n:4, label:"4/8"},
  ];

  const card = document.getElementById('cardArea');
  function draw(){
    const cur = stepsData[step];
    const filled = new Set(Array.from({length:cur.n},(_,i)=>i));
    const equationParts = stepsData.slice(0, step+1).map(s=>`<span class="eq-frac">${s.label}</span>`).join(`<span class="eq-sign">=</span>`);
    card.innerHTML = `
      <div class="challenge-tag" style="background:var(--basil); box-shadow:0 3px 0 var(--basil-dark);">PART 2 — EQUIVALENT FRACTIONS</div>
      <div class="speech">
        <div class="avatar">📄</div>
        <div class="bubble">Imagine folding a paper pizza in half, then folding again. Watch what happens to the fraction when we cut the <b>same amount</b> into more pieces!</div>
      </div>
      <div class="pizza-block" style="margin:0 auto;">
        ${buildPizzaSVG(cur.d, filled, false)}
      </div>
      <div class="equation-row">${equationParts}</div>
      <div style="text-align:center;">
        ${step < stepsData.length-1
          ? `<button class="primary" id="foldBtn">Fold again →</button>`
          : `<div class="feedback show good" style="display:inline-block;">Same amount of pizza, every time — just cut into more pieces! That's what makes fractions equivalent.</div><br><button class="primary teal" id="tryBtn" style="margin-top:12px;">Try it yourself →</button>`
        }
      </div>
    `;
    if(step < stepsData.length-1){
      document.getElementById('foldBtn').addEventListener('click', ()=>{ step++; draw(); });
    } else {
      document.getElementById('tryBtn').addEventListener('click', renderEquivalentQuiz);
    }
  }
  draw();
  renderStageBar();
}

function renderEquivalentQuiz(){
  const q = pick(equivalentQuizBank);
  const filledBase = new Set(Array.from({length:q.base.n},(_,i)=>i));
  let optionFracs = shuffle([q.correct, ...q.distractors]);

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    <div class="challenge-tag" style="background:var(--basil); box-shadow:0 3px 0 var(--basil-dark);">PART 2 — QUICK CHECK</div>
    <div class="speech">
      <div class="avatar">📄</div>
      <div class="bubble">This pizza shows <span class="frac">${q.base.n}/${q.base.d}</span>. Which of these pizzas shows the <b>same amount</b> of pizza, just cut differently?</div>
    </div>
    <div class="pizza-block" style="margin:0 auto 14px;">
      ${buildPizzaSVG(q.base.d, filledBase, false)}
      <div class="pizza-label">${q.base.n}/${q.base.d}</div>
    </div>
    <div class="three-pizza-row" id="eqOptions">
      ${optionFracs.map((f,i)=>{
        const filled = new Set(Array.from({length:f.n},(_,idx)=>idx));
        return `<div class="pizza-frame pickable" data-n="${f.n}" data-d="${f.d}">
          ${buildPizzaSVG(f.d, filled, false, "small")}
          <div class="pizza-label">${f.n}/${f.d}</div>
        </div>`;
      }).join("")}
    </div>
    <div class="feedback" id="feedback" style="text-align:center; margin-top:14px;"></div>
  `;

  document.getElementById('eqOptions').addEventListener('click', (e)=>{
    const frame = e.target.closest('.pizza-frame');
    if(!frame) return;
    document.querySelectorAll('#eqOptions .pizza-frame').forEach(f=>f.classList.remove('picked'));
    frame.classList.add('picked');
    const n = parseInt(frame.dataset.n), d = parseInt(frame.dataset.d);
    const feedback = document.getElementById('feedback');
    feedback.classList.add('show');
    if(n/d === q.base.n/q.base.d){
      feedback.className = "feedback show good";
      feedback.textContent = `Yes! ${q.base.n}/${q.base.d} = ${n}/${d} — same amount of pizza, different number of slices.`;
      updateScore(10); reactAvatar(true); burstConfetti();
      const holder = document.createElement('div');
      holder.style.textAlign = 'center';
      holder.style.marginTop = '14px';
      holder.innerHTML = `<button class="primary purple" id="nextBtn">Next: Number Line →</button>`;
      card.appendChild(holder);
      document.getElementById('nextBtn').addEventListener('click', ()=> goTo(3, renderNumberLineStage));
    } else {
      feedback.className = "feedback show bad";
      feedback.textContent = `Not quite — check how many slices are topped compared to the total, and see if it matches the same share.`;
      updateScore(-2); reactAvatar(false);
    }
  });

  renderStageBar();
}

// =========================================================
// STAGE 3: NUMBER LINE
// =========================================================
function renderNumberLineStage(){
  const targets = [
    {label:"1/4", value:0.25},
    {label:"1/2", value:0.5},
    {label:"3/4", value:0.75},
  ];
  const tokens = shuffle(targets);
  let selectedToken = null;
  let placedCount = 0;

  const ticks = [];
  for(let i=0;i<=8;i++){ ticks.push(i/8); }

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    <div class="challenge-tag" style="background:var(--teal); box-shadow:0 3px 0 var(--teal-dark);">PART 3 — COMPARING WITH A NUMBER LINE</div>
    <div class="speech">
      <div class="avatar">📏</div>
      <div class="bubble">Place <span class="frac">1/4</span>, <span class="frac">1/2</span>, and <span class="frac">3/4</span> onto the number line where they belong.</div>
    </div>
    <div class="token-tray" id="tokenTray">
      ${tokens.map(t=>`<button class="token-chip" data-label="${t.label}" data-value="${t.value}">${t.label}</button>`).join("")}
    </div>
    <div class="numberline-wrap" id="nlWrap">
      <div class="numberline-track"></div>
      ${ticks.map(v=>`<div class="nl-tick" data-value="${v}" style="left:${v*100}%;"></div>`).join("")}
      <div class="nl-endlabel" style="left:0%;">0</div>
      <div class="nl-endlabel" style="left:100%;">1</div>
    </div>
    <div class="status-line" id="nlStatus" style="text-align:center;">Tap a fraction above, then tap where it belongs on the line.</div>
    <div class="feedback" id="feedback" style="text-align:center;"></div>
  `;

  const tray = document.getElementById('tokenTray');
  const wrap = document.getElementById('nlWrap');
  const statusLine = document.getElementById('nlStatus');
  const feedback = document.getElementById('feedback');

  tray.addEventListener('click', (e)=>{
    const btn = e.target.closest('.token-chip');
    if(!btn || btn.classList.contains('used')) return;
    document.querySelectorAll('.token-chip').forEach(b=>b.classList.remove('selected'));
    btn.classList.add('selected');
    selectedToken = btn;
    statusLine.textContent = `Now tap the spot on the line for ${btn.dataset.label}.`;
  });

  wrap.addEventListener('click', (e)=>{
    const tick = e.target.closest('.nl-tick');
    if(!tick || tick.classList.contains('filled')) return;
    if(!selectedToken){
      statusLine.textContent = `Pick a fraction chip first!`;
      return;
    }
    const tokenVal = parseFloat(selectedToken.dataset.value);
    const tickVal = parseFloat(tick.dataset.value);
    if(Math.abs(tokenVal - tickVal) < 0.001){
      tick.classList.add('filled');
      const lbl = document.createElement('div');
      lbl.className = 'nl-placed-label';
      lbl.textContent = selectedToken.dataset.label;
      lbl.style.left = (tickVal*100) + "%";
      wrap.appendChild(lbl);
      selectedToken.classList.add('used');
      selectedToken.classList.remove('selected');
      selectedToken = null;
      placedCount++;
      updateScore(8); reactAvatar(true);
      feedback.classList.add('show');
      feedback.className = "feedback show good";
      feedback.textContent = `Nice placement!`;
      if(placedCount === tokens.length){
        burstConfetti();
        feedback.textContent = `All placed correctly! Notice how the further right on the line, the bigger the fraction. 📏`;
        const holder = document.createElement('div');
        holder.style.textAlign = 'center';
        holder.style.marginTop = '14px';
        holder.innerHTML = `<button class="primary pink" id="nextBtn">Next: Butterfly Method →</button>`;
        card.appendChild(holder);
        document.getElementById('nextBtn').addEventListener('click', ()=> goTo(4, renderButterflyStage));
      } else {
        statusLine.textContent = `Pick the next fraction chip.`;
      }
    } else {
      feedback.classList.add('show');
      feedback.className = "feedback show bad";
      feedback.textContent = `Not quite that spot — think about how far ${selectedToken.dataset.label} is between 0 and 1.`;
      updateScore(-2); reactAvatar(false);
    }
  });

  renderStageBar();
}

// =========================================================
// STAGE 4: BUTTERFLY METHOD
// =========================================================
function mcqOptionsFor(correct){
  let opts = new Set([correct]);
  while(opts.size < 3){
    const delta = Math.floor(Math.random()*10)+2;
    const variant = Math.random()<0.5 ? correct+delta : Math.max(1, correct-delta);
    opts.add(variant);
  }
  return shuffle([...opts]);
}

function renderButterflyStage(fixedPair=null){
  const pair = fixedPair || {a:{n:3,d:4}, b:{n:5,d:8}};
  const { a, b } = pair;
  const prod1 = a.n * b.d; // top-left x bottom-right
  const prod2 = b.n * a.d; // top-right x bottom-left
  let winner;
  if(prod1 > prod2) winner = "A";
  else if(prod2 > prod1) winner = "B";
  else winner = "EQUAL";

  const opts1 = mcqOptionsFor(prod1);
  const opts2 = mcqOptionsFor(prod2);

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    <div class="challenge-tag" style="background:var(--purple); box-shadow:0 3px 0 var(--purple-dark);">MATH TRICK — 🦋 BUTTERFLY MAGIC</div>
    <div class="speech">
      <div class="avatar">🦋</div>
      <div class="bubble">To compare <span class="frac">${a.n}/${a.d}</span> and <span class="frac">${b.n}/${b.d}</span> fast, multiply diagonally — like butterfly wings!</div>
    </div>
    <div class="butterfly-row">
      <div class="bfrac"><span>${a.n}</span><span class="bar"></span><span>${a.d}</span></div>
      <div class="bfly-emoji">🦋</div>
      <div class="bfrac"><span>${b.n}</span><span class="bar"></span><span>${b.d}</span></div>
    </div>
    <div id="bflySteps"></div>
  `;

  const stepsHolder = document.getElementById('bflySteps');

  function renderStep1(){
    stepsHolder.innerHTML = `
      <div class="bstep">
        <div class="bstep-label">Step 1 — Multiply diagonally: ${a.n} (top-left) × ${b.d} (bottom-right)</div>
        <div class="choice-row" id="step1Choices">
          ${opts1.map(o=>`<button class="choice-btn" data-val="${o}">${o}</button>`).join("")}
        </div>
        <div class="feedback" id="fb1"></div>
      </div>
    `;
    document.getElementById('step1Choices').addEventListener('click',(e)=>{
      const btn = e.target.closest('.choice-btn');
      if(!btn) return;
      document.querySelectorAll('#step1Choices .choice-btn').forEach(b=>b.classList.remove('picked'));
      btn.classList.add('picked');
      const fb = document.getElementById('fb1');
      fb.classList.add('show');
      if(parseInt(btn.dataset.val) === prod1){
        fb.className = "feedback show good";
        fb.textContent = `Right! ${a.n} × ${b.d} = ${prod1}.`;
        updateScore(6); reactAvatar(true);
        document.querySelectorAll('#step1Choices .choice-btn').forEach(b=>b.disabled=true);
        setTimeout(renderStep2, 400);
      } else {
        fb.className = "feedback show bad";
        fb.textContent = `Try again — multiply ${a.n} by ${b.d}.`;
        updateScore(-2); reactAvatar(false);
      }
    });
  }

  function renderStep2(){
    const step2Div = document.createElement('div');
    step2Div.className = "bstep";
    step2Div.innerHTML = `
      <div class="bstep-label">Step 2 — Multiply diagonally: ${b.n} (top-right) × ${a.d} (bottom-left)</div>
      <div class="choice-row" id="step2Choices">
        ${opts2.map(o=>`<button class="choice-btn" data-val="${o}">${o}</button>`).join("")}
      </div>
      <div class="feedback" id="fb2"></div>
    `;
    stepsHolder.appendChild(step2Div);
    document.getElementById('step2Choices').addEventListener('click',(e)=>{
      const btn = e.target.closest('.choice-btn');
      if(!btn) return;
      document.querySelectorAll('#step2Choices .choice-btn').forEach(b=>b.classList.remove('picked'));
      btn.classList.add('picked');
      const fb = document.getElementById('fb2');
      fb.classList.add('show');
      if(parseInt(btn.dataset.val) === prod2){
        fb.className = "feedback show good";
        fb.textContent = `Right! ${b.n} × ${a.d} = ${prod2}.`;
        updateScore(6); reactAvatar(true);
        document.querySelectorAll('#step2Choices .choice-btn').forEach(b=>b.disabled=true);
        setTimeout(renderStep3, 400);
      } else {
        fb.className = "feedback show bad";
        fb.textContent = `Try again — multiply ${b.n} by ${a.d}.`;
        updateScore(-2); reactAvatar(false);
      }
    });
  }

  function renderStep3(){
    const step3Div = document.createElement('div');
    step3Div.className = "bstep";
    step3Div.innerHTML = `
      <div class="bstep-label">Step 3 — Compare: ${prod1} vs ${prod2}. Which fraction is bigger?</div>
      <div class="choice-row" id="step3Choices">
        <button class="choice-btn" data-val="A">${a.n}/${a.d}</button>
        <button class="choice-btn" data-val="B">${b.n}/${b.d}</button>
        <button class="choice-btn" data-val="EQUAL">They're equal</button>
      </div>
      <div class="feedback" id="fb3"></div>
    `;
    stepsHolder.appendChild(step3Div);
    document.getElementById('step3Choices').addEventListener('click',(e)=>{
      const btn = e.target.closest('.choice-btn');
      if(!btn) return;
      document.querySelectorAll('#step3Choices .choice-btn').forEach(b=>b.classList.remove('picked'));
      btn.classList.add('picked');
      const fb = document.getElementById('fb3');
      fb.classList.add('show');
      if(btn.dataset.val === winner){
        fb.className = "feedback show good";
        fb.textContent = winner === "EQUAL"
          ? `Correct — ${prod1} = ${prod2}, so they're equal!`
          : `Correct! ${Math.max(prod1,prod2)} > ${Math.min(prod1,prod2)}, so ${winner==="A"?`${a.n}/${a.d}`:`${b.n}/${b.d}`} is bigger. 🦋 Butterfly Magic!`;
        updateScore(8); reactAvatar(true); burstConfetti();
        document.querySelectorAll('#step3Choices .choice-btn').forEach(b=>b.disabled=true);
        const holder = document.createElement('div');
        holder.style.textAlign = 'center';
        holder.style.marginTop = '14px';
        holder.innerHTML = `
          <button class="ghost" id="tryAnotherBtn" style="margin-right:8px;">Try another pair</button>
          <button class="primary" id="nextBtn">Next: Challenges →</button>
        `;
        stepsHolder.appendChild(holder);
        document.getElementById('tryAnotherBtn').addEventListener('click', ()=>{
          const bank = [
            {a:{n:2,d:3}, b:{n:3,d:5}},
            {a:{n:5,d:6}, b:{n:4,d:5}},
            {a:{n:3,d:5}, b:{n:5,d:8}},
            {a:{n:2,d:5}, b:{n:3,d:7}},
          ];
          renderButterflyStage(pick(bank));
        });
        document.getElementById('nextBtn').addEventListener('click', ()=>{
          challengeRound = 1;
          goTo(5, renderChallengeStage);
        });
      } else {
        fb.className = "feedback show bad";
        fb.textContent = `Compare the two products again — the bigger cross-product's fraction wins.`;
        updateScore(-2); reactAvatar(false);
      }
    });
  }

  renderStep1();
  renderStageBar();
}

// =========================================================
// STAGE 5: CHALLENGE ROUND (mixed mastery mini-games)
// =========================================================
const challengeTypes = ["simplify","trueFalse","halfSort","orderThree"];

function renderChallengeStage(){
  const type = challengeTypes[(challengeRound-1) % challengeTypes.length];
  if(type === "simplify") renderSimplifyChallenge();
  else if(type === "trueFalse") renderTrueFalseChallenge();
  else if(type === "halfSort") renderHalfSortChallenge();
  else renderOrderThreeChallenge();
  renderStageBar();
}

function challengeHeader(tagText, promptHtml, avatarEmoji="🧑‍🍳"){
  return `
    <div class="challenge-tag" style="background:var(--purple); box-shadow:0 3px 0 var(--purple-dark);">CHALLENGE ${challengeRound} OF ${TOTAL_CHALLENGE_ROUNDS} — ${tagText}</div>
    <div class="speech">
      <div class="avatar">${avatarEmoji}</div>
      <div class="bubble">${promptHtml}</div>
    </div>
  `;
}

function advanceOrFinish(){
  const card = document.getElementById('cardArea');
  if(challengeRound < TOTAL_CHALLENGE_ROUNDS){
    const btn = document.createElement('div');
    btn.style.textAlign = 'center';
    btn.style.marginTop = '14px';
    btn.innerHTML = `<button class="primary purple" id="nextChallengeBtn">Next Challenge →</button>`;
    card.appendChild(btn);
    document.getElementById('nextChallengeBtn').addEventListener('click', ()=>{
      challengeRound += 1;
      renderChallengeStage();
    });
  } else {
    const btn = document.createElement('div');
    btn.style.textAlign = 'center';
    btn.style.marginTop = '14px';
    btn.innerHTML = `<div class="bubble" style="display:inline-block; margin-bottom:10px;">You finished Day 2 — Fraction Fun Factory! Great work! 🏆</div><br><button class="primary" id="playAgainBtn">Play again from the start 🍕</button>`;
    card.appendChild(btn);
    document.getElementById('playAgainBtn').addEventListener('click', ()=> goTo(0, renderIcebreakerStage));
  }
}

// ---- Challenge A: Simplify It ----
const simplifyBank = [
  {n:2,d:4},{n:2,d:6},{n:4,d:8},{n:3,d:9},{n:6,d:8},{n:4,d:6},{n:2,d:10},{n:5,d:10}
];
function renderSimplifyChallenge(){
  const q = pick(simplifyBank);
  const simp = simplify(q.n,q.d);
  const filled = new Set(Array.from({length:q.n},(_,i)=>i));

  let options = [`${simp.n}/${simp.d}`];
  while(options.length < 3){
    const fakeD = pick([2,3,4,5,6,8,10]);
    const fakeN = Math.max(1, Math.floor(Math.random()*fakeD));
    const label = `${fakeN}/${fakeD}`;
    if(!options.includes(label) && fakeN/fakeD !== simp.n/simp.d) options.push(label);
  }
  options = shuffle(options);

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    ${challengeHeader("SIMPLIFY IT", `This pizza shows <span class="frac">${q.n}/${q.d}</span>. What's that fraction in <b>simplest form</b>?`, "🍕")}
    <div class="main-row">
      <div class="pizza-block">
        ${buildPizzaSVG(q.d, filled, false)}
      </div>
      <div class="controls">
        <div class="choice-row" id="simpChoices">
          ${options.map(o=>`<button class="choice-btn" data-val="${o}">${o}</button>`).join("")}
        </div>
        <div class="feedback" id="feedback"></div>
      </div>
    </div>
  `;

  document.getElementById('simpChoices').addEventListener('click',(e)=>{
    const btn = e.target.closest('.choice-btn');
    if(!btn) return;
    document.querySelectorAll('#simpChoices .choice-btn').forEach(b=>b.classList.remove('picked'));
    btn.classList.add('picked');
    const feedback = document.getElementById('feedback');
    feedback.classList.add('show');
    const correct = `${simp.n}/${simp.d}`;
    if(btn.dataset.val === correct){
      feedback.className = "feedback show good";
      feedback.textContent = `Yes! ${q.n}/${q.d} simplifies to ${correct}.`;
      updateScore(10); reactAvatar(true); burstConfetti();
      document.querySelectorAll('#simpChoices .choice-btn').forEach(b=>b.style.pointerEvents='none');
      advanceOrFinish();
    } else {
      feedback.className = "feedback show bad";
      feedback.textContent = `Not quite — try dividing top and bottom by the same number.`;
      updateScore(-2); reactAvatar(false);
    }
  });
}

// ---- Challenge B: True or False ----
function renderTrueFalseChallenge(){
  const q = pick(orderPool);
  const isTrue = Math.random() < 0.5;
  let shownN = q.n, shownD = q.d;
  if(!isTrue){
    shownN = q.n + (Math.random()<0.5 ? 1 : -1);
    if(shownN <= 0) shownN = q.n + 1;
    if(shownN >= shownD) shownN = shownD - 1;
  }
  const filled = new Set(Array.from({length:q.n},(_,i)=>i));

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    ${challengeHeader("TRUE OR FALSE", `This pizza is labeled <span class="frac">${shownN}/${shownD}</span>. Is that label correct?`, "🍕")}
    <div class="main-row">
      <div class="pizza-block">
        ${buildPizzaSVG(q.d, filled, false)}
        <div class="pizza-label">Label: ${shownN}/${shownD}</div>
      </div>
      <div class="controls">
        <div class="choice-row">
          <button class="choice-btn tf-true" data-val="true">True ✅</button>
          <button class="choice-btn tf-false" data-val="false">False ❌</button>
        </div>
        <div class="feedback" id="feedback"></div>
      </div>
    </div>
  `;

  document.querySelectorAll('.choice-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('.choice-btn').forEach(b=>b.classList.remove('picked'));
      btn.classList.add('picked');
      const feedback = document.getElementById('feedback');
      feedback.classList.add('show');
      const userSaysTrue = btn.dataset.val === "true";
      if(userSaysTrue === isTrue){
        feedback.className = "feedback show good";
        feedback.textContent = isTrue
          ? `Correct — ${q.n} out of ${q.d} slices really are topped!`
          : `Correct — the pizza actually shows ${q.n}/${q.d}, not ${shownN}/${shownD}.`;
        updateScore(10); reactAvatar(true); burstConfetti();
        document.querySelectorAll('.choice-btn').forEach(b=>b.style.pointerEvents='none');
        advanceOrFinish();
      } else {
        feedback.className = "feedback show bad";
        feedback.textContent = `Look again — count the topped slices out of the total slices.`;
        updateScore(-2); reactAvatar(false);
      }
    });
  });
}

// ---- Challenge C: More/Less/Equal to 1/2 ----
function renderHalfSortChallenge(){
  const q = pick(orderPool);
  const val = q.n/q.d;
  let answer;
  if(Math.abs(val - 0.5) < 1e-9) answer = "EQUAL";
  else answer = val > 0.5 ? "MORE" : "LESS";
  const filled = new Set(Array.from({length:q.n},(_,i)=>i));

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    ${challengeHeader("HALF OR NOT?", `Is <span class="frac">${q.n}/${q.d}</span> of this pizza more than half, less than half, or exactly half?`, "🍕")}
    <div class="main-row">
      <div class="pizza-block">
        ${buildPizzaSVG(q.d, filled, false)}
      </div>
      <div class="controls">
        <div class="choice-row">
          <button class="choice-btn" data-val="MORE">More than half</button>
          <button class="choice-btn" data-val="LESS">Less than half</button>
          <button class="choice-btn" data-val="EQUAL">Exactly half</button>
        </div>
        <div class="feedback" id="feedback"></div>
      </div>
    </div>
  `;

  document.querySelectorAll('.choice-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('.choice-btn').forEach(b=>b.classList.remove('picked'));
      btn.classList.add('picked');
      const feedback = document.getElementById('feedback');
      feedback.classList.add('show');
      if(btn.dataset.val === answer){
        feedback.className = "feedback show good";
        feedback.textContent = `Right! ${q.n}/${q.d} is ${answer === "EQUAL" ? "exactly half" : (answer === "MORE" ? "more than half" : "less than half")} of the pizza.`;
        updateScore(10); reactAvatar(true); burstConfetti();
        document.querySelectorAll('.choice-btn').forEach(b=>b.style.pointerEvents='none');
        advanceOrFinish();
      } else {
        feedback.className = "feedback show bad";
        feedback.textContent = `Try comparing ${q.n} to half of ${q.d}.`;
        updateScore(-2); reactAvatar(false);
      }
    });
  });
}

// ---- Challenge D: Order three fractions least to greatest ----
function renderOrderThreeChallenge(){
  let picks = [];
  while(picks.length < 3){
    const cand = pick(orderPool);
    if(!picks.some(p=>p.n/p.d === cand.n/cand.d)) picks.push(cand);
  }
  const correctOrder = [...picks].sort((a,b)=> a.n/a.d - b.n/b.d);
  const displayOrder = shuffle(picks);
  let selections = [];

  const card = document.getElementById('cardArea');
  card.innerHTML = `
    ${challengeHeader("ORDER THE PIZZAS", `Tap the pizzas in order from <b>least</b> to <b>greatest</b> amount of pizza.`, "🍕")}
    <div class="three-pizza-row" id="threeRow">
      ${displayOrder.map((p,i)=>{
        const filled = new Set(Array.from({length:p.n},(_,idx)=>idx));
        return `<div class="pizza-frame pickable order-tag" data-idx="${i}" data-n="${p.n}" data-d="${p.d}">
          ${buildPizzaSVG(p.d, filled, false, "small")}
          <div class="pizza-label">${p.n}/${p.d}</div>
        </div>`;
      }).join("")}
    </div>
    <div class="feedback" id="feedback" style="text-align:center; margin-top:14px;"></div>
  `;

  document.getElementById('threeRow').addEventListener('click', (e)=>{
    const frame = e.target.closest('.pizza-frame');
    if(!frame || frame.classList.contains('picked')) return;
    const n = parseInt(frame.dataset.n), d = parseInt(frame.dataset.d);
    selections.push({n,d,frame});
    frame.classList.add('picked');
    const badge = document.createElement('div');
    badge.className = 'order-badge';
    badge.textContent = selections.length;
    frame.appendChild(badge);

    if(selections.length === 3){
      const feedback = document.getElementById('feedback');
      feedback.classList.add('show');
      const isCorrect = selections.every((s,i)=> s.n/s.d === correctOrder[i].n/correctOrder[i].d);
      if(isCorrect){
        feedback.className = "feedback show good";
        feedback.textContent = `Nice ordering! Least to greatest: ${correctOrder.map(p=>`${p.n}/${p.d}`).join(" < ")}.`;
        updateScore(10); reactAvatar(true); burstConfetti();
        advanceOrFinish();
      } else {
        feedback.className = "feedback show bad";
        feedback.textContent = `Not quite — the correct order was ${correctOrder.map(p=>`${p.n}/${p.d}`).join(" < ")}. Moving on!`;
        updateScore(-2); reactAvatar(false);
        setTimeout(()=>advanceOrFinish(), 300);
      }
    }
  });
}

// ---------- init ----------
document.getElementById('resetBtn').addEventListener('click', ()=>{
  score = 0;
  streak = 0;
  updateScore(0);
  goTo(0, renderIcebreakerStage);
});

renderStageBar();
renderIcebreakerStage();
</script>
</body>
</html>
