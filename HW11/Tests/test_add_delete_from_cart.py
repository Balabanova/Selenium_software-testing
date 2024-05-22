from main_page import MainPage
from product_page import ProductPage
from cart_page import CartPage


def test_cart(driver):
    main = MainPage(driver)
    product = ProductPage(driver)
    for i in range(0, 3):
        main.go_to_main_page()
        main.go_to_most_popular_product(1)
        assert product.add_product_to_cart()

    cart = CartPage(driver)
    cart.go_to_cart_page()
    items_count = len(cart.get_products_from_table())
    for i in range(0, items_count):
        item = cart.get_products_from_table()[0]
        print(item)
        assert cart.delete_product(item)

