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
    # Section 6.1, https://www.dker.bg/uploads/reshenia/2024/res-c-17-2024.pdf
    "electrohold": {
        "дневна": .16210,
        "нощна": .07104,
        "fees": .01354 + .00770 + .03803
    },
    # Section 6.1, https://www.dker.bg/uploads/reshenia/2024/res-c-17-2024.pdf
    "evn": {
        "дневна": .15926,
        "нощна": .06833,
        "fees": .01354 + .00819 + .03704
    },
    # Section 6.3, https://www.dker.bg/uploads/reshenia/2024/res-c-17-2024.pdf
    "energo_pro": {
        "дневна": .16341,
        "нощна": .06636,
        "fees": .01354 + .00977 + .03689
    }
}
