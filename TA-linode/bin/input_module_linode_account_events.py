
# encoding = utf-8

import os
import sys
import time
import datetime

def validate_input(helper, definition):
    pass

def collect_events(helper, ew):
    from ta_linode_util.account_events import AccountEventsHandler
    handler = AccountEventsHandler(helper, ew)
    handler.collect_events()

