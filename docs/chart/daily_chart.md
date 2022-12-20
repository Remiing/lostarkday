---
layout: default
title: Daily
parent: Chart
nav_order: 1
---

# Daily chart
{: .fs-9 }

일간 템레벨 변화
{: .fs-6 .fw-300 }

{{site.data.update_time[-2].update_time}} ~ {{site.data.update_time[-1].update_time}}
{: .text-right }

---

{% assign member_list = site.data.guild_members.main_character | concat: site.data.guild_members.sub_character %}
{% assign before_data = site.data.update_time[-2].filename | remove: ".csv" %}
{% assign after_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign before_data = site.data.chart[before_data] %}
{% assign after_data = site.data.chart[after_data] %}

| {::nomarkdown}<p>닉네임</p><p>클래스</p>{:/} | 아이템 레벨 변화 | 강화 수치 변화 | 기대값 |
|:-|:-:|:-:|:-:|
{% assign empty_check = 0 -%}
{%- for member in member_list -%}
  {%- assign before = before_data | where:"name", member | first -%}
  {%- assign after = after_data | where:"name", member | first -%}
  {%- unless before and after -%}{%- continue -%}{%- endunless -%}
  {%- if before.itemLV == after.itemLV -%}{%- continue -%}{%- else -%}{%- assign empty_check = 1 -%}{%- endif -%}
  |{::nomarkdown}<p>{{after.name-}}</p><p>{{after.class-}}</p>{:/}{{-raw-}}
  |{{before.itemLV}} > {{after.itemLV-}}
  |{%- assign before_equip = before.equipment | split: ',' -%}
  {%- assign after_equip = after.equipment | split: ',' -%}
  {%- if before_equip.size != 6 or after_equip.size != 6 -%}{%- continue -%}{%- endif -%}
  {%- assign total_gold = 0 -%}
  {%- for i in (0..5) -%}
    {%- assign before_equipPart = before_equip[i] | split: '/' -%}
    {%- assign after_equipPart = after_equip[i] | split: '/' -%}
    {%- assign before_equipStep = before_equipPart[1] | abs -%}
    {%- assign after_equipStep = after_equipPart[1] | abs -%}
    {%- if before_equipStep == after_equipStep -%}{%- continue -%}{%- endif -%}
    {%- assign before_equipType = before_equipPart[0] -%}
    {%- assign after_equipType = after_equipPart[0] -%}
    {%- assign before_equipLevel = before_equipPart[2] | remove:'lv' -%}
    {%- assign after_equipLevel = after_equipPart[2] | remove:'lv' -%}
    {%- assign part_gold = 0 -%}
    {%- for step_price in site.data.step_price -%}
      {%- assign step_level = step_price.level | remove:'level_' -%}
      {%- assign step_num = step_price.step | remove:'step_' | abs -%}
      {%- if step_level != before_equipLevel and step_level != after_equipLevel -%}{%- continue -%}{%- endif -%}
      {%- if step_level == '1302' and step_num > 15 -%}{%- continue -%}{%- endif -%}
      {%- if step_level == '1340' and step_num <= 6 or step_num > 20 -%}{%- continue -%}{%- endif -%}
      {%- if step_level == '1390' and step_num <= 12 or step_num > 19 -%}{%- continue -%}{%- endif -%}
      {%- if step_level == '1525' and step_num <= 12 -%}{%- continue -%}{%- endif -%}
      {%- if step_level == before_equipLevel and step_num <= before_equipStep -%}{%- continue -%}{%- endif -%}
      {%- if step_level == after_equipLevel and step_num > after_equipStep -%}{%- continue -%}{%- endif -%}
      {%- if i == 0 -%}
        {%- assign part_gold = part_gold | plus: step_price.weaponAvg -%}
      {%- else -%}
        {%- assign part_gold = part_gold | plus: step_price.armorAvg -%}
      {%- endif -%}
    {%- endfor -%}
    {%- assign total_gold = total_gold | plus: part_gold -%}
    {::nomarkdown}<p>{{before_equipType}} {{before_equipStep}} > {{after_equipStep}}</p>{:/}{{-raw-}}
  {%- endfor -%}
  |{{ total_gold }}골드|
{% endfor %}
{%- if empty_check == 0 -%}||||{%- endif -%}
