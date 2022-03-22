from cgi import test


testQuery = f"""
create or replace table temp.test_dag
as
select 1 as test_column
"""