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

# To run: python3 -m unittest discover -s tests/ -p test_*.py -t . -v

import unittest
import pandas as pd
from ib_trading_calendars.status import get_exchange_status

class ExchangeStatusTestCase(unittest.TestCase):

    def test_ib_trading_calendars(self):

        # holiday
        self.assertDictEqual(
            get_exchange_status("SEHKNTL", "2014-10-06 10:00:00"),
            {'status': 'closed',
             'since': '2014-09-30T15:00:00',
             'until': '2014-10-08T09:30:00'})

        # reopened after holiday
        # Note: ib-trading-calendars ignores lunch break
        self.assertDictEqual(
            get_exchange_status("SEHKNTL", "2014-10-08 10:00:00"),
            {'status': 'open',
             'since': '2014-10-08T09:30:00',
             'until': '2014-10-08T15:00:00'})

        # MLK holiday
        self.assertDictEqual(
            get_exchange_status("NYSE", "2019-01-21 10:00:00"),
            {'status': 'closed',
             'since': '2019-01-18T16:00:00',
             'until': '2019-01-22T09:30:00'})

        # reopened after holiday
        self.assertDictEqual(
            get_exchange_status("NYSE", "2019-01-22 10:00:00"),
            {'status': 'open',
             'since': '2019-01-22T09:30:00',
             'until': '2019-01-22T16:00:00'})

        # early close
        self.assertDictEqual(
            get_exchange_status("NYSE", "2018-12-24 13:30:00"),
            {'status': 'closed',
             'since': '2018-12-24T13:00:00',
             'until': '2018-12-26T09:30:00'})

    def test_fallback_to_trading_calendars(self):
        self.assertDictEqual(
            get_exchange_status("XNYS", "2018-12-24 13:30:00"),
            {'status': 'closed',
             'since': '2018-12-24T13:00:00',
             'until': '2018-12-26T09:30:00'})
