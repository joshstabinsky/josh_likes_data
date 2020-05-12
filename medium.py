# tl;dr

# create query object

query = '''
select * 
from your_schema.your_table
where this_filer = true
and that_filter = false
and last_filter = false
'''

# use the following pandas function to create the dataframe using the output of the query results
df = sql(query).toPandas()

# view the results
df.head()