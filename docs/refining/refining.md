---
layout: default
title: Refining
nav_order: 4
has_children: true
permalink: /docs/refining
---

# Refining
{: .fs-9 }

장비 강화에 대한 모든 것
{: .fs-6 .fw-300 }

---

## 강화 확률에 따른 평균 트라이 횟수
보조 재료(은총, 축복, 가호, 야금술, 단조술 등)는 사용하지 않고 계산

{% assign data = site.data.refining.refining_15 %}
{% assign try_num = data | map: 'try_num' %}
{% assign success_this_time = data | map: 'success_this_time' %}
{% assign avg = 0 -%}
{%- for i in (i..try_num.size) -%}
{%- assign avg = try_num[i] | times: success_this_time[i] | plus: avg | round: 1 -%}
{%- endfor -%}

| 강화확률 | 평균 트라이 횟수 | 장기백 | 장기백 비율 |
| :-: | :-: | :-: | :-: |
| 15% | 4.9번 | 11트 | 8.5% |
| 10% | 6.6번 | 15트 | 8.5% |
| 5% | 11.4번 | 26트 | 9.7% |
| 4% | 13.7번 | 31트 | 10.4% |
| 3% | 17.5번 | 40트 | 10.7% |
| 1.5% | 32.4번 | 76트 | 11.1% |
| 1% | 47.2번 | 112트 | 11.2% |
| 0.5% | 91.3번 | 219트 | 11.5% |

---

## 무기 강화 기대값
T3 1525 레벨 제한 아이템

{% assign price = site.data.refining.price.level_1525 %}
파괴강석 개당 {{price.basic_stone}}골드, 돌파석 개당 {{price.leap_stone}}골드, 명예의 파편 개당 {{price.honor_shard}}골드, 오레하 개당 {{price.fusion}}골드

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
{%- assign basic_stone = material.basic_stone | times: price.basic_stone -%}
{%- assign fusion = material.fusion | times: price.fusion -%}
{%- assign honor_shard = material.honor_shard | times: price.honor_shard -%}
{%- assign leap_stone = material.leap_stone | times: price.leap_stone -%}
{%- assign refining_once = basic_stone| plus: fusion | plus: honor_shard | plus: leap_stone | plus: material.gold | round -%}
{%- assign refining_total = refining_once | times: avg | round -%}
{%- capture canvas_label %}{{canvas_label}}{{i}},{% endcapture -%}
{%- capture canvas_data %}{{canvas_data}}{{refining_total}},{% endcapture -%}
| {{i}} | {{material.probability}}% | {{refining_once}}골드 | {{refining_total}}골드 |
{% endfor %}

<canvas id="weapon_refining" style="box-sizing: border-box; width: 100%;"></canvas>

---

## 강화 확률에 따른 데이터 분석 방법 예시
각 트라이 횟수에 따른 확률은 다음과 같습니다. (기본 재련 확률 10%)

| 트라이 회차 | 트라이 확률 | N트만에 성공할 확률 | N트안에 성공할 확률 | 장인의 기운 |
|:-:|:-:|:-:|:-:|:-:|
{% for i in site.data.refining.refining_10 -%}
|{{ i.try_num }}|{{ i.change_probability | times:100 }}%|{{ i.success_this_time | times:100 }}%|{{ i.cumulative | times:100 }}%|{{ i.master_energy | times:100 }}%|
{% endfor %}

## 트라이 확률

해당 트라이 상황에서의 재련 성공 확률을 의미합니다.

예를 들어, 세 번째 트라이를 시도함을 가정하면 이는 첫 번째 및 두 번째 트라이가 모두 실패하였고,

실패 후 재련 보정을 받은 10% + (10% * 0.1 * 2) = 12%의 확률이 적용됩니다.

---

## N트만에 성공할 확률

N회차의 트라이 상황이 주어지는 상황의 확률과 해당 상황에서 트라이가 성공하는 확률을 곱한 값을 의미합니다.

즉, 우리가 재련을 시도할 때 N회차 이전에 성공하는 것이 아닌, 기어코 N회차에서 비로소 성공할 확률을 의미합니다.

3번째 트라이에 성공할 확률은 (100% - 10%)*(100% - 11%)*(12%) = 9.612% 입니다. 

---

## N트안에 성공할 확률

N트만에 성공할 확률의 누적 수치입니다.

예를 들어, 최대 세 번째 트라이까지 수행한다면, 10% + 9.9% + 9.612% = 29.512%의 확률로 재련에 성공합니다.

---

## 장인의 기운

현재 재련 단계에서 누적된 장인의 기운 수치를 의미합니다.

예를 들어, 위의 표에서 세 번째 트라이 회차의 장인의 기운 수치는 9.767%이며,

이는 첫 번째 및 두 번째 트라이 시 실패함으로써 얻은 장인의 기운 수치입니다.



15번째 트라이에서는 14번째 트라이 실패까지 누적된 장인의 기운이 100%에 도달함으로써, 무조건 재련에 성공하게 됩니다.

따라서, “트라이 확률”은 100%가 되고, “N트만에 성공할 확률”은 100%에서 이전 회차의 누적 사건 발생 확률 수치를 모두 차감한 수치입니다.

당연히 “N트 이하로 누적 성공 확률"은 100%가 됩니다.

<script>
var ctx = document.getElementById("weapon_refining");

var chart_data = [{{ canvas_data }}];
var labels = [{{ canvas_label }}];
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
    indexAxis: 'x',
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