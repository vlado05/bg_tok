[![](https://img.shields.io/github/release/vlado05/bg_electricity_regulated_pricing_bg_tok/all.svg?style=for-the-badge)](https://github.com/vlado05/bg_electricity_regulated_pricing_bg_tok/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![](https://img.shields.io/github/license/vlado05/bg_electricity_regulated_pricing_bg_tok?style=for-the-badge)](LICENSE.txt)
[![](https://img.shields.io/github/workflow/status/vlado05/bg_electricity_regulated_pricing_bg_tok/Python%20package?style=for-the-badge)](https://github.com/vlado05/bg_electricity_regulated_pricing_bg_tok/actions)

# БГ електроенергия - цена/тарифа
Custom integration for [Home Assistant](https://www.home-assistant.io) that provides the price of electricity on the regulated market for domestic customers, and the applicable tariff, (day or night).

All three major regional providers, Electrohold, EVN, and ENERGO-PRO are supported.

The prices are defined statically as they change only about once a year. The official source for the current prices is section 6 from [Resolution C-14/30.06.2023 of the Bulgarian Energy and Water Regulatory Commission](https://www.dker.bg/uploads/reshenia/2023/res_c_14_23.pdf). All prices are the final amount that you'd pay, including VAT.

The night tariff starts at 22:00 UTC+2 and ends at 06:00 UTC+2. Note that even though Bulgaria switches to UTC+3 in the summer, meter clocks are not adjusted. In other words, the night tariff starts at 22:00/ends at 06:00 in the winter and at 23:00/07:00 in the summer.

> [!NOTE]
> Summary in Bulgarian: Интеграция за Home Assistant, която предоставя сензори за текущата цена на електроенергията и текущата тарифа (дневна или нощна) според часа и конфигурирания доставчик на електронергия. Предоставените цени са определени от КЕВР за трите основни доставчика на регулирания пазар: Електрохолд, EVN и ЕНЕРГО-ПРО. 

## Provided sensors

The integration provides two sensors that adjust according to the time of day and the configuration:

### Current price in BGN per kWh

This sensor provides the current price according to the configured provider and current tariff (day or night). It can be used to track expenses together with an energy meter in Home Assistant. The ID of the sensor will be `sensor.xxx_price` where `xxx` is derived from the name you give to the integration instance when configuring it. 
             
<img src="https://github.com/vlado05/bg_electricity_regulated_pricing_bg_tok/raw/main/images/price.png" width="50%" height="auto">

### Current tariff (day or night)

This sensor provides the current tariff. It can be used to run power-hungry devices when the night tariff starts. The ID of the sensor will be `sensor.xxx_tariff` where `xxx` is derived from the name you give to the integration instance when configuring it.

<img src="https://github.com/vlado05/bg_electricity_regulated_pricing_bg_tok/raw/main/images/tariff.png" width="50%" height="auto">

## Install
