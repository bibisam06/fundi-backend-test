#model/pqsql_test.py

import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.POSTGRES_TEST_DATABASE_STRING,
    min_size = config.POSTGRES_TEST_POOL_MIN_SIZE,
    max_size = config.POSTGRES_TEST_POOL_MAX_SIZE,
    max_idle = config.POSTGRES_TEST_POOL_MAX_IDLE
)

# def list_admin():
#     with pool_default.connection() as conn:
#         cur = conn.cursor(row_factory=psycopg.rows.dict_row)
#         try:
#             results = cur.execute("SELect * from tb_admin").fatchall()
#         except psycopg.OperationalError as err :
#             print(err)
#         except psycopg.ProgrammingError as err :
#             print(err)
#         except psycopg.IntegrityError as err:
#             print('postgresql integrityError via psycopg : %s', err)
#             results = False
#
#     return results

def list_admin():
    with pool_default.connection() as conn:
        cur = conn.cursor(row_factory=psycopg.rows.dict_row)
        try:
            cur.excute("call sp_l_admin('out1')")
            results = cur.execute("fetch all from out1").fatchall()
            conn.commit()
        except psycopg.OperationalError as err :
            print(err)
        except psycopg.ProgrammingError as err :
            print(err)
        except psycopg.IntegrityError as err:
            print('postgresql integrityError via psycopg : %s', err)
            results = False

    return results


