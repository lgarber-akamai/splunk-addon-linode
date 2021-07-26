"""Handler for Linode Account Payments"""

import unittest

from .fixtures_util import request_fixture_override, MockHelper

from ..ta_linode_util import AccountPaymentsHandler, BaseLinodeEventLogger


class TestAccountPayments(unittest.TestCase):
    """Test Account payments event collectors"""

    @staticmethod
    def test_account_payments():
        """Test that payments are collected and filtered correctly"""

        handler = AccountPaymentsHandler(helper=MockHelper(), fixture_mode=True)
        request_fixture_override(handler)

        collect_time = BaseLinodeEventLogger._parse_time('2016-01-01T00:01:01')
        events = handler.fetch_data(collect_time)
        assert len(events) == 2
        assert events[0]['id'] == 123
        assert events[1]['id'] == 456

        collect_time = BaseLinodeEventLogger._parse_time('2018-01-01T00:01:01')
        events = handler.fetch_data(collect_time)
        assert len(events) == 1
        assert events[0]['id'] == 456

        collect_time = BaseLinodeEventLogger._parse_time('2020-01-01T00:01:01')
        events = handler.fetch_data(collect_time)
        assert len(events) == 0
