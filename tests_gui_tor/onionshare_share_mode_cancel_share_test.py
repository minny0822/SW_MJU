#!/usr/bin/env python3
import os
import sys
import unittest
import pytest
import json

from PyQt5 import QtWidgets

from onionshare.common import Common
from onionshare.web import Web
from onionshare import onion, strings
from onionshare_gui import *

from .commontests import CommonTests

class OnionShareGuiTest(unittest.TestCase):
    '''Test the OnionShare GUI'''
    @classmethod
    def setUpClass(cls):
        '''Create the GUI'''
        # Create our test file
        testfile = open('/tmp/test.txt', 'w')
        testfile.write('onionshare')
        testfile.close()
        common = Common()
        common.define_css()

        # Start the Onion
        strings.load_strings(common)

        testonion = onion.Onion(common)
        global qtapp
        qtapp = Application(common)
        app = OnionShare(common, testonion, False, 0)

        web = Web(common, False, True)

        test_settings = {
            "auth_password": "",
            "auth_type": "no_auth",
            "autoupdate_timestamp": "",
            "close_after_first_download": True,
            "connection_type": "bundled",
            "control_port_address": "127.0.0.1",
            "control_port_port": 9051,
            "downloads_dir": "/tmp/OnionShare",
            "hidservauth_string": "",
            "no_bridges": True,
            "private_key": "",
            "public_mode": False,
            "receive_allow_receiver_shutdown": True,
            "save_private_key": False,
            "shutdown_timeout": False,
            "slug": "",
            "socks_address": "127.0.0.1",
            "socks_port": 9050,
            "socket_file_path": "/var/run/tor/control",
            "systray_notifications": True,
            "tor_bridges_use_meek_lite_azure": False,
            "tor_bridges_use_meek_lite_amazon": False,
            "tor_bridges_use_custom_bridges": "",
            "tor_bridges_use_obfs4": False,
            "use_stealth": False,
            "use_legacy_v2_onions": False,
            "use_autoupdate": True,
            "version": "1.3.1"
        }
        testsettings = '/tmp/testsettings.json'
        open(testsettings, 'w').write(json.dumps(test_settings))

        cls.gui = OnionShareGui(common, testonion, qtapp, app, ['/tmp/test.txt'], testsettings, False)

    @classmethod
    def tearDownClass(cls):
        '''Clean up after tests'''
        os.remove('/tmp/test.txt')

    @pytest.mark.run(order=1)
    def test_gui_loaded(self):
        CommonTests.test_gui_loaded(self)

    @pytest.mark.run(order=2)
    def test_windowTitle_seen(self):
        CommonTests.test_windowTitle_seen(self)

    @pytest.mark.run(order=3)
    def test_settings_button_is_visible(self):
        CommonTests.test_settings_button_is_visible(self)

    @pytest.mark.run(order=4)
    def test_server_status_bar_is_visible(self):
        CommonTests.test_server_status_bar_is_visible(self)

    @pytest.mark.run(order=5)
    def test_file_selection_widget_has_a_file(self):
        CommonTests.test_file_selection_widget_has_a_file(self)

    @pytest.mark.run(order=8)
    def test_deleting_only_file_hides_delete_button(self):
        CommonTests.test_deleting_only_file_hides_delete_button(self)

    @pytest.mark.run(order=9)
    def test_add_a_file_and_delete_using_its_delete_widget(self):
        CommonTests.test_add_a_file_and_delete_using_its_delete_widget(self)

    @pytest.mark.run(order=10)
    def test_file_selection_widget_readd_files(self):
        CommonTests.test_file_selection_widget_readd_files(self)

    @pytest.mark.run(order=11)
    def test_server_working_on_start_button_pressed(self):
        CommonTests.test_server_working_on_start_button_pressed(self, 'share')

    @pytest.mark.run(order=12)
    def test_server_status_indicator_says_starting(self):
        CommonTests.test_server_status_indicator_says_starting(self, 'share')

    @pytest.mark.run(order=13)
    def test_add_delete_buttons_hidden(self):
        CommonTests.test_add_delete_buttons_hidden(self)

    @pytest.mark.run(order=14)
    def test_settings_button_is_hidden(self):
        CommonTests.test_settings_button_is_hidden(self)

    @pytest.mark.run(order=16)
    def test_a_web_server_is_running(self):
        CommonTests.test_a_web_server_is_running(self)

    @pytest.mark.run(order=17)
    def test_cancel_the_share(self):
        CommonTests.test_cancel_the_share(self, 'share')

    @pytest.mark.run(order=18)
    def test_server_is_stopped(self):
        CommonTests.test_server_is_stopped(self, 'share', False)

    @pytest.mark.run(order=19)
    def test_web_service_is_stopped(self):
        CommonTests.test_web_service_is_stopped(self)

    @pytest.mark.run(order=20)
    def test_add_button_visible(self):
        CommonTests.test_add_button_visible(self)


if __name__ == "__main__":
    unittest.main()
