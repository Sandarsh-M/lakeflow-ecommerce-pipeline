# from pyspark import pipelines as dp
# from pyspark.sql.functions import col


# rules = {"rule1":"product_id IS NOT NULL",
#          "rule2":"updated_at IS NOT NULL"}

# @dp.table(name="products_table")
# @dp.expect_all(rules)

# def products_table():
#     df=spark.read.table("sdp_practice.source.products")
#     return df