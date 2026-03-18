"""Constants for the bg_tok integration."""
from homeassistant.const import UnitOfEnergy

DOMAIN = "bg_tok"
EUR_PER_KILOWATT_HOUR = f"EUR/{UnitOfEnergy.KILO_WATT_HOUR}"

CONF_PROVIDER = "provider"
PROVIDERS = ["electrohold", "evn", "energo_pro", "custom"]

CONF_TARIFF_TYPE = "tariff_type"
TARIFF_TYPES = ["dual", "single"]

CONF_CLOCK_OFFSET = "clock_offset"

CONF_CUSTOM_DAY_PRICE = "custom_day_price"

CONF_CUSTOM_NIGHT_PRICE = "custom_night_price"

VAT_RATE = 0.0

PROVIDER_PRICES = {
    # Section 6.1, https://www.dker.bg/uploads/reshenia/2025/res_c-03_25.pdf
    "electrohold": {
        "дневна": .14973,
        "нощна": .08857,
        "fees": .0 + .0 + .0
    },
    # Section 6.1, https://www.dker.bg/uploads/reshenia/2025/res_c-03_25.pdf
    "evn": {
        "дневна": .14986,
        "нощна": .08870,
        "fees": .0 + .0 + .0
    },
    # Section 6.3, https://www.dker.bg/uploads/reshenia/2025/res_c-03_25.pdf
    "energo_pro": {
        "дневна": .15838,
        "нощна": .09478,
        "fees": .0 + .0 + .0
    }
}
