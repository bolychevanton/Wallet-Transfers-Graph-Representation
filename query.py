from clickhouse_driver import Client
import pandas as pd


def get_transactions(
    clickhouse_url: str, wallet_address: str, n_depth: int, max_children: int
) -> pd.DataFrame:
    client = Client.from_url(clickhouse_url)

    # YOUR CODE GOES HERE

    # REWRITE LINES BELOW TO SOLVE THE PROBLEM
    # INTERPET THE CODE AS AN EXMAPLE OF USAGE
    # OF CLICKHOUSE DRIVER
    wallet_address = "0xa6fac4a7b509d4d103a6c764b72a177e39a0136e"
    sql_query = f"""
    SELECT 
        from_address, to_address, value 
    FROM 
        transactions 
    WHERE 
        from_address = '{wallet_address}' 
    ORDER BY 
        value 
    LIMIT {max_children}
    """
    df = client.query_dataframe(sql_query)

    return df
