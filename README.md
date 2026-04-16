[index.html](https://github.com/user-attachments/files/26768906/index.html)
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>2026五一贵州五日游</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--primary:#2d8a4e;--primary-dark:#1a5c35;--bg:#f0f7f4;--card-bg:#fff;--text:#333;--text-light:#666;--warning:#ff9800;--free:#4caf50}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden}
.header{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);color:white;padding:40px 20px;text-align:center;position:relative;overflow:hidden}
.header::before{content:"";position:absolute;top:0;left:0;right:0;bottom:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M0 50 Q25 30 50 50 T100 50 V100 H0Z' fill='rgba(255,255,255,0.1)'/%3E%3C/svg%3E") repeat-x;background-size:200px 100px}
.header h1{font-size:26px;font-weight:700;margin-bottom:8px;position:relative}
.header .subtitle{font-size:14px;opacity:0.9;position:relative}
.stats{display:flex;justify-content:center;gap:30px;padding:20px;background:white;margin:-20px 20px 20px;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,0.08);position:relative;z-index:1}
.stat{text-align:center}
.stat-num{font-size:24px;font-weight:700;color:var(--primary)}
.stat-label{font-size:12px;color:var(--text-light)}
.container{max-width:900px;margin:0 auto;padding:0 16px 80px}
.card{background:var(--card-bg);border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 2px 12px rgba(0,0,0,0.06);opacity:0;transform:translateY(20px);transition:all 0.5s ease}
.card.visible{opacity:1;transform:translateY(0)}
.card-title{font-size:17px;font-weight:600;color:var(--primary);margin-bottom:16px;display:flex;align-items:center;gap:10px}
.card-title::before{content:"";width:5px;height:20px;background:linear-gradient(180deg,var(--primary),var(--primary-dark));border-radius:3px}
.alert-card{background:linear-gradient(135deg,#fff3e0,#fff);border-left:4px solid var(--warning)}
.alert-title{color:#e65100;font-weight:600;font-size:15px;margin-bottom:8px;display:flex;align-items:center;gap:6px}
.route-flow{display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;padding:10px 0}
.route-node{background:linear-gradient(135deg,var(--primary),var(--primary-dark));color:white;padding:8px 16px;border-radius:20px;font-size:13px;font-weight:500}
.route-arrow{color:var(--primary);font-size:18px}
.transport-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}
.transport-item{background:#f8faf8;padding:14px;border-radius:12px;display:flex;justify-content:space-between;align-items:center}
.transport-item .train{font-weight:600;color:var(--primary)}
.transport-item .time{color:var(--text-light);font-size:13px}
.hotel-list .hotel-item{padding:14px 0;border-bottom:1px solid #eee}
.hotel-list .hotel-item:last-child{border-bottom:none}
.hotel-item .name{font-weight:600;color:var(--text)}
.hotel-item .detail{font-size:13px;color:var(--text-light);margin-top:4px}
.spot-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}
.spot-card{background:#f8faf8;border-radius:12px;padding:16px;border-left:4px solid var(--free);cursor:pointer;transition:all 0.3s}
.spot-card:hover,.spot-card:active{transform:scale(1.02);box-shadow:0 4px 16px rgba(0,0,0,0.1)}
.spot-card.warning{border-left-color:var(--warning)}
.spot-card .spot-name{font-weight:600;font-size:15px;margin-bottom:6px;display:flex;align-items:center;gap:6px}
.spot-card .spot-info{font-size:13px;color:var(--text-light)}
.spot-card .spot-tag{display:inline-block;background:var(--free);color:white;padding:2px 8px;border-radius:10px;font-size:11px;margin-top:6px}
.spot-card .spot-tag.warning{background:var(--warning)}
.spot-card .map-hint{font-size:11px;color:var(--primary);margin-top:8px;display:flex;align-items:center;gap:4px}
.tabs{display:flex;gap:4px;overflow-x:auto;padding-bottom:10px;margin-bottom:16px;-webkit-overflow-scrolling:touch}
.tab{padding:10px 20px;background:#e8f5ec;border-radius:10px;font-size:14px;font-weight:500;color:var(--text-light);white-space:nowrap;cursor:pointer;transition:all 0.3s}
.tab.active{background:var(--primary);color:white}
.tab-content{display:none}
.tab-content.active{display:block}
.timeline{padding-left:24px;border-left:2px solid #e8f5ec;margin-left:8px}
.day-block{position:relative;margin-bottom:24px;padding-left:16px}
.day-block::before{content:"";position:absolute;left:-29px;top:4px;width:14px;height:14px;background:var(--primary);border-radius:50%;border:3px solid white;box-shadow:0 0 0 2px var(--primary)}
.day-block .time{font-size:13px;color:var(--text-light);margin-bottom:4px}
.day-block .content{font-size:14px;font-weight:500}
.day-block .content .highlight{color:var(--primary);font-weight:600}
.map-link{color:var(--primary);text-decoration:underline;text-decoration-style:dashed;cursor:pointer}
.map-link:hover{text-decoration-style:solid}
.food-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.food-item{background:#f8faf8;padding:14px;border-radius:12px;text-align:center;cursor:pointer;transition:all 0.3s}
.food-item:hover,.food-item:active{transform:scale(1.02)}
.food-item .emoji{font-size:28px;margin-bottom:6px}
.food-item .name{font-weight:600;font-size:14px}
.food-item .restaurant{font-size:12px;color:var(--text-light);margin-top:4px}
.food-daily{margin-top:16px}
.food-daily-item{display:flex;gap:12px;padding:10px 0;border-bottom:1px solid #eee}
.food-daily-item:last-child{border-bottom:none}
.food-daily-item .day{font-weight:600;color:var(--primary);min-width:60px}
.food-daily-item .meal{font-size:14px;cursor:pointer;color:var(--primary);text-decoration:underline dashed}
.weather-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px}
.weather-item{background:#f8faf8;padding:14px;border-radius:12px;text-align:center}
.weather-item .city{font-size:13px;color:var(--text-light)}
.weather-item .temp{font-size:20px;font-weight:700;color:var(--primary)}
.weather-item .desc{font-size:12px;color:var(--text-light)}
.tips{background:#f8faf8;padding:16px;border-radius:12px;font-size:14px}
.tips li{margin:6px 0;padding-left:20px;position:relative}
.tips li::before{content:"✓";position:absolute;left:0;color:var(--primary);font-weight:bold}
.nav{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #eee;display:flex;z-index:100;max-width:900px;margin:0 auto}
.nav a{flex:1;text-align:center;padding:12px 8px;font-size:11px;color:var(--text-light);text-decoration:none;transition:color 0.3s}
.nav a.active{color:var(--primary)}
.nav a span{display:block;font-size:20px;margin-bottom:4px}
.fee-table{width:100%;border-collapse:collapse}
.fee-table th,.fee-table td{padding:12px;text-align:left;border-bottom:1px solid #eee;font-size:14px}
.fee-table th{background:#f8faf8;font-weight:600;color:var(--text)}
.fee-table .total{font-weight:700;color:var(--primary)}
.badge-free{background:var(--free);color:white;padding:2px 8px;border-radius:10px;font-size:11px}
.badge-warn{background:var(--warning);color:white;padding:2px 8px;border-radius:10px;font-size:11px}
.map-modal{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.5);z-index:1000;display:none;justify-content:center;align-items:center;padding:20px}
.map-modal.active{display:flex}
.map-modal-content{background:white;border-radius:16px;padding:24px;max-width:400px;width:100%;max-height:80vh;overflow-y:auto}
.map-modal-title{font-weight:600;font-size:16px;margin-bottom:16px;color:var(--primary)}
.map-option{background:#f8faf8;padding:14px;border-radius:10px;margin-bottom:10px;cursor:pointer;transition:all 0.3s}
.map-option:hover,.map-option:active{background:#e8f5ec}
.map-option .name{font-weight:600;font-size:14px;margin-bottom:4px}
.map-option .app{font-size:12px;color:var(--text-light)}
.map-close{background:var(--primary);color:white;border:none;padding:12px 24px;border-radius:8px;width:100%;margin-top:10px;cursor:pointer;font-size:14px}
@keyframes fadeInUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@media(min-width:768px){
.container{padding:0 20px 100px}
.header{padding:50px 20px}
.stats{position:absolute;bottom:-30px;left:50%;transform:translateX(-50%);width:500px;border-radius:16px}
.header{position:relative;padding-bottom:60px}
.card{margin-bottom:20px;padding:28px}
}
</style>
</head>
<body>
<div class="header">
<h1>🏔️ 2026五一贵州五日游</h1>
<p class="subtitle">5月1日-5月5日 · 3人 · 成都/重庆 → 贵阳 → 荔波</p>
</div>
<div class="container">
<div class="card" id="overview">
<div class="card-title">🚨 紧急行动项</div>
<div class="alert-card" style="padding:16px;border-radius:12px;margin-bottom:12px">
<div class="alert-title">⚠️ 荔波小七孔5月3日门票</div>
<p style="font-size:14px;color:#666">五一非常抢手，很可能售罄，<strong>尽快抢购</strong>！</p>
</div>
<div style="background:#f8faf8;padding:14px;border-radius:12px">
<div style="font-weight:600;margin-bottom:8px">📍 预约平台</div>
<p style="font-size:14px;color:#666">"一码游贵州"小程序 / 携程 / 驴妈妈</p>
</div>
</div>
<div class="card">
<div class="card-title">🗺️ 路线总览</div>
<div class="route-flow">
<div class="route-node">成都/重庆</div>
<div class="route-arrow">→</div>
<div class="route-node">贵阳</div>
<div class="route-arrow">→</div>
<div class="route-node">荔波</div>
<div class="route-arrow">→</div>
<div class="route-node">贵阳</div>
<div class="route-arrow">→</div>
<div class="route-node">成都/重庆</div>
</div>
</div>
<div class="card">
<div class="card-title">💰 费用预估</div>
<table class="fee-table">
<tr><th>景区</th><th>门票</th><th>状态</th></tr>
<tr><td>荔波小七孔</td><td>待定</td><td><span class="badge-warn">需抢购</span></td></tr>
<tr><td>甲秀楼</td><td>免费</td><td><span class="badge-free">免费</span></td></tr>
<tr><td>黔灵山公园</td><td>免费</td><td><span class="badge-free">免费</span></td></tr>
<tr><td>贵州省博物馆</td><td>免费</td><td><span class="badge-free">免费</span></td></tr>
<tr><td>花溪公园</td><td>免费</td><td><span class="badge-free">免费</span></td></tr>
<tr><td class="total">合计</td><td class="total" colspan="2">待定（主要为荔波小七孔）</td></tr>
</table>
</div>
<div class="card">
<div class="card-title">🌤️ 天气预报</div>
<div class="weather-grid">
<div class="weather-item">
<div class="city">贵阳</div>
<div class="temp">16-23°C</div>
<div class="desc">阴雨</div>
</div>
<div class="weather-item">
<div class="city">荔波</div>
<div class="temp">17-25°C</div>
<div class="desc">阴雨</div>
</div>
</div>
<p style="font-size:12px;color:#999;margin-top:10px">⚠️ 记得携带雨具！</p>
</div>
<div class="card">
<div class="card-title">🚄 交通总览</div>
<div class="transport-grid">
<div class="transport-item"><div><div class="train">G5393</div><div class="time">成都南→贵阳北</div></div><div class="time">5月1日 09:10</div></div>
<div class="transport-item"><div><div class="train">G2883</div><div class="time">重庆西→贵阳北</div></div><div class="time">5月1日 10:01</div></div>
<div class="transport-item"><div><div class="train">G3569</div><div class="time">贵阳→荔波</div></div><div class="time">5月3日 08:28</div></div>
<div class="transport-item"><div><div class="train">C5872</div><div class="time">荔波→贵阳</div></div><div class="time">5月4日 14:42</div></div>
<div class="transport-item"><div><div class="train">G5360</div><div class="time">贵阳北→成都南/重庆西</div></div><div class="time">5月5日 14:55</div></div>
</div>
</div>
<div class="card">
<div class="card-title">🏨 住宿总览</div>
<div class="hotel-list">
<div class="hotel-item"><div class="name">全季酒店(贵阳喷水池)</div><div class="detail">5月1-3日 · 2晚 · 含双早</div></div>
<div class="hotel-item"><div class="name">维也纳酒店(荔波古镇)</div><div class="detail">5月3-4日 · 1晚 · 含双早</div></div>
<div class="hotel-item"><div class="name">全季酒店(贵阳喷水池)</div><div class="detail">5月4-5日 · 1晚 · 含双早</div></div>
</div>
</div>
<div class="card">
<div class="card-title">🎫 景区门票 <span style="font-size:12px;color:var(--text-light);font-weight:normal">(点击查看地图)</span></div>
<div class="spot-grid">
<div class="spot-card" onclick="openMap('甲秀楼','贵阳市南明区南明河畔')">
<div class="spot-name">🏯 甲秀楼</div>
<div class="spot-info">5月1日晚 · 免费</div>
<div class="spot-info">贵阳市区 · 无需预约</div>
<div class="map-hint">📍 点击打开地图</div>
</div>
<div class="spot-card" onclick="openMap('黔灵山公园','贵阳市云岩区黔灵山公园')">
<div class="spot-name">🏞️ 黔灵山公园</div>
<div class="spot-info">5月1日/2日 · 免费</div>
<div class="spot-info">爬山·熊猫·猴子·弘福寺</div>
<div class="map-hint">📍 点击打开地图</div>
</div>
<div class="spot-card" onclick="openMap('贵州省博物馆','贵阳市观山湖区林城东路')">
<div class="spot-name">🏛️ 贵州省博物馆</div>
<div class="spot-info">5月2日下午 · 免费</div>
<div class="spot-info">贵州历史文化 · 免预约</div>
<div class="map-hint">📍 点击打开地图</div>
</div>
<div class="spot-card" onclick="openMap('花溪公园','贵阳市花溪区花溪大道')">
<div class="spot-name">🌿 花溪公园/十里河滩</div>
<div class="spot-info">5月2日下午 · 免费</div>
<div class="spot-info">骑行·拍照·天然氧吧</div>
<div class="map-hint">📍 点击打开地图</div>
</div>
<div class="spot-card warning" onclick="openMap('荔波小七孔','黔南州荔波县小七孔景区')">
<div class="spot-name">🌊 荔波小七孔</div>
<div class="spot-info">5月3日 · 需预约</div>
<div class="spot-tag warning">⚠️ 尽快抢购</div>
<div class="map-hint">📍 点击打开地图</div>
</div>
</div>
</div>
<div class="card">
<div class="card-title">📅 每日行程 <span style="font-size:12px;color:var(--text-light);font-weight:normal">(点击地点打开地图)</span></div>
<div class="tabs">
<div class="tab active" onclick="showTab('day1')">Day1</div>
<div class="tab" onclick="showTab('day2')">Day2</div>
<div class="tab" onclick="showTab('day3')">Day3</div>
<div class="tab" onclick="showTab('day4')">Day4</div>
<div class="tab" onclick="showTab('day5')">Day5</div>
</div>
<div id="day1" class="tab-content active">
<div class="timeline">
<div class="day-block"><div class="time">09:10-12:11</div><div class="content"><span class="highlight">G5393</span> 成都南→贵阳北（2人）</div></div>
<div class="day-block"><div class="time">10:01-11:59</div><div class="content"><span class="highlight">G2883</span> 重庆西→贵阳北（1人）</div></div>
<div class="day-block"><div class="time">12:00-13:00</div><div class="content">🍜 <span class="map-link" onclick="openMap('玉珍酸笋火锅','贵阳市云岩区喷水池')">玉珍酸笋火锅</span>（喷水池店）午餐</div></div>
<div class="day-block"><div class="time">14:30-17:30</div><div class="content">🏞️ <span class="map-link" onclick="openMap('黔灵山公园','贵阳市云岩区黔灵山公园')">黔灵山公园</span>（市区公园）</div></div>
<div class="day-block"><div class="time">18:30-19:30</div><div class="content">🏯 <span class="map-link" onclick="openMap('甲秀楼','贵阳市南明区南明河畔')">甲秀楼夜景</span>（免费）</div></div>
<div class="day-block"><div class="time">晚餐</div><div class="content">🍲 <span class="map-link" onclick="openMap('菲姐小板凳斗米牛肉火锅','贵阳市观山湖区')">菲姐小板凳斗米牛肉火锅</span>（观山湖店）</div></div>
</div>
</div>
<div id="day2" class="tab-content">
<div class="timeline">
<div class="day-block"><div class="time">08:00</div><div class="content">🍳 起床早餐（酒店含早）</div></div>
<div class="day-block"><div class="time">09:00-11:30</div><div class="content">🏞️ <span class="map-link" onclick="openMap('黔灵山公园','贵阳市云岩区黔灵山公园')">黔灵山公园</span>（爬山、看熊猫、喂猴子、弘福寺）</div></div>
<div class="day-block"><div class="time">12:00-13:00</div><div class="content">🍜 午餐：<span class="map-link" onclick="openMap('肠旺面','贵阳市南明区')">肠旺面</span> 或 <span class="map-link" onclick="openMap('辣子鸡','贵阳市云岩区')">辣子鸡</span></div></div>
<div class="day-block"><div class="time">14:00-16:00</div><div class="content">🏛️ <span class="map-link" onclick="openMap('贵州省博物馆','贵阳市观山湖区林城东路')">贵州省博物馆</span>（了解贵州历史文化）</div></div>
<div class="day-block"><div class="time">16:30-18:00</div><div class="content">🌿 <span class="map-link" onclick="openMap('花溪公园','贵阳市花溪区花溪大道')">花溪公园/十里河滩</span>（骑行、拍照、天然氧吧）</div></div>
<div class="day-block"><div class="time">18:30</div><div class="content">🏨 返回酒店休息</div></div>
<div class="day-block"><div class="time">晚餐</div><div class="content">🍗 <span class="map-link" onclick="openMap('老刘鲜烤鸡','贵阳市云岩区黔灵东路')">老刘鲜烤鸡</span>（黔灵东路）必吃！</div></div>
</div>
</div>
<div id="day3" class="tab-content">
<div class="timeline">
<div class="day-block"><div class="time">07:30</div><div class="content">🍳 起床早餐退房（酒店含早）</div></div>
<div class="day-block"><div class="time">08:28-09:34</div><div class="content">🚄 <span class="highlight">G3569</span> 贵阳→荔波（高铁1小时）</div></div>
<div class="day-block"><div class="time">10:00-17:00</div><div class="content">🌊 <span class="map-link" onclick="openMap('荔波小七孔','黔南州荔波县小七孔景区')">荔波小七孔</span> ⚠️ 08:00入园，16:30停止</div></div>
<div class="day-block"><div class="time">17:00</div><div class="content">🏨 前往酒店入住（维也纳酒店）</div></div>
<div class="day-block"><div class="time">晚餐</div><div class="content">🐟 <span class="map-link" onclick="openMap('荔波烤鱼','黔南州荔波县古镇美食街')">荔波烤鱼</span>（荔波古镇美食街）</div></div>
</div>
</div>
<div id="day4" class="tab-content">
<div class="timeline">
<div class="day-block"><div class="time">上午</div><div class="content">🏘️ 自由活动 / 荔波古镇逛逛（早餐：豆花面或米片）</div></div>
<div class="day-block"><div class="time">14:00</div><div class="content">🚄 退房前往荔波站</div></div>
<div class="day-block"><div class="time">14:42-16:08</div><div class="content">🚄 <span class="highlight">C5872</span> 荔波→贵阳（高铁1.5小时）</div></div>
<div class="day-block"><div class="time">16:30</div><div class="content">🏨 前往全季酒店入住</div></div>
<div class="day-block"><div class="time">晚餐</div><div class="content">🍡 <span class="map-link" onclick="openMap('豆腐圆子','贵阳市南明区')">豆腐圆子</span> + <span class="map-link" onclick="openMap('贵阳烤串','贵阳市云岩区')">贵阳烤串</span></div></div>
</div>
</div>
<div id="day5" class="tab-content">
<div class="timeline">
<div class="day-block"><div class="time">上午</div><div class="content">🏙️ 自由活动</div></div>
<div class="day-block"><div class="time">早餐</div><div class="content">🍜 <span class="map-link" onclick="openMap('羊肉粉','贵阳市云岩区')">羊肉粉</span>（遵义羊肉粉）</div></div>
<div class="day-block"><div class="time">12:00-13:00</div><div class="content">🍽️ 午餐退房</div></div>
<div class="day-block"><div class="time">14:55</div><div class="content">🚄 <span class="highlight">G5360</span> 贵阳北→成都南（2人）</div></div>
<div class="day-block"><div class="time">14:55</div><div class="content">🚄 <span class="highlight">G5360</span> 贵阳北→重庆西（1人）</div></div>
</div>
</div>
</div>
<div class="card">
<div class="card-title">🍜 美食地图 <span style="font-size:12px;color:var(--text-light);font-weight:normal">(点击餐厅打开地图)</span></div>
<div class="food-grid">
<div class="food-item" onclick="openMap('酸汤鱼','贵阳市云岩区')"><div class="emoji">🍜</div><div class="name">酸汤鱼</div><div class="restaurant">贵州招牌</div></div>
<div class="food-item" onclick="openMap('肠旺面','贵阳市南明区')"><div class="emoji">🍝</div><div class="name">肠旺面</div><div class="restaurant">贵阳人最爱</div></div>
<div class="food-item" onclick="openMap('辣子鸡','贵阳市云岩区')"><div class="emoji">🍗</div><div class="name">辣子鸡</div><div class="restaurant">超香下饭</div></div>
<div class="food-item" onclick="openMap('荔波烤鱼','黔南州荔波县古镇美食街')"><div class="emoji">🐟</div><div class="name">荔波烤鱼</div><div class="restaurant">古镇夜市</div></div>
</div>
<div class="food-daily">
<div class="food-daily-item"><div class="day">5/1中午</div><div class="meal"><span class="map-link" onclick="openMap('玉珍酸笋火锅','贵阳市云岩区喷水池')">玉珍酸笋火锅</span>（喷水池）</div></div>
<div class="food-daily-item"><div class="day">5/1晚上</div><div class="meal"><span class="map-link" onclick="openMap('菲姐小板凳斗米牛肉火锅','贵阳市观山湖区')">菲姐小板凳斗米牛肉火锅</span></div></div>
<div class="food-daily-item"><div class="day">5/2晚上</div><div class="meal"><span class="map-link" onclick="openMap('老刘鲜烤鸡','贵阳市云岩区黔灵东路')">老刘鲜烤鸡</span>（黔灵东路）</div></div>
<div class="food-daily-item"><div class="day">5/3晚上</div><div class="meal"><span class="map-link" onclick="openMap('荔波烤鱼','黔南州荔波县古镇美食街')">荔波烤鱼</span>（古镇）</div></div>
<div class="food-daily-item"><div class="day">5/4晚上</div><div class="meal"><span class="map-link" onclick="openMap('豆腐圆子','贵阳市南明区')">豆腐圆子</span>+烤串</div></div>
</div>
</div>
<div class="card">
<div class="card-title">📌 实用信息</div>
<div class="tips">
<li>携带雨具，贵州多阴雨</li>
<li>荔波小七孔08:00开门，建议早去</li>
<li>黔灵山公园有猴子，小心携带食物</li>
<li>贵州省博物馆周一闭馆（节假日除外）</li>
<li>甲秀楼傍晚看夜景最佳</li>
<li>花溪公园建议租单车骑行十里河滩</li>
</div>
</div>
</div>
<nav class="nav">
<a href="#overview"><span>📋</span>总览</a>
<a href="#day1"><span>📅</span>Day1</a>
<a href="#day2"><span>📅</span>Day2</a>
<a href="#day3"><span>📅</span>Day3</a>
<a href="#day4"><span>📅</span>Day4</a>
<a href="#day5"><span>📅</span>Day5</a>
</nav>
<div class="map-modal" id="mapModal">
<div class="map-modal-content">
<div class="map-modal-title" id="mapModalTitle">📍 甲秀楼</div>
<div class="map-option" onclick="openGaodeMap()">
<div class="name">🗺️ 高德地图</div>
<div class="app">推荐使用，导航精准</div>
</div>
<div class="map-option" onclick="openTencentMap()">
<div class="name">🗺️ 腾讯地图</div>
<div class="app">微信内使用方便</div>
</div>
<div class="map-option" onclick="openAppleMap()">
<div class="name">🍎 Apple地图</div>
<div class="app">iPhone自带</div>
</div>
<div class="map-option" onclick="openBaiduMap()">
<div class="name">🗺️ 百度地图</div>
<div class="app">中文搜索强</div>
</div>
<button class="map-close" onclick="closeMapModal()">关闭</button>
</div>
</div>
<script>
let currentLocation='';let currentAddress='';
function openMap(name,address){currentLocation=name;currentAddress=address;document.getElementById('mapModalTitle').textContent='📍 '+name;document.getElementById('mapModal').classList.add('active')}
function closeMapModal(){document.getElementById('mapModal').classList.remove('active')}
function getEncodedAddress(){return encodeURIComponent(currentAddress)}
function getEncodedName(){return encodeURIComponent(currentLocation)}
function openGaodeMap(){window.location.href='iosamap://navi?sourceName='+getEncodedName()+'&lat=&lng=&dev=1'}
function openTencentMap(){window.location.href='qqmap://map/routeplan?type=drive&to='+getEncodedName()+'&tocoord=&coord_type=gcj02'}
function openAppleMap(){window.location.href='http://maps.apple.com/?daddr='+getEncodedAddress()+'&dirflg=d'}
function openBaiduMap(){window.location.href='baidumap://map/direction?destination='+getEncodedAddress()}
function showTab(id){document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));document.querySelector('.tab[onclick="showTab(\''+id+'\')"]').classList.add('active');document.getElementById(id).classList.add('active')}
const observer=new IntersectionObserver((entries)=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')})},{threshold:0.1});document.querySelectorAll('.card').forEach(c=>observer.observe(c));
document.querySelectorAll('.nav a').forEach(a=>{a.addEventListener('click',function(e){e.preventDefault();const id=this.getAttribute('href').slice(1);const el=document.getElementById(id);if(el)el.scrollIntoView({behavior:'smooth',block:'start'})})});
document.getElementById('mapModal').addEventListener('click',function(e){if(e.target===this)closeMapModal()});
</script>
</body>
</html>
