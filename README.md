# ib-trading-calendars

Trading calendars for Interactive Brokers-supported exchanges. Based on [quantopian/trading_calendars](https://github.com/quantopian/trading_calendars).

This package differs from the underlying `quantopian/trading_calendars` package in that it uses IBKR exchange codes instead of MIC codes.

## Installation

```
pip install ib-trading-calendars
```

## Supported exchanges

Currently the supported IBKR exchange codes are:

* AEB
* AMEX
* ARCA
* ASX
* BATS
* BM
* BUX
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
* MEXI
* MOEX
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
* VSE
* WSE

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

## License

`ib-trading-calendars` is distributed under the Apache 2.0 License. See the LICENSE file in the release for details.
