---
layout: default
title: Market Price
nav_order: 11
---

{% assign material_price = site.data.material_price | reverse %}

# Market Price
{: .fs-9 }

Market Price.
{: .fs-6 .fw-300 }

---

{%- for price in material_price reversed limit:10 -%}
  {%- capture date %}{{date}}"{{price[nil] | date: "%m/%d"}}",{% endcapture -%}
  {%- capture item1 %}{{item1}}{{price["파괴석 결정"]}},{% endcapture -%}
  {%- capture item2 %}{{item2}}{{price["파괴강석"]}},{% endcapture -%}
  {%- capture item3 %}{{item3}}{{price["정제된 파괴강석"]}},{% endcapture -%}
  {%- capture item4 %}{{item4}}{{price["수호석 결정"]}},{% endcapture -%}
  {%- capture item5 %}{{item5}}{{price["수호강석"]}},{% endcapture -%}
  {%- capture item6 %}{{item6}}{{price["정제된 수호강석"]}},{% endcapture -%}
  {%- capture item7 %}{{item7}}{{price["명예의 돌파석"]}},{% endcapture -%}
  {%- capture item8 %}{{item8}}{{price["위대한 명예의 돌파석"]}},{% endcapture -%}
  {%- capture item9 %}{{item9}}{{price["경이로운 명예의 돌파석"]}},{% endcapture -%}
  {%- capture item10 %}{{item10}}{{price["찬란한 명예의 돌파석"]}},{% endcapture -%}
  {%- capture item11 %}{{item11}}{{price["하급 오레하 융화 재료"]}},{% endcapture -%}
  {%- capture item12 %}{{item12}}{{price["중급 오레하 융화 재료"]}},{% endcapture -%}
  {%- capture item13 %}{{item13}}{{price["상급 오레하 융화 재료"]}},{% endcapture -%}
  {%- capture item14 %}{{item14}}{{price["최상급 오레하 융화 재료"]}},{% endcapture -%}
  {%- capture item15 %}{{item15}}{{price["명예의 파편 주머니(소)"]}},{% endcapture -%}
  {%- capture item16 %}{{item16}}{{price["명예의 파편 주머니(중)"]}},{% endcapture -%}
  {%- capture item17 %}{{item17}}{{price["명예의 파편 주머니(대)"]}},{% endcapture -%}
  {%- capture item18 %}{{item18}}{{price["7멸"]}},{% endcapture -%}
  {%- capture item19 %}{{item19}}{{price["7홍"]}},{% endcapture -%}
  {%- capture item20 %}{{item20}}{{price["8멸"]}},{% endcapture -%}
  {%- capture item21 %}{{item21}}{{price["8홍"]}},{% endcapture -%}
  {%- capture item22 %}{{item22}}{{price["9멸"]}},{% endcapture -%}
  {%- capture item23 %}{{item23}}{{price["9홍"]}},{% endcapture -%}
  {%- capture item24 %}{{item24}}{{price["10멸"]}},{% endcapture -%}
  {%- capture item25 %}{{item25}}{{price["10홍"]}},{% endcapture -%}

{% endfor %}



## 정제된 파괴강석

<canvas id="item3" style="box-sizing: border-box; width: 100%;"></canvas>

## 정제된 수호강석

<canvas id="item6" style="box-sizing: border-box; width: 100%;"></canvas>

## 찬란한 명예의 돌파석

<canvas id="item10" style="box-sizing: border-box; width: 100%;"></canvas>

## 최상급 오레하 융화 재료

<canvas id="item14" style="box-sizing: border-box; width: 100%;"></canvas>

## 명예의 파편 주머니(대)

<canvas id="item17" style="box-sizing: border-box; width: 100%;"></canvas>

## 7멸

<canvas id="item18" style="box-sizing: border-box; width: 100%;"></canvas>

## 9멸

<canvas id="item22" style="box-sizing: border-box; width: 100%;"></canvas>

## 10멸

<canvas id="item24" style="box-sizing: border-box; width: 100%;"></canvas>

## 10홍

<canvas id="item25" style="box-sizing: border-box; width: 100%;"></canvas>


<script>
var options = {
    responsive: true,
    events: [], 
    plugins: {
      legend: false, 
      datalabels: {
        backgroundColor: function(context) {
          return context.dataset.backgroundColor;
        },
        align: 'end', 
        anchor: 'end', 
        borderRadius: 4,
        color: 'white', 
        font: {
          weight: 'bold'
        },
        padding: 6, 
      }
    },
    layout: {
      padding: {
        top: 32,
        right: 32,
        bottom: 16,
        left: 8
      }
    },
    aspectRatio: 4,
};

var ctx = document.getElementById("item3");

var chart_data = [{{item3}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item6");

var chart_data = [{{item6}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item10");

var chart_data = [{{item10}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item14");

var chart_data = [{{item14}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item17");

var chart_data = [{{item17}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item18");

var chart_data = [{{item18}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item22");

var chart_data = [{{item22}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item24");

var chart_data = [{{item24}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>
<script>
var ctx = document.getElementById("item25");

var chart_data = [{{item25}}];
var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: chart_data,
        backgroundColor: "rgba(0, 0, 128, 1)",
        borderColor: "rgba(0, 0, 128, 1)",
      }
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
  plugins:[ChartDataLabels],
});
</script>


