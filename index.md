---
layout: default
title: Home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

{% assign data = site.data.total_info %}

# Day
{: .fs-9 }

Day guild information.
{: .fs-6 .fw-300 }

---

## 최고 평균 최저 레벨

<canvas id="representative_value" style="width: 100vh; height:20vh"></canvas>

---

## 레벨대 분포

<canvas id="variance"></canvas>

---

## 직업별 인원수

|![](./assets/images/class_images/emblem_berserker.png){{data.class_num.Berserker-}}
|![](./assets/images/class_images/emblem_destroyer.png){{data.class_num.Destroyer-}}
|![](./assets/images/class_images/emblem_warlord.png){{data.class_num.Gunlancer-}}
|![](./assets/images/class_images/emblem_holyknight.png){{data.class_num.Paladin-}}||
|![](./assets/images/class_images/emblem_arcana.png){{data.class_num.Arcanist-}}
|![](./assets/images/class_images/emblem_summoner.png){{data.class_num.Summoner-}}
|![](./assets/images/class_images/emblem_bard.png){{data.class_num.Bard-}}
|![](./assets/images/class_images/emblem_elemental_master.png){{data.class_num.Sorceress-}}||
|![](./assets/images/class_images/emblem_battle_master.png){{data.class_num.Wardancer-}}
|![](./assets/images/class_images/emblem_infighter.png){{data.class_num.Scrapper-}}
|![](./assets/images/class_images/emblem_force_master.png){{data.class_num.Soulfist-}}
|![](./assets/images/class_images/emblem_lance_master.png){{data.class_num.Glaivier-}}
|![](./assets/images/class_images/emblem_battle_master_male.png){{data.class_num.Striker-}}|
|![](./assets/images/class_images/emblem_blade.png){{data.class_num.Deathblade-}}
|![](./assets/images/class_images/emblem_demonic.png){{data.class_num.Shadowhunter-}}
|![](./assets/images/class_images/emblem_reaper.png){{data.class_num.Reaper-}}|||
|![](./assets/images/class_images/emblem_hawk_eye.png){{data.class_num.Sharpshooter-}}
|![](./assets/images/class_images/emblem_devil_hunter.png){{data.class_num.Deadeye-}}
|![](./assets/images/class_images/emblem_blaster.png){{data.class_num.Artillerist-}}
|![](./assets/images/class_images/emblem_scouter.png){{data.class_num.Machinist-}}
|![](./assets/images/class_images/emblem_devil_hunter_female.png){{data.class_num.Gunslinger-}}|
|![](./assets/images/class_images/emblem_yinyangshi.png){{data.class_num.Artist-}}
|![](./assets/images/class_images/emblem_weather_artist.png){{data.class_num.Aeromancer-}}||||
{: .class_table .text-grey-lt-000 .text-center}

---

## 직업군 인원수

<canvas id="class_num"></canvas>

---

## 포지션 인원수

<canvas id="position" style="width: 100vh; height:20vh"></canvas>

---


<script>
var ctx = document.getElementById("representative_value");

var chart_data = [{{data.representative_value.highest_level}}, {{data.representative_value.average_level}}, {{data.representative_value.lowest_level}}];
var labels = ["High", "Avg", "Low"];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: [
          "rgba(138, 43, 226, 0.2)",
          "rgba(240, 169, 87, 0.2)",
          "rgba(0, 0, 128, 0.2)",
          "rgba(128, 0, 128, 0.2)",
          "rgba(70, 126, 198, 0.2)",
          "rgba(133, 172, 32, 0.2)"
        ],
        borderColor: [
          "rgba(138, 43, 226, 1)",
          "rgba(240, 169, 87, 1)",
          "rgba(0, 0, 128, 1)",
          "rgba(128, 0, 128, 1)",
          "rgba(70, 126, 198, 1)",
          "rgba(133, 172, 32, 1)"
        ],
        borderWidth: 1
      }
    ]
  };
var options = {
    indexAxis: 'y',
    responsive: false,
    events: ['mousemove'], 
    animations: {
        duration: 0
    }, 
    scales: {
        x: {
            min: 1400, 
            max: 1655
        }
    },
    plugins: {
      legend: false, 
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options
});
</script>
<script>
var ctx = document.getElementById("variance");

var chart_data = [{{data.variance.above_1620}},{{data.variance.above_1610}},{{data.variance.above_1600}},{{data.variance.above_1590}},{{data.variance.above_1580}},{{data.variance.above_1570}},{{data.variance.above_1560}},{{data.variance.above_1550}},{{data.variance.above_1540}},{{data.variance.above_1530}},{{data.variance.above_1520}},{{data.variance.above_1510}},{{data.variance.above_1500}},{{data.variance.above_1490}},{{data.variance.under_1490}}];
var labels = ["1620~", "1610~", "1600~", "1590~", "1580~", "1570~", "1560~", "1550~", "1540~", "1530~", "1520~", "1510~", "1500~", "1490~", "0~"];
var data = {
    labels: labels,
    datasets: [{
        label: 'variance',
        data: chart_data,
        backgroundColor: [
          "rgba(138, 43, 226, 0.2)",
          "rgba(240, 169, 87, 0.2)",
          "rgba(0, 0, 128, 0.2)",
          "rgba(128, 0, 128, 0.2)",
          "rgba(70, 126, 198, 0.2)",
          "rgba(133, 172, 32, 0.2)"
        ],
        borderColor: [
          "rgba(138, 43, 226, 1)",
          "rgba(240, 169, 87, 1)",
          "rgba(0, 0, 128, 1)",
          "rgba(128, 0, 128, 1)",
          "rgba(70, 126, 198, 1)",
          "rgba(133, 172, 32, 1)"
        ],
        borderWidth: 1
      }
    ]
  };
var options = {
    indexAxis: 'x',
    responsive: true,
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options
});
</script>
<script>
var ctx = document.getElementById("class_num");

var chart_data = [{{data.class_num.Berserker| plus: data.class_num.Destroyer| plus: data.class_num.Gunlancer| plus: data.class_num.Paladin}}, {{data.class_num.Arcanist| plus: data.class_num.Summoner| plus: data.class_num.Bard| plus: data.class_num.Sorceress}}, {{data.class_num.Wardancer| plus: data.class_num.Scrapper| plus: data.class_num.Soulfist| plus: data.class_num.Glaivier| plus: data.class_num.Striker}}, {{data.class_num.Deathblade| plus: data.class_num.Shadowhunter| plus: data.class_num.Reaper}}, {{data.class_num.Sharpshooter| plus: data.class_num.Deadeye| plus: data.class_num.Artillerist| plus: data.class_num.Machinist| plus: data.class_num.Gunslinger}}, {{data.class_num.Artist| plus: data.class_num.Aeromancer}}];
var labels = ["전사", "마법사", "무도가", "암살자", "헌터", "스페셜리스트"];
var data = {
    labels: labels,
    datasets: [{
        label: 'class_num',
        data: chart_data,
        backgroundColor: [
          "rgba(138, 43, 226, 0.2)",
          "rgba(240, 169, 87, 0.2)",
          "rgba(0, 0, 128, 0.2)",
          "rgba(128, 0, 128, 0.2)",
          "rgba(70, 126, 198, 0.2)",
          "rgba(133, 172, 32, 0.2)"
        ],
        borderColor: [
          "rgba(138, 43, 226, 1)",
          "rgba(240, 169, 87, 1)",
          "rgba(0, 0, 128, 1)",
          "rgba(128, 0, 128, 1)",
          "rgba(70, 126, 198, 1)",
          "rgba(133, 172, 32, 1)"
        ],
        borderWidth: 1
      }
    ]
  };
var options = {
    indexAxis: 'y',
    responsive: true,
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options
});
</script>
<script>
var ctx = document.getElementById("position");

var chart_data = [{{data.class_num.Berserker| plus: data.class_num.Destroyer| plus: data.class_num.Gunlancer| plus: data.class_num.Arcanist| plus: data.class_num.Summoner| plus: data.class_num.Sorceress| plus: data.class_num.Wardancer| plus: data.class_num.Scrapper| plus: data.class_num.Soulfist| plus: data.class_num.Glaivier| plus: data.class_num.Striker| plus: data.class_num.Deathblade| plus: data.class_num.Shadowhunter| plus: data.class_num.Reaper| plus: data.class_num.Sharpshooter| plus: data.class_num.Deadeye| plus: data.class_num.Artillerist| plus: data.class_num.Machinist| plus: data.class_num.Gunslinger| plus: data.class_num.Artist| plus: data.class_num.Aeromancer}}, {{data.class_num.Bard| plus: data.class_num.Paladin}}];
var labels = ["딜러", "서포터"];
var data = {
    labels: labels,
    datasets: [{
        label: 'position',
        data: chart_data,
        backgroundColor: [
          "rgba(138, 43, 226, 0.2)",
          "rgba(240, 169, 87, 0.2)",
          "rgba(0, 0, 128, 0.2)",
          "rgba(128, 0, 128, 0.2)",
          "rgba(70, 126, 198, 0.2)",
          "rgba(133, 172, 32, 0.2)"
        ],
        borderColor: [
          "rgba(138, 43, 226, 1)",
          "rgba(240, 169, 87, 1)",
          "rgba(0, 0, 128, 1)",
          "rgba(128, 0, 128, 1)",
          "rgba(70, 126, 198, 1)",
          "rgba(133, 172, 32, 1)"
        ],
        borderWidth: 1
      }
    ]
  };
var options = {
    indexAxis: 'y',
    responsive: false,
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options
});
</script>




