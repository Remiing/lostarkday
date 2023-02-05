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

{% assign last_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign members_data = site.data.chart[last_data] %}
{% assign data = site.data.capitalization %}

| 닉네임 | 장비 | 악세 | 보석 | 총합 |
|:-|:-:|:-:|:-:|:-:|
{% for row in data -%}
{% assign member = members_data | where:"name", row.name | first -%}
|{{row.name-}}
|{::nomarkdown}<div class="td-relative"><p>{% include numberWithCommas.html number=row.equipTotal %}</p><div class="detail">
{%- assign equipPrice = row.equipPart | split: ',' -%}
{%- assign equipPart = member.equipment | split: ',' -%}
{%- assign list_len = equipPrice | size | minus: 1 -%}
{%- for i in (0..list_len) -%}
<p>{{equipPart[i]}} {{equipPrice[i]}}</p>
{%- endfor -%}</div></div>{:/}{{-raw-}}
|{::nomarkdown}<div class="td-relative"><p>{% include numberWithCommas.html number=row.accTotal %}</p><div class="detail">
{%- assign accPrice = row.accPart | split: ',' -%}
{%- assign accPart = member.accessory | split: ',' -%}
{%- assign list_len = accPrice | size | minus: 1 -%}
{%- for i in (0..list_len) -%}
<p>{{accPart[i]}} {{accPrice[i]}}</p>
{%- endfor -%}</div></div>{:/}{{-raw-}}
|{::nomarkdown}<div class="td-relative"><p>{% include numberWithCommas.html number=row.gemTotal %}</p><div class="detail">
{%- assign gemPrice = row.gemPart | split: ',' -%}
{%- assign gemPart = member.gem_simple | split: ',' -%}
{%- assign list_len = gemPrice | size | minus: 1 -%}
{%- for i in (0..list_len) -%}
<p>{{gemPart[i]}} {{gemPrice[i]}}</p>
{%- endfor -%}</div></div>{:/}{{-raw-}}
|{%- assign total_gold = row.equipTotal | plus: row.accTotal | plus: row.gemTotal -%}
{% include numberWithCommas.html number=total_gold %}|
{% endfor %}
