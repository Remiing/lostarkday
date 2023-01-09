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
|{::nomarkdown}<p>{% include numberWithCommas.html number=row.equipTotal %}</p><div class="detail">
{%- assign equipDetail = row.equipDetail | split: ',' -%}
{%- for equip in equipDetail -%}
<p>{{equip}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{::nomarkdown}<p>{% include numberWithCommas.html number=row.accTotal %}</p><div class="detail">
{%- assign accDetail = row.accDetail | split: ',' -%}
{%- for acc in accDetail -%}
<p>{{acc}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{::nomarkdown}<p>{% include numberWithCommas.html number=row.gemTotal %}</p><div class="detail">
{%- assign gemDetail = row.gemDetail | split: ',' -%}
{%- for gem in gemDetail -%}
<p>{{gem}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{%- assign total_gold = row.equipTotal | plus: row.accTotal | plus: row.gemTotal -%}
{% include numberWithCommas.html number=total_gold %}|
{% endfor %}
