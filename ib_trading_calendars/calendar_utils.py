# Copyright 2019 QuantRocket LLC - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from itertools import chain
from trading_calendars import register_calendar, register_calendar_alias
from .exchange_calendar_nyse import NYSEExchangeCalendar

_ib_calendar_factories = {
    "NYSE": NYSEExchangeCalendar,
}

_ib_calendar_aliases = {
    "NASDAQ": "NYSE",
    "ARCA": "NYSE",
    "AMEX": "NYSE",
    "BATS": "NYSE",
    "IEX": "NYSE",
    "PINK": "NYSE",
}

ib_calendar_names = sorted(chain(_ib_calendar_factories.keys(),_ib_calendar_aliases.keys()))

for name, calendar in _ib_calendar_factories.items():
    register_calendar(name, calendar(), force=True)


for alias, real_name in _ib_calendar_aliases.items():
    register_calendar_alias(alias, real_name, force=True)
