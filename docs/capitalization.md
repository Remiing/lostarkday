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
{% assign material_price = site.data.material_price %}

| {::nomarkdown}<p>닉네임</p><p>클래스</p>{:/} | 아이템 | 장비 | 악세 | 보석 | 총합 |
|:-|:-:|:-:|:-:|:-:|:-:|
{% for member in members_data -%}
|{::nomarkdown}<p>{{member.name-}}</p><p>{{member.class-}}</p>{:/}{{-raw-}}
|{{member.itemLV-}}
|{%- assign weapon = member.equipment | split: '/' -%}
{::nomarkdown}<p>{{weapon[1]-}}</p><div class="detail">
{%- assign equip = member.equipment | split: ',' -%}
{%- assign equipName = member.equipment_name | split: ',' -%}
{%- for i in (0..5) -%}
{%- assign equipDetail = equip[i] | split: '/' -%}
<p>{{equipDetail[1]}} {{equipName[i]}} {{equipDetail[3]}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{::nomarkdown}<p>{{member.engraving_simple-}}</p><div class="detail">
{%- assign engraving_detail = member.engraving_detail | split: ',' -%}
{%- for engraving in engraving_detail -%}
<p>{{-engraving-}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{%- capture gemDetail %}{% endcapture -%}
{%- assign gem_total = 0 -%}
{%- assign gems = member.gem_simple | split: ',' -%}
{%- for gem in gems -%}
  {%- assign gemPrice = 0 -%}
  {%- assign gemType = gem | split: ' x' -%}
  {%- assign gemName = gemType[0] -%}
  {%- assign gemCount = gemType[1] | abs -%}
  {%- assign gemPrice = material_price | where:"itemName", gemName | map: "itemPrice" | first | ceil | times: gemCount -%}
  {%- assign gem_total = gem_total | plus: gemPrice -%}
  {%- capture gemDetail %}{{gemDetail}}{{gem}} {{gemPrice}},{% endcapture -%}
{%- endfor -%}
{::nomarkdown}<p>{{-gem_total-}}</p><div class="detail">
{%- assign gemDetail = gemDetail | split: ',' -%}
{%- for gem in gemDetail -%}
<p>{{-gem-}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|0|
{% endfor %}
