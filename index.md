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

총인원 80

<canvas id="representative_value" style="height:20vh"></canvas>

1600대 몇명, 1590대 몇명

<canvas id="variance"></canvas>

각 직업 인원수

|{{data.class_num.Berserker}}|{{data.class_num.Destroyer}}|{{data.class_num.Gunlancer}}|{{data.class_num.Paladin}}||
|{{data.class_num.Arcanist}}|{{data.class_num.Summoner}}|{{data.class_num.Bard}}|{{data.class_num.Sorceress}}||
|{{data.class_num.Wardancer}}|{{data.class_num.Scrapper}}|{{data.class_num.Soulfist}}|{{data.class_num.Glaivier}}|{{data.class_num.Striker}}|
|{{data.class_num.Deathblade}}|{{data.class_num.Shadowhunter}}|{{data.class_num.Reaper}}|||
|{{data.class_num.Sharpshooter}}|{{data.class_num.Deadeye}}|{{data.class_num.Artillerist}}|{{data.class_num.Machinist}}|{{data.class_num.Gunslinger}}|
|{{data.class_num.Artist}}|{{data.class_num.Aeromancer}}||||

직업군(전사, 무도가, 헌터, 마법사, 암살자, 스페셜리스트)

<canvas id="class_num"></canvas>

딜러, 서포터 수

<canvas id="position"></canvas>


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
          "rgba(54, 162, 235, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)"
        ],
        borderColor: [
          "rgba(54, 162, 235, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)"
        ],
        borderWidth: 0.5
      }
    ]
  };
var options = {
    indexAxis: 'y',
    responsive: true,
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




