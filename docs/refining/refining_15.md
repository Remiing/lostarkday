---
layout: default
title: 15%
parent: Refining
nav_order: 1
---

{% assign data = site.data.refining.refining_15 %}
{% assign try_num = data | map: 'try_num' %}
{% assign success_this_time = data | map: 'success_this_time' %}
{% assign cumulative = data | map: 'cumulative' %}

# 강화 확률 15%
{: .fs-9 }

- [ ] T3 1302 레벨 제한 아이템 12, 13, 14
- [ ] T3 1340 레벨 제한 아이템 12, 13, 14
- [ ] T3 1390 레벨 제한 아이템 
- [ ] T3 1525 레벨 제한 아이템 10, 11
{: .fs-5 .fw-300 }

---

{% assign avg = 0 -%}
{%- for i in (i..try_num.size) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- endfor -%}

## 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

## N트만에 성공할 확률

<canvas id="success_this_time" style="box-sizing: border-box; width: 100%;"></canvas>

---

## N트안에 성공할 확률

<canvas id="cumulative" style="box-sizing: border-box; width: 100%;"></canvas>

---

## 트라이 회차에 따른 확률 데이터
기본 재련 확률 15%

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in site.data.refining.refining_15 -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

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
