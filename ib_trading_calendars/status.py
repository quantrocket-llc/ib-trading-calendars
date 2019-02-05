#!/usr/bin/env python

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

import argparse
import pandas as pd
import json
from ib_trading_calendars.calendar_utils import ib_calendar_factories

def get_exchange_status(exchange, dt):
    """
    Returns the exchange status at the specified datetime.
    """
    calendar_cls = ib_calendar_factories[exchange]

    asof_datetime = pd.Timestamp(dt, tz=calendar_cls.tz)
    start = asof_datetime - pd.Timedelta(days=30)
    start = pd.Timestamp(start.date(), tz="UTC")
    end = asof_datetime + pd.Timedelta(days=30)
    end = pd.Timestamp(end.date(), tz="UTC")
    calendar = calendar_cls(start=start, end=end)

    is_open = calendar.is_open_on_minute(asof_datetime)

    if is_open:
        since = calendar.previous_open(asof_datetime)
        until = calendar.next_close(asof_datetime)
    else:
        since = calendar.previous_close(asof_datetime)
        until = calendar.next_open(asof_datetime)

    since = since.tz_convert(asof_datetime.tz.zone).strftime("%Y-%m-%dT%H:%M:%S")
    until = until.tz_convert(asof_datetime.tz.zone).strftime("%Y-%m-%dT%H:%M:%S")

    return dict(
        status="open" if is_open else "closed",
        since=since,
        until=until)

def main():

    parser = argparse.ArgumentParser(
        description="check the status of an exchange at the specified time")
    parser.add_argument(
        "exchange",
        help="the IB exchange code")
    parser.add_argument(
        "dt",
        help="the ISO format datetime to check")

    args = parser.parse_args()
    args = vars(args)

    status = get_exchange_status(args["exchange"], args["dt"])
    print(json.dumps(status))
