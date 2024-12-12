import re
import unittest

ipv6_pattern = re.compile(r"""
^(
    ([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|              # Полный адрес (8 групп по 4 символа)
    ([0-9a-fA-F]{1,4}:){1,7}:|                          # Сокращение с пустым блоком
    ([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|          # 1-6 групп, затем 1 группа
    ([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|   # 1-5 групп, затем 1-2 группы
    ([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|   # 1-4 группы, затем 1-3 группы
    ([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|   # 1-3 группы, затем 1-4 группы
    ([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|   # 1-2 группы, затем 1-5 групп
    [0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|        # 1 группа, затем 1-6 групп
    :((:[0-9a-fA-F]{1,4}){1,7}|:)                       # Сокращение :: или :1-7 групп
)$
""", re.VERBOSE)


def is_valid(test):
    return re.match(ipv6_pattern, test) is not None

def find_in_file(name):
    f = open(name,mode= "r")
    dele = r'[ ,;|.]'
    for i in f:
        temp = re.split(dele, i)
        for j in temp:
            lt = re.findall(ipv6_pattern,j)
            ans = [y[0] for y in lt]
            if ans:
                print(ans[0])





class TestIPv6(unittest.TestCase):
    def test_valid_ipv6_addresses(self):
        valid_ipv6_addresses = [
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "2001:db8:85a3:0:0:8a2e:370:7334",
            "2001:db8:85a3::8a2e:370:7334",
            "::1",
            "::",
            "fe80::1",
            "1234:5678:9abc:def0:1234:5678:9abc:def0",
            "0:0:0:0:0:0:0:1",
            "0:0:0:0:0:0:0:0"
        ]
        for address in valid_ipv6_addresses:
            with self.subTest(address=address):
                self.assertTrue(re.fullmatch(ipv6_pattern, address))

    def test_invalid_ipv6_addresses(self):
        invalid_ipv6_addresses = [
            "2001:db8:85a3:0:0:8a2e:3707334",
            "2001:db8:85a3::8a2e:370:7334:",
            ":2001:db8:85a3::8a2e:370:7334",
            "2001:db8:85a3:::8a2e:370:7334",
            "12345:5678:9abc:def0:1234:5678:9abc:def0",
            "2001:db8:85a3:0:0:8a2e:370",
            "2001:db8:85a3:0:0:8a2e:370:7334:1234",
            "1200::AB00:1234::2552:7777:1313"
        ]
        for address in invalid_ipv6_addresses:
            with self.subTest(address=address):
                self.assertFalse(re.fullmatch(ipv6_pattern, address))

if __name__ == "__main__":
    while True:
        print("запустить тестирование 1")
        print("поиск файла  2")
        v = input()
        if v == "2":
            find_in_file("test.txt")
        elif v == "1":
            unittest.main()
        else:
            print("нету такой функции")
