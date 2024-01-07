import unittest
from rust_x3dh import x3dh_ser

class X3DHTest(unittest.TestCase):
    def test_shared_secret_keys(self):
        u1_shared_secret_key, u2_shared_secret_key = x3dh_ser.gen_3xdh_secrets_key_pairs()

        self.assertEqual(u1_shared_secret_key, u2_shared_secret_key)

if __name__ == '__main__':
    unittest.main()