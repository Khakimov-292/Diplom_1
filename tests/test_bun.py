import test_data.data
from praktikum.bun import Bun


class TestBun:
    def test_get_name_returns_correct_name(self):
        bun = Bun(test_data.data.BUN_NAME, test_data.data.BUN_PRICE)
        assert bun.get_name() == test_data.data.BUN_NAME

    def test_get_price_returns_correct_price(self):
        bun = Bun(test_data.data.BUN_NAME, test_data.data.BUN_PRICE)
        assert bun.get_price() == test_data.data.BUN_PRICE
