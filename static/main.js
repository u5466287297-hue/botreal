
let interval = window.APP_INTERVAL||60;
let remaining = interval;

async function fetchStatus(){
  try{
    let r = await fetch("/api/status");
    let j = await r.json();
    document.getElementById("signalText").textContent = j.signal==="BUY"?"Купи":(j.signal==="SELL"?"Продай":"Няма сигнал");
    document.getElementById("confText").textContent = `Увереност: ${j.confidence}%`;
    const s = j.stats;
    document.getElementById("todayStats").textContent = `Сигнали: ${s.today_signals} | Купи: ${s.today_buy} | Продай: ${s.today_sell} | Точност: ${s.today_accuracy}%`;
    document.getElementById("allStats").textContent = `Win: ${s.win} | Loss: ${s.loss} | Точност: ${s.accuracy}%`;
    remaining = j.next_in;

    // Chart
    let traceCandle = {
      x: j.chart.times,
      open: j.chart.opens,
      high: j.chart.highs,
      low: j.chart.lows,
      close: j.chart.closes,
      type: "candlestick",
      name: "Цена"
    };
    let traceBuy = {
      x: j.chart.times,
      y: j.chart.closes.map((c,i)=> j.chart.buys.includes(i)?c:null),
      mode: "markers",
      marker: {color:"lime", symbol:"triangle-up", size:12},
      name:"Купи"
    };
    let traceSell = {
      x: j.chart.times,
      y: j.chart.closes.map((c,i)=> j.chart.sells.includes(i)?c:null),
      mode: "markers",
      marker: {color:"red", symbol:"triangle-down", size:12},
      name:"Продай"
    };
    Plotly.newPlot("chart",[traceCandle,traceBuy,traceSell],{margin:{t:20},paper_bgcolor:"#111827",plot_bgcolor:"#111827",font:{color:"#e5e7eb"}});
  }catch(e){console.error(e)}
}

function tick(){
  remaining = Math.max(0,remaining-1);
  document.getElementById("countdown").textContent = remaining;
  document.getElementById("progress").style.width = ((interval-remaining)/interval*100)+"%";
  if(remaining<=0){fetchStatus()}
}

fetchStatus();
setInterval(tick,1000);
