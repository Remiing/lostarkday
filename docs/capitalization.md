---
layout: default
title: Capitalization
nav_order: 5
---

# Capitalization
{: .fs-9 }

Character value gold conversion
{: .fs-6 .fw-300 }

---

Last Update {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign data = site.data.capitalization %}

| 닉네임 | 아이템 | 장비 | 악세 | 보석 | 총합 |
|:-|:-:|:-:|:-:|:-:|:-:|
{% for row in data -%}
|{{row.name-}}
|{{row.itemLV-}}
|{::nomarkdown}<p>{{row.equipTotal}}</p><div class="detail">
{%- assign equipDetail = row.equipDetail | split: ',' -%}
{%- for equip in equipDetail -%}
<p>{{equip}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{::nomarkdown}<p>{{row.accTotal}}</p><div class="detail">
{%- assign accDetail = row.accDetail | split: ',' -%}
{%- for equip in accDetail -%}
<p>{{equip}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{::nomarkdown}<p>{{row.gemTotal}}</p><div class="detail">
{%- assign gemDetail = row.gemDetail | split: ',' -%}
{%- for equip in gemDetail -%}
<p>{{equip}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{{row.equipTotal | plus: row.accTotal | plus: row.gemTotal}}|
{% endfor %}
