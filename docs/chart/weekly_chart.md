---
layout: default
title: Weekly
parent: Chart
nav_order: 2
---

# Weekly chart
{: .fs-9 }

주간 템레벨 변화
{: .fs-6 .fw-300 }

{{site.data.update_time[-8].update_time}} ~ {{site.data.update_time[-1].update_time}}
{: .text-right }

---

{% assign member_list = site.data.guild_members.main_character | concat: site.data.guild_members.sub_character %}
{% assign before_data = site.data.update_time[-8].filename | remove: ".csv" %}
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
    {%- assign tier = "level_1525,level_1390,level_1340,level_1302" | split:"," -%}
    {%- assign before_tier = nil -%}
    {%- assign after_tier = nil -%}
    {%- for t in tier -%}
      {%- for set in site.data.equipment_set[t] -%}
        {%- if before_tier == nil and before_equip[i] contains set -%}{%- assign before_tier = t -%}{%- endif -%}
        {%- if after_tier == nil and after_equip[i] contains set -%}{%- assign after_tier = t -%}{%- endif -%}
      {%- endfor -%}
      {%- if before_tier and after_tier -%}{%- break -%}{%- endif -%}
    {%- endfor -%}

    {%- if before_equip_val < after_equip_val and before_tier == after_tier -%}
      {%- assign step_list = nil -%}
      {%- assign start_step = before_equip_val | plus: 1 -%}
      {%- assign end_step = after_equip_val -%}
      {%- for j in (start_step..end_step) -%}
        {%- capture step_list %}{{step_list}}{{before_tier}}-{{j}},{% endcapture -%}
      {%- endfor -%}
    {%- endif -%}

    {%- if before_tier != after_tier -%}
      {%- assign step_list = nil -%}
      
      {%- if before_tier == 'level_1340' -%}
        {%- if before_equip_val < '20' -%}
          {%- assign start_step = before_equip_val | plus: 1 -%}
          {%- for j in (start_step..20) -%}
            {%- capture step_list %}{{step_list}}{{before_tier}}-{{j}},{% endcapture -%}
          {%- endfor -%}
        {%- endif -%}
      {%- endif -%}

      {%- if before_tier == 'level_1390' -%}
        {%- if before_equip_val < '19' -%}
          {%- assign start_step = before_equip_val | plus: 1 -%}
          {%- for j in (start_step..19) -%}
            {%- capture step_list %}{{step_list}}{{before_tier}}-{{j}},{% endcapture -%}
          {%- endfor -%}
        {%- endif -%}
      {%- endif -%}

      {%- assign end_step = after_equip_val -%}
      {%- for j in (13..end_step) -%}
        {%- capture step_list %}{{step_list}}{{after_tier}}-{{j}},{% endcapture -%}
      {%- endfor -%}
    {%- endif -%}

    {%- assign step_list = step_list | split:"," -%}
    {%- for tier_step in step_list -%}
      {%- assign tier = tier_step | split:"-" | first -%}
      {%- assign step = tier_step | split:"-" | last -%}
      {%- assign price = site.data.refining.price[tier] -%}
      {%- assign step = 'step_' | append: step -%}
      {%- if i == 0 -%}{%- assign material = site.data.refining.weapon_material[tier][step] -%}{%- assign basic_stone = 'destruction_stone' -%}
      {%- else -%}{%- assign material = site.data.refining.armor_material[tier][step] -%}{%- assign basic_stone = 'guardian_stone' -%}{%- endif -%}
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
      {%- assign basic_stone = material[basic_stone] | times: price[basic_stone] -%}
      {%- assign fusion = material.fusion | times: price.fusion -%}
      {%- assign honor_shard = material.honor_shard | times: price.honor_shard -%}
      {%- assign leap_stone = material.leap_stone | times: price.leap_stone -%}
      {%- assign refining_once = basic_stone| plus: fusion | plus: honor_shard | plus: leap_stone | plus: material.gold | round -%}
      {%- assign refining_total = refining_once | times: avg | round -%}
      {%- assign total_gold = total_gold | plus: refining_total -%}
    {%- endfor -%}

    {::nomarkdown}<p>{{before_equip_type}} {{before_equip_val}} > {{after_equip_val}}</p>{:/}{% endfor -%}
  |{{ total_gold }}골드|
  {% endfor %}
{%- if empty_check == 0 -%}||||{%- endif -%}
