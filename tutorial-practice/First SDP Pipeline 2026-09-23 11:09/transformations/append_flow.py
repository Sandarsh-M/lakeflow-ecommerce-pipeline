# from pyspark import pipelines as dp

# # Target streaming table that both flows append into
# dp.create_streaming_table("tot_sales")

# # Flow 1: append North sales
# @dp.append_flow(target="tot_sales")
# def north_sales():
#     df = spark.readStream.table("sdp_practice.source.sales_north")
#     return df

# # Flow 2: append South sales
# @dp.append_flow(target="tot_sales")
# def south_sales():
#     df = spark.readStream.table("sdp_practice.source.sales_south")
#     return df