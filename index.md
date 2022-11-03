---
layout: default
title: Home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

# Day
{: .fs-9 }

Day guild information.
{: .fs-6 .fw-300 }

총인원 80

<canvas id="myChart1"></canvas>

1600대 몇명, 1590대 몇명

각 직업 인원수

딜러, 서포터 수

직업군(전사, 무도가, 헌터, 마법사, 암살자, 스페셜리스트)

<script>
var ctx = document.getElementById("myChart1");

var data1 = [1615, 1555, 1444];
var labels = ["High", "Avg", "Low"];
var data = {
    labels: labels,
    datasets: [{
        label: 'Level',
        data: data1,
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
    scales: {
        x: {
            min: 1400, 
            max: 1655
        }
    }
};

new Chart(ctx, {
  type: "bar",
  data: data, 
  options: options
});
</script>