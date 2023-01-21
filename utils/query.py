from clickhouse_driver import Client
import pandas as pd
from config import SERVER


def get_transactions(
    wallet_address: str, n_depth: int, max_neighbours: int
) -> pd.DataFrame:
    SERVER.start()
    client = Client.from_url(
        f"clickhouse://localhost:{SERVER.local_bind_port}/ethereum"
    )

    # YOUR CODE GOES HERE

    # REWRITE LINES BELOW TO SOLVE THE PROBLEM
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
    DESC
    LIMIT 
        {max_neighbours}
    """
    transactions = client.query_dataframe(sql_query)

    # YOUR CODE ENDS HERE

    SERVER.close()

    return transactions
