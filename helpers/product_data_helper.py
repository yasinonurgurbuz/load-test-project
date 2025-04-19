import os
import random

def get_random_product_name_data():
    data = open(os.path.abspath("data/product_names_data"), "r")
    data_row = random.choice(data.readlines()).rstrip("\n")
    data_row_split = data_row.split(',')
    return data_row_split

def get_random_promotion_ids_data():
    data = open(os.path.abspath("data/promotion_ids_data"), "r")
    data_row = random.choice(data.readlines()).rstrip("\n")
    data_row_split = data_row.split(',')
    return data_row_split

def get_random_category_names_data():
    data = open(os.path.abspath("data/category_names_data"), "r")
    data_row = random.choice(data.readlines()).rstrip("\n")
    data_row_split = data_row.split(',')
    return data_row_split