from cgi import test


testQuery = f"""
create or replace table temp.test_dag
as
select 2 as test_column
"""