"""Constants for the bg_tok integration."""
from homeassistant.const import UnitOfEnergy

DOMAIN = "bg_tok"
BGN_PER_KILOWATT_HOUR = f"BGN/{UnitOfEnergy.KILO_WATT_HOUR}"

CONF_PROVIDER = "provider"
PROVIDERS = ["electrohold", "evn", "energo_pro", "custom"]

CONF_TARIFF_TYPE = "tariff_type"
TARIFF_TYPES = ["dual", "single"]

CONF_CLOCK_OFFSET = "clock_offset"

CONF_CUSTOM_DAY_PRICE = "custom_day_price"

CONF_CUSTOM_NIGHT_PRICE = "custom_night_price"

VAT_RATE = 0.2

PROVIDER_PRICES = {
    # Section 6.1, https://www.dker.bg/uploads/reshenia/2025/res_c-03_25.pdf
    "electrohold": {
        "дневна": .24406,
        "нощна": .14438,
        "fees": .0 + .0 + .0
    },
    # Section 6.1, https://www.dker.bg/uploads/reshenia/2025/res_c-03_25.pdf
    "evn": {
        "дневна": .24425,
        "нощна": .14456,
        "fees": .0 + .0 + .0
    },
    # Section 6.3, https://www.dker.bg/uploads/reshenia/2025/res_c-03_25.pdf
    "energo_pro": {
        "дневна": .24673,
        "нощна": .14705,
        "fees": .0 + .0 + .0
    }
}
