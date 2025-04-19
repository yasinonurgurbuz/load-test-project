from locust import HttpUser, between, task

from helpers.header_helper import *
from helpers.product_data_helper import *


class InsiderLoadTest(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://www.n11.com"

    @task(40)
    def get_search_with_different_product_names(self):
        product_names = get_random_product_name_data()
        path=f"/arama?q={product_names[0]}"
        self.client.get(path,
                        headers=get_header(),
                        name="search_with_product_names")
        print(f"⏩ GET request sends for product names: {self.host}{path}")

    @task(40)
    def get_search_with_different_promotion_ids(self):
        promotion_ids = get_random_promotion_ids_data()
        path=f"/arama?promotions={promotion_ids[0]}"
        self.client.get(path,
                        headers=get_header(),
                        name="search_with_promotion_ids")
        print(f"⏩ GET request sends for promotion ids: {self.host}{path}")

    @task(20)
    def get_search_with_different_category_names(self):
        category_names = get_random_category_names_data()
        path=f"/{category_names[0]}"
        self.client.get(path,
                        headers=get_header(),
                        name="search_with_category_names")
        print(f"⏩ GET request sends for category names: {self.host}{path}")