---
layout: default
title: Daily
parent: Chart
nav_order: 1
---

# Daily chart
{: .fs-9 }

Day guild members ranking
{: .fs-6 .fw-300 }

---

{% for chart_hash in site.data.chart %}
  {% assign last_update = chart_hash %}
{% endfor %}


