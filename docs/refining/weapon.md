---
layout: default
title: Weapon
parent: Refining
nav_order: 2
---

# Weapon
{: .fs-9 .no_toc }

무기 강화 기대값
{: .fs-5 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

{% assign price = site.data.material_price %}

---

## T3 1525 레벨 제한 아이템

- 파괴석 개당 {{price | where:"itemName", "정제된 파괴강석" | map: 'itemPrice'}}골드
- 돌파석 개당 {{price | where:"itemName", "찬란한 명예의 돌파석" | map: 'itemPrice'}}골드
- 오레하 개당 {{price | where:"itemName", "최상급 오레하 융화 재료" | map: 'itemPrice'}}골드

| 강화단계 | 트라이비용 | 평균기대값 | 최대값 |
| :-: | :-: | :-: | :-: |
{% for step in site.data.step_price -%}
  {%- if step.level != 'level_1525' -%}
    {%- continue -%}
  {%- endif -%}
  {%- assign step_num = step.step | remove:'step_' | abs -%}
  {%- if step_num < 10 -%}
    {%- continue -%}
  {%- endif -%}
  {%- capture lv1525_step %}{{lv1525_step}}{{step_num}},{% endcapture -%}
  {%- capture lv1525_Avg %}{{lv1525_Avg}}{{step.weaponAvg}},{% endcapture -%}
  {%- capture lv1525_Max %}{{lv1525_Max}}{{step.weaponMax}},{% endcapture -%}
  | {{step_num}} | {{step.weaponOnce}}골드 | {{step.weaponAvg}}골드 | {{step.weaponMax}}골드 |
{% endfor %}

<canvas id="weapon_level_1525" style="box-sizing: border-box; width: 100%;"></canvas>

---

## T3 1390 레벨 제한 아이템

- 파괴석 개당 {{price | where:"itemName", "파괴강석" | map: 'itemPrice'}}골드
- 돌파석 개당 {{price | where:"itemName", "경이로운 명예의 돌파석" | map: 'itemPrice'}}골드
- 오레하 개당 {{price | where:"itemName", "상급 오레하 융화 재료" | map: 'itemPrice'}}골드

| 강화단계 | 트라이비용 | 평균기대값 | 최대값 |
| :-: | :-: | :-: | :-: |
{% for step in site.data.step_price -%}
  {%- if step.level != 'level_1390' -%}
    {%- continue -%}
  {%- endif -%}
  {%- assign step_num = step.step | remove:'step_' | abs -%}
  {%- if step_num < 10 -%}
    {%- continue -%}
  {%- endif -%}
  {%- capture lv1390_step %}{{lv1390_step}}{{step_num}},{% endcapture -%}
  {%- capture lv1390_Avg %}{{lv1390_Avg}}{{step.weaponAvg}},{% endcapture -%}
  {%- capture lv1390_Max %}{{lv1390_Max}}{{step.weaponMax}},{% endcapture -%}
  | {{step_num}} | {{step.weaponOnce}}골드 | {{step.weaponAvg}}골드 | {{step.weaponMax}}골드 |
{% endfor %}

<canvas id="weapon_level_1390" style="box-sizing: border-box; width: 100%;"></canvas>

---

## T3 1340 레벨 제한 아이템

- 파괴석 개당 {{price | where:"itemName", "파괴석 결정" | map: 'itemPrice'}}골드
- 돌파석 개당 {{price | where:"itemName", "위대한 명예의 돌파석" | map: 'itemPrice'}}골드
- 오레하 개당 {{price | where:"itemName", "중급 오레하 융화 재료" | map: 'itemPrice'}}골드

| 강화단계 | 트라이비용 | 평균기대값 | 최대값 |
| :-: | :-: | :-: | :-: |
{% for step in site.data.step_price -%}
  {%- if step.level != 'level_1340' -%}
    {%- continue -%}
  {%- endif -%}
  {%- assign step_num = step.step | remove:'step_' | abs -%}
  {%- if step_num < 10 -%}
    {%- continue -%}
  {%- endif -%}
  {%- capture lv1340_step %}{{lv1340_step}}{{step_num}},{% endcapture -%}
  {%- capture lv1340_Avg %}{{lv1340_Avg}}{{step.weaponAvg}},{% endcapture -%}
  {%- capture lv1340_Max %}{{lv1340_Max}}{{step.weaponMax}},{% endcapture -%}
  | {{step_num}} | {{step.weaponOnce}}골드 | {{step.weaponAvg}}골드 | {{step.weaponMax}}골드 |
{% endfor %}

<canvas id="weapon_level_1340" style="box-sizing: border-box; width: 100%;"></canvas>

---

## T3 1302 레벨 제한 아이템

- 파괴석 개당 {{price | where:"itemName", "파괴석 결정" | map: 'itemPrice'}}골드
- 돌파석 개당 {{price | where:"itemName", "명예의 돌파석" | map: 'itemPrice'}}골드
- 오레하 개당 {{price | where:"itemName", "하급 오레하 융화 재료" | map: 'itemPrice'}}골드

| 강화단계 | 트라이비용 | 평균기대값 | 최대값 |
| :-: | :-: | :-: | :-: |
{% for step in site.data.step_price -%}
  {%- if step.level != 'level_1302' -%}
    {%- continue -%}
  {%- endif -%}
  {%- assign step_num = step.step | remove:'step_' | abs -%}
  {%- if step_num < 10 -%}
    {%- continue -%}
  {%- endif -%}
  {%- capture lv1302_step %}{{lv1302_step}}{{step_num}},{% endcapture -%}
  {%- capture lv1302_Avg %}{{lv1302_Avg}}{{step.weaponAvg}},{% endcapture -%}
  {%- capture lv1302_Max %}{{lv1302_Max}}{{step.weaponMax}},{% endcapture -%}
  | {{step_num}} | {{step.weaponOnce}}골드 | {{step.weaponAvg}}골드 | {{step.weaponMax}}골드 |
{% endfor %}

<canvas id="weapon_level_1302" style="box-sizing: border-box; width: 100%;"></canvas>

---

<script>
var ctx = document.getElementById("weapon_level_1525");

var chart_data = [{{ lv1525_Avg }}];
var labels = [{{ lv1525_step }}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: [
          "rgba(0, 0, 128, 0.2)",
        ],
        borderColor: [
          "rgba(0, 0, 128, 1)",
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
    plugins: {
      legend: false, 
      tooltip: {
        enabled: false
      },
      datalabels: {
        align: 'end', 
        anchor: 'end', 
        color: 'black',
        font: {
          weight: 'bold'
        },
        padding: {
          right: 10, 
        },
        formatter: function (value, context) {
            var idx = context.dataIndex;
            return value;
          },
      }
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("weapon_level_1390");

var chart_data = [{{ lv1390_Avg }}];
var labels = [{{ lv1390_step }}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: [
          "rgba(0, 0, 128, 0.2)",
        ],
        borderColor: [
          "rgba(0, 0, 128, 1)",
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
    plugins: {
      legend: false, 
      tooltip: {
        enabled: false
      },
      datalabels: {
        align: 'end', 
        anchor: 'end', 
        color: 'black',
        font: {
          weight: 'bold'
        },
        padding: {
          right: 10, 
        },
        formatter: function (value, context) {
            var idx = context.dataIndex;
            return value;
          },
      }
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("weapon_level_1340");

var chart_data = [{{ lv1340_Avg }}];
var labels = [{{ lv1340_step }}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: [
          "rgba(0, 0, 128, 0.2)",
        ],
        borderColor: [
          "rgba(0, 0, 128, 1)",
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
    plugins: {
      legend: false, 
      tooltip: {
        enabled: false
      },
      datalabels: {
        align: 'end', 
        anchor: 'end', 
        color: 'black',
        font: {
          weight: 'bold'
        },
        padding: {
          right: 10, 
        },
        formatter: function (value, context) {
            var idx = context.dataIndex;
            return value;
          },
      }
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("weapon_level_1302");

var chart_data = [{{ lv1302_Avg }}];
var labels = [{{ lv1302_step }}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: [
          "rgba(0, 0, 128, 0.2)",
        ],
        borderColor: [
          "rgba(0, 0, 128, 1)",
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
    plugins: {
      legend: false, 
      tooltip: {
        enabled: false
      },
      datalabels: {
        align: 'end', 
        anchor: 'end', 
        color: 'black',
        font: {
          weight: 'bold'
        },
        padding: {
          right: 10, 
        },
        formatter: function (value, context) {
            var idx = context.dataIndex;
            return value;
          },
      }
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
