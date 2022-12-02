---
layout: default
title: Probability
parent: Refining
nav_order: 1
---

# Probability
{: .fs-9 }

강화 확률에 따른 데이터
{: .fs-5 .fw-300 }

---

## 강화 확률 15%

- [ ] T3 1302 레벨 제한 아이템 12, 13, 14
- [ ] T3 1340 레벨 제한 아이템 12, 13, 14
- [ ] T3 1390 레벨 제한 아이템 
- [ ] T3 1525 레벨 제한 아이템 10, 11

---

{%- assign data = site.data.refining.refining_15 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_15_num %}{{pb_15_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_15_stt %}{{pb_15_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_15_cum %}{{pb_15_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_15_success_this_time" style="box-sizing: border-box; width: 100%;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_15_cumulative" style="box-sizing: border-box; width: 100%;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 10%

- [ ] T3 1302 레벨 제한 아이템 15
- [ ] T3 1340 레벨 제한 아이템 15, 16, 17
- [ ] T3 1390 레벨 제한 아이템 12, 13
- [ ] T3 1525 레벨 제한 아이템 12, 13

---

{%- assign data = site.data.refining.refining_10 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_10_num %}{{pb_10_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_10_stt %}{{pb_10_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_10_cum %}{{pb_10_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_10_success_this_time" style="box-sizing: border-box; width: 100%;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_10_cumulative" style="box-sizing: border-box; width: 100%;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 5%

- [ ] T3 1302 레벨 제한 아이템 
- [ ] T3 1340 레벨 제한 아이템 18, 19
- [ ] T3 1390 레벨 제한 아이템 14, 15
- [ ] T3 1525 레벨 제한 아이템 14, 15

---

{%- assign data = site.data.refining.refining_5 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_5_num %}{{pb_5_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_5_stt %}{{pb_5_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_5_cum %}{{pb_5_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_5_success_this_time" style="box-sizing: border-box; width: 100%;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_5_cumulative" style="box-sizing: border-box; width: 100%;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 4%

- [ ] T3 1302 레벨 제한 아이템 12, 13, 14
- [ ] T3 1340 레벨 제한 아이템 
- [ ] T3 1390 레벨 제한 아이템 16, 17
- [ ] T3 1525 레벨 제한 아이템 16, 17

---

{%- assign data = site.data.refining.refining_4 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_4_num %}{{pb_4_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_4_stt %}{{pb_4_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_4_cum %}{{pb_4_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_4_success_this_time" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_4_cumulative" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 3%

- [ ] T3 1302 레벨 제한 아이템 
- [ ] T3 1340 레벨 제한 아이템 20, 21
- [ ] T3 1390 레벨 제한 아이템 18, 19
- [ ] T3 1525 레벨 제한 아이템 18, 19

---

{%- assign data = site.data.refining.refining_3 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_3_num %}{{pb_3_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_3_stt %}{{pb_3_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_3_cum %}{{pb_3_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_3_success_this_time" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_3_cumulative" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 1.5%

- [ ] T3 1302 레벨 제한 아이템 
- [ ] T3 1340 레벨 제한 아이템 
- [ ] T3 1390 레벨 제한 아이템 20, 21
- [ ] T3 1525 레벨 제한 아이템 20, 21

---

{%- assign data = site.data.refining.refining_1_5 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_1_5_num %}{{pb_1_5_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_1_5_stt %}{{pb_1_5_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_1_5_cum %}{{pb_1_5_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_1_5_success_this_time" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_1_5_cumulative" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 1%

- [ ] T3 1302 레벨 제한 아이템 
- [ ] T3 1340 레벨 제한 아이템 22, 23
- [ ] T3 1390 레벨 제한 아이템 22, 23
- [ ] T3 1525 레벨 제한 아이템 22, 23

---

{%- assign data = site.data.refining.refining_1 -%}
{%- assign try_num = data | map: 'try_num' -%}
{%- assign success_this_time = data | map: 'success_this_time' -%}
{%- assign cumulative = data | map: 'cumulative' -%}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_1_num %}{{pb_1_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_1_stt %}{{pb_1_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_1_cum %}{{pb_1_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg | round: 1}} 번

---

### N트만에 성공할 확률

<canvas id="pb_1_success_this_time" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_1_cumulative" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---

## 강화 확률 0.5%

- [ ] T3 1302 레벨 제한 아이템 
- [ ] T3 1340 레벨 제한 아이템 24, 25
- [ ] T3 1390 레벨 제한 아이템 24, 25
- [ ] T3 1525 레벨 제한 아이템 24, 25

---

{% assign data = site.data.refining.refining_0_5 %}
{% assign try_num = data | map: 'try_num' %}
{% assign success_this_time = data | map: 'success_this_time' %}
{% assign cumulative = data | map: 'cumulative' %}

{%- assign avg = 0 -%}
{%- assign index = try_num.size | minus: 1 -%}
{%- for i in (0..index) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg -%}
{%- capture pb_0_5_num %}{{pb_0_5_num}}{{i | plus: 1}},{% endcapture -%}
{%- capture pb_0_5_stt %}{{pb_0_5_stt}}{{success_this_time[i] | times: 100}},{% endcapture -%}
{%- capture pb_0_5_cum %}{{pb_0_5_cum}}{{cumulative[i] | times: 100}},{% endcapture -%}
{% endfor %}

### 평균적으로 누르는 횟수 {{avg}} 번

---

### N트만에 성공할 확률

<canvas id="pb_0_5_success_this_time" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### N트안에 성공할 확률

<canvas id="pb_0_5_cumulative" style="box-sizing: border-box; width: 100%; height: 100vh;"></canvas>

---

### 트라이 회차에 따른 확률 데이터

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in data -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

---


<script>
var ctx = document.getElementById("pb_15_success_this_time");

var chart_data = [{{ pb_15_stt }}];
var labels = [{{ pb_15_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_15_cumulative");

var chart_data = [{{ pb_15_cum }}];
var labels = [{{ pb_15_num }}];
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
var ctx = document.getElementById("pb_10_success_this_time");

var chart_data = [{{ pb_10_stt }}];
var labels = [{{ pb_10_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_10_cumulative");

var chart_data = [{{ pb_10_cum }}];
var labels = [{{ pb_10_num }}];
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
var ctx = document.getElementById("pb_5_success_this_time");

var chart_data = [{{ pb_5_stt }}];
var labels = [{{ pb_5_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_5_cumulative");

var chart_data = [{{ pb_5_cum }}];
var labels = [{{ pb_5_num }}];
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
var ctx = document.getElementById("pb_4_success_this_time");

var chart_data = [{{ pb_4_stt }}];
var labels = [{{ pb_4_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_4_cumulative");

var chart_data = [{{ pb_4_cum }}];
var labels = [{{ pb_4_num }}];
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
var ctx = document.getElementById("pb_3_success_this_time");

var chart_data = [{{ pb_3_stt }}];
var labels = [{{ pb_3_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_3_cumulative");

var chart_data = [{{ pb_3_cum }}];
var labels = [{{ pb_3_num }}];
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
var ctx = document.getElementById("pb_1_5_success_this_time");

var chart_data = [{{ pb_1_5_stt }}];
var labels = [{{ pb_1_5_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_1_5_cumulative");

var chart_data = [{{ pb_1_5_cum }}];
var labels = [{{ pb_1_5_num }}];
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
var ctx = document.getElementById("pb_1_success_this_time");

var chart_data = [{{ pb_1_stt }}];
var labels = [{{ pb_1_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_1_cumulative");

var chart_data = [{{ pb_1_cum }}];
var labels = [{{ pb_1_num }}];
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
var ctx = document.getElementById("pb_0_5_success_this_time");

var chart_data = [{{ pb_0_5_stt }}];
var labels = [{{ pb_0_5_num }}];
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
    events: [], 
    animations: {
        duration: 0
    }, 
    plugins: {
      legend: false, 
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
var ctx = document.getElementById("pb_0_5_cumulative");

var chart_data = [{{ pb_0_5_cum }}];
var labels = [{{ pb_0_5_num }}];
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
