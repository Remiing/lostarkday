---
layout: default
title: chart
nav_order: 2
---

# Chart

Day guild members chart

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

Day guild members chart using _data guild_member.csv

| 닉네임 | 클래스 | 아이템 | 전투 | 원정대 | 각인 | 특성 | 카드 | 보석 | 무기 | 공격력 | 체력 | update |
|:------|:------|:-----|:----|:------|:------|:------|:------|:------|:------|:------|:------|:------|
{%- for member in site.data.guild_member %}
|{{member.character_name-}}
|{{member.character_class-}}
|{{member.character_item_level-}}
|{{member.character_battle_level-}}
|{{member.character_expedition_level-}}
|{{member.character_engraving | replace_regex: '[^0-9]', ''-}}
|{{member.character_stat-}}
|{{member.character_card-}}
|{{member.character_gem-}}
|{{member.character_equipment_level-}}
|{{member.character_power-}}
|{{member.character_vitality-}}
|{{member.character_modified_date}}|
{%- endfor %}
