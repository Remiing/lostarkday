---
layout: default
title: 1%
parent: Refining
nav_order: 7
---

{% assign data = site.data.refining.refining_1 %}
{% assign try_num = data | map: 'try_num' %}
{% assign success_this_time = data | map: 'success_this_time' %}
{% assign cumulative = data | map: 'cumulative' %}

# 강화 확률 1%
{: .fs-9 }

22, 23 단계 도전
{: .fs-6 .fw-300 }

---

## N트만에 성공할 확률

<canvas id="success_this_time" style="box-sizing: border-box; width: 100%;"></canvas>

---

## N트안에 성공할 확률

<canvas id="cumulative" style="box-sizing: border-box; width: 100%;"></canvas>

---


<script>
var ctx = document.getElementById("success_this_time");

var chart_data = [{%- for i in success_this_time -%}{{i | times: 100 }},{% endfor%}];
var labels = [{{ try_num | join: "," }}];
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
    plugins: {
      legend: false, 
      tooltip: {
        enabled: false
      },
      datalabels: {
        formatter: function (value, context) {
            var idx = context.dataIndex;
            return value + '%';
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
var ctx = document.getElementById("cumulative");

var chart_data = [{%- for i in cumulative -%}{{i | times: 100 }},{% endfor%}];
var labels = [{{ try_num | join: "," }}];
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
    plugins: {
      legend: false, 
      tooltip: {
        enabled: false
      },
      datalabels: {
        formatter: function (value, context) {
            var idx = context.dataIndex;
            return value + '%';
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
