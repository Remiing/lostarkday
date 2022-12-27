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
|{%- capture equipDetail %}{% endcapture -%}
{%- assign equip_total = 0 -%}
{%- assign equips = member.equipment | split: ',' -%}
{%- assign i = 0 -%}
{%- for equip in equips -%}
  {%- assign equipPrice = 0 -%}
  {%- assign equipPart = equip | split: '/' -%}
  {%- if i == 0 -%}{%- assign equipType = "무기" -%}
  {%- elsif i == 1 -%}{%- assign equipType = "투구" -%}
  {%- elsif i == 2 -%}{%- assign equipType = "상의" -%}
  {%- elsif i == 3 -%}{%- assign equipType = "하의" -%}
  {%- elsif i == 4 -%}{%- assign equipType = "장갑" -%}
  {%- elsif i == 5 -%}{%- assign equipType = "어깨" -%}
  {%- endif -%}
  {%- assign equipStep = equipPart[1] | abs -%}
  {%- assign equipLevel = equipPart[2] | remove:'lv' -%}
  {%- for step_price in site.data.step_price -%}
    {%- assign step_level = step_price.level | remove:'level_' -%}
    {%- assign step_num = step_price.step | remove:'step_' | abs -%}
    {%- if step_level == equipLevel and step_num > equipStep -%}{%- break -%}{%- endif -%}
    {%- if step_level == '1302' and step_num > 15 -%}{%- continue -%}{%- endif -%}
    {%- if step_level == '1340' and step_num <= 6 or step_num > 20 -%}{%- continue -%}{%- endif -%}
    {%- if step_level == '1390' and step_num <= 12 or step_num > 19 -%}{%- continue -%}{%- endif -%}
    {%- if step_level == '1525' and step_num <= 12 -%}{%- continue -%}{%- endif -%}
    {%- if i == 0 -%}
      {%- assign equipPrice = equipPrice | plus: step_price.weaponAvg -%}
    {%- else -%}
      {%- assign equipPrice = equipPrice | plus: step_price.armorAvg -%}
    {%- endif -%}
  {%- endfor -%}
  {%- assign equip_total = equip_total | plus: equipPrice -%}
  {%- capture equipDetail %}{{equipDetail}}{{equipType}} {{equipStep}} {{equipPrice}},{% endcapture -%}
  {%- assign i = i | plus: 1 -%}
{%- endfor -%}
{::nomarkdown}<p>{{-equip_total-}}</p><div class="detail">
{%- assign equipDetail = equipDetail | split: ',' -%}
{%- for equip in equipDetail -%}
<p>{{-equip-}}</p>
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
