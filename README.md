# ib-trading-calendars

Trading calendars for Interactive Brokers-supported exchanges. Based on [quantopian/trading_calendars](https://github.com/quantopian/trading_calendars).

This package differs from the underlying `quantopian/trading_calendars` package in two ways. First, it uses IB exchange codes instead of MIC codes. Second, it corrects an issue with the open time, as described below.

## Installation

```
pip install ib-trading-calendars
```

## Supported exchanges

Currently the supported IB exchange codes are:

* AEB
* AMEX
* ARCA
* ASX
* BATS
* BM
* BVL
* BVME
* CBOE
* EBS
* ENEXT.BE
* FWB
* GLOBEX
* ICEUS
* IEX
* KSE
* LSE
* NASDAQ
* NYSE
* OSE
* PINK
* SBF
* SEHK
* SEHKNTL
* SEHKSZSE
* SFB
* SGX
* TSE
* TSEJ

## Usage

```python
from ib_trading_calendars import get_calendar
get_calendar("NYSE")
```

To see supported exchanges:

```python
from ib_trading_calendars import ib_calendar_names
print(ib_calendar_names)
```

## Open time

The underlying `quantopian/trading_calendars` package sets exchange open times 1 minute later than the actual open. For example, the exchange hours for NYSE are 9:31-16:00 in `quantopian/trading_calendars`, even though NYSE actually opens at 9:30. This behavior reflects the needs of zipline, from which `trading_calendars` originated, but it leads to incorrect results for more generic use cases:

```python
# quantopian/trading_calendars reports NYSE as closed shortly after the open
nyse_calendar = get_calendar("NYSE")
nyse_calendar.is_open_on_minute(pd.Timestamp("2019-01-30 09:30:30", tz="America/New_York"))
False
```

In `ib-trading-calendars` the open time is set to the actual exchange open time, rather than the subsequent minute.

## License

`ib-trading-calendars` is distributed under the Apache 2.0 License. See the LICENSE file in the release for details.
