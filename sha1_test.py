import unittest
import sha1

class HashTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(sha1.generate("hello"), "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d")

    def test2(self):
        self.assertEqual(sha1.generate("123"), "40bd001563085fc35165329ea1ff5c5ecbdbbeef")

    def test3(self):
        self.assertEqual(sha1.generate("hi321"), "bfd98e1f91cae3cfe944a8ff10b9eb0af8f8b062")


if __name__ == '__main__':
    unittest.main()
