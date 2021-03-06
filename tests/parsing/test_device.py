import unittest

from banyan.model.user_device import Device
from tests.parsing import load_testdata


class DeviceParserTest(unittest.TestCase):
    def test_device(self):
        d: Device = Device.Schema().loads(load_testdata("tests/data/device.json"))
        self.assertEqual("C02WG12DHTD7", d.serial_number)
        self.assertEqual(True, bool(d.registered_status))
        self.assertEqual("High", d.trust_data.level)
        self.assertEqual("BNN", d.mdm_data.source)
        self.assertEqual("AutoUpdateEnabled", d.trust_data.factors[0].name)
        self.assertEqual(True, bool(d.trust_data.factors[0].value))
        self.assertEqual("banyan", d.trust_data.factors[0].source)
