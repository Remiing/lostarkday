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
|{%- assign before_equip = before.equipmentLV | split: ',' -%}
{%- assign after_equip = after.equipmentLV | split: ',' -%}
{%- assign total_gold = 0 -%}
{%- for i in (0..5) -%}
{%- assign before_equip_val = before_equip[i] | split: ' ' | first -%}
{%- assign after_equip_val = after_equip[i] | split: ' ' | first -%}
{%- if before_equip_val == after_equip_val -%}{%- continue -%}{%- endif -%}
{%- assign before_equip_type = before_equip[i] | split: ' ' | last -%}
{%- assign after_equip_type = after_equip[i] | split: ' ' | last -%}

{::nomarkdown}<p>{{before_equip_type}} {{before_equip_val}} > {{after_equip_val}}</p>{:/}{% endfor -%}
|{{ total_gold}}|
{% endfor %}
{%- if empty_check == 0 -%}||||{%- endif -%}
