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

# VAT_RATE оставяме за справка, но няма да се използва при изчисления
VAT_RATE = 0.2  

# Цени директно с ДДС (€/kWh)
PROVIDER_PRICES = {
    "electrohold": {
        "дневна": 0.14973,  # с ДДС
        "нощна": 0.08857,   # с ДДС
        "fees": 0.0
    },
    "evn": {
        "дневна": 0.14986,  # с ДДС
        "нощна": 0.08870,   # с ДДС
        "fees": 0.0
    },
    "energo_pro": {
        "дневна": 0.15838,  # с ДДС
        "нощна": 0.09478,   # с ДДС
        "fees": 0.0
    }
}        "нощна": .07519,
        "fees": .0 + .0 + .0
    }
}
