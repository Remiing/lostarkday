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

---

## T3 1525 레벨 제한 아이템

{% assign price = site.data.refining.price.level_1525 %}
파괴석 개당 {{price.destruction_stone}}골드, 돌파석 개당 {{price.leap_stone}}골드, 명예의 파편 개당 {{price.honor_shard}}골드, 오레하 개당 {{price.fusion}}골드

| 강화단계 | 강화확률 | 트라이비용 | 평균기대값 |
| :-: | :-: | :-: | :-: |
{% for i in (10..25) -%}
{%- assign step = 'step_' | append: i -%}
{%- assign material = site.data.refining.material.level_1525[step] -%}
{%- case material.probability -%}
{%- when '15' %}{% assign avg = 4.9 -%}
{%- when '10' %}{% assign avg = 6.6 -%}
{%- when '5' %}{% assign avg = 11.4 -%}
{%- when '4' %}{% assign avg = 13.7 -%}
{%- when '3' %}{% assign avg = 17.5 -%}
{%- when '1.5' %}{% assign avg = 32.4 -%}
{%- when '1' %}{% assign avg = 47.2 -%}
{%- when '0.5' %}{% assign avg = 91.3 -%}
{%- endcase -%}
{%- assign destruction_stone = material.destruction_stone | times: price.destruction_stone -%}
{%- assign fusion = material.fusion | times: price.fusion -%}
{%- assign honor_shard = material.honor_shard | times: price.honor_shard -%}
{%- assign leap_stone = material.leap_stone | times: price.leap_stone -%}
{%- assign refining_once = destruction_stone| plus: fusion | plus: honor_shard | plus: leap_stone | plus: material.gold | round -%}
{%- assign refining_total = refining_once | times: avg | round -%}
{%- capture level_1525_label %}{{level_1525_label}}{{i}},{% endcapture -%}
{%- capture level_1525_data %}{{level_1525_data}}{{refining_total}},{% endcapture -%}
| {{i}} | {{material.probability}}% | {{refining_once}}골드 | {{refining_total}}골드 |
{% endfor %}

<canvas id="weapon_level_1525" style="box-sizing: border-box; width: 100%;"></canvas>

---

## T3 1390 레벨 제한 아이템

{% assign price = site.data.refining.price.level_1390 %}
파괴석 개당 {{price.destruction_stone}}골드, 돌파석 개당 {{price.leap_stone}}골드, 명예의 파편 개당 {{price.honor_shard}}골드, 오레하 개당 {{price.fusion}}골드

| 강화단계 | 강화확률 | 트라이비용 | 평균기대값 |
| :-: | :-: | :-: | :-: |
{% for i in (10..25) -%}
{%- assign step = 'step_' | append: i -%}
{%- assign material = site.data.refining.material.level_1390[step] -%}
{%- case material.probability -%}
{%- when '15' %}{% assign avg = 4.9 -%}
{%- when '10' %}{% assign avg = 6.6 -%}
{%- when '5' %}{% assign avg = 11.4 -%}
{%- when '4' %}{% assign avg = 13.7 -%}
{%- when '3' %}{% assign avg = 17.5 -%}
{%- when '1.5' %}{% assign avg = 32.4 -%}
{%- when '1' %}{% assign avg = 47.2 -%}
{%- when '0.5' %}{% assign avg = 91.3 -%}
{%- endcase -%}
{%- assign destruction_stone = material.destruction_stone | times: price.destruction_stone -%}
{%- assign fusion = material.fusion | times: price.fusion -%}
{%- assign honor_shard = material.honor_shard | times: price.honor_shard -%}
{%- assign leap_stone = material.leap_stone | times: price.leap_stone -%}
{%- assign refining_once = destruction_stone| plus: fusion | plus: honor_shard | plus: leap_stone | plus: material.gold | round -%}
{%- assign refining_total = refining_once | times: avg | round -%}
{%- capture level_1390_label %}{{level_1390_label}}{{i}},{% endcapture -%}
{%- capture level_1390_data %}{{level_1390_data}}{{refining_total}},{% endcapture -%}
| {{i}} | {{material.probability}}% | {{refining_once}}골드 | {{refining_total}}골드 |
{% endfor %}

<canvas id="weapon_level_1390" style="box-sizing: border-box; width: 100%;"></canvas>

---

## T3 1340 레벨 제한 아이템

{% assign price = site.data.refining.price.level_1340 %}
파괴석 개당 {{price.destruction_stone}}골드, 돌파석 개당 {{price.leap_stone}}골드, 명예의 파편 개당 {{price.honor_shard}}골드, 오레하 개당 {{price.fusion}}골드

| 강화단계 | 강화확률 | 트라이비용 | 평균기대값 |
| :-: | :-: | :-: | :-: |
{% for i in (12..25) -%}
{%- assign step = 'step_' | append: i -%}
{%- assign material = site.data.refining.material.level_1340[step] -%}
{%- case material.probability -%}
{%- when '15' %}{% assign avg = 4.9 -%}
{%- when '10' %}{% assign avg = 6.6 -%}
{%- when '5' %}{% assign avg = 11.4 -%}
{%- when '4' %}{% assign avg = 13.7 -%}
{%- when '3' %}{% assign avg = 17.5 -%}
{%- when '1.5' %}{% assign avg = 32.4 -%}
{%- when '1' %}{% assign avg = 47.2 -%}
{%- when '0.5' %}{% assign avg = 91.3 -%}
{%- endcase -%}
{%- assign destruction_stone = material.destruction_stone | times: price.destruction_stone -%}
{%- assign fusion = material.fusion | times: price.fusion -%}
{%- assign honor_shard = material.honor_shard | times: price.honor_shard -%}
{%- assign leap_stone = material.leap_stone | times: price.leap_stone -%}
{%- assign refining_once = destruction_stone| plus: fusion | plus: honor_shard | plus: leap_stone | plus: material.gold | round -%}
{%- assign refining_total = refining_once | times: avg | round -%}
{%- capture level_1340_label %}{{level_1340_label}}{{i}},{% endcapture -%}
{%- capture level_1340_data %}{{level_1340_data}}{{refining_total}},{% endcapture -%}
| {{i}} | {{material.probability}}% | {{refining_once}}골드 | {{refining_total}}골드 |
{% endfor %}

<canvas id="weapon_level_1340" style="box-sizing: border-box; width: 100%;"></canvas>

---

## T3 1302 레벨 제한 아이템

{% assign price = site.data.refining.price.level_1302 %}
파괴석 개당 {{price.destruction_stone}}골드, 돌파석 개당 {{price.leap_stone}}골드, 명예의 파편 개당 {{price.honor_shard}}골드, 오레하 개당 {{price.fusion}}골드

| 강화단계 | 강화확률 | 트라이비용 | 평균기대값 |
| :-: | :-: | :-: | :-: |
{% for i in (16..25) -%}
{%- assign step = 'step_' | append: i -%}
{%- assign material = site.data.refining.material.level_1302[step] -%}
{%- case material.probability -%}
{%- when '15' %}{% assign avg = 4.9 -%}
{%- when '10' %}{% assign avg = 6.6 -%}
{%- when '5' %}{% assign avg = 11.4 -%}
{%- when '4' %}{% assign avg = 13.7 -%}
{%- when '3' %}{% assign avg = 17.5 -%}
{%- when '1.5' %}{% assign avg = 32.4 -%}
{%- when '1' %}{% assign avg = 47.2 -%}
{%- when '0.5' %}{% assign avg = 91.3 -%}
{%- endcase -%}
{%- assign destruction_stone = material.destruction_stone | times: price.destruction_stone -%}
{%- assign fusion = material.fusion | times: price.fusion -%}
{%- assign honor_shard = material.honor_shard | times: price.honor_shard -%}
{%- assign leap_stone = material.leap_stone | times: price.leap_stone -%}
{%- assign refining_once = destruction_stone| plus: fusion | plus: honor_shard | plus: leap_stone | plus: material.gold | round -%}
{%- assign refining_total = refining_once | times: avg | round -%}
{%- capture level_1302_label %}{{level_1302_label}}{{i}},{% endcapture -%}
{%- capture level_1302_data %}{{level_1302_data}}{{refining_total}},{% endcapture -%}
| {{i}} | {{material.probability}}% | {{refining_once}}골드 | {{refining_total}}골드 |
{% endfor %}

<canvas id="weapon_level_1302" style="box-sizing: border-box; width: 100%;"></canvas>

---

<script>
var ctx = document.getElementById("weapon_level_1525");

var chart_data = [{{ level_1525_data }}];
var labels = [{{ level_1525_label }}];
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

var chart_data = [{{ level_1390_data }}];
var labels = [{{ level_1390_label }}];
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

var chart_data = [{{ level_1340_data }}];
var labels = [{{ level_1340_label }}];
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

var chart_data = [{{ level_1302_data }}];
var labels = [{{ level_1302_label }}];
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
