from pyspark import pipelines as dp
from pyspark.sql.functions import col


# ------------------------------------------------------------------
# 1. Source: stream new/changed rows from the raw products table
# ------------------------------------------------------------------
@dp.temporary_view(name="product_source")
def product_source():
    return spark.readStream.table("sdp_practice.source.products")


# ------------------------------------------------------------------
# 2. SCD Type 2 target (full history)
#    Table declaration and its flow are kept together so the
#    pipeline always registers both.
# ------------------------------------------------------------------
dp.create_streaming_table(
    name="products_scd2",
    comment="Products with full change history (SCD Type 2)"
)

dp.create_auto_cdc_flow(
    name="products_scd2_flow",          # explicit, unique flow name
    target="products_scd2",
    source="product_source",
    keys=["product_id"],
    sequence_by=col("updated_at"),
    except_column_list=["updated_at"],  # history lives in __START_AT / __END_AT
    stored_as_scd_type=2                # integer, not string
)


# ------------------------------------------------------------------
# 3. SCD Type 1 target (latest version only)
# ------------------------------------------------------------------
dp.create_streaming_table(
    name="products_scd1",
    comment="Latest version of each product (SCD Type 1)"
)

dp.create_auto_cdc_flow(
    name="products_scd1_flow",          # explicit, unique flow name
    target="products_scd1",
    source="product_source",
    keys=["product_id"],
    sequence_by=col("updated_at"),
    stored_as_scd_type=1                # keeps updated_at so you can see last change time
)