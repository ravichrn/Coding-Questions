#spark
#given country, site, visits -> read to dataframe, get the top visited site per country using spark sql and then mapPartitions
#given a python function, write test code to cover all the scenarios

#pandas
#schema - company name, type of company, number of employees, url
#1. read to a dataframe - read_csv()
#2. filter compnaies with employees > 100000
#3. sum of employees by type of company
#4. number of companies per type of comapny - value_counts() 
#5. find the columns with missing/null values - df.isnull()
#6. replace True with 'Yes' and False with 'No' in a column - df.replace({True:'Yes', False:'No'})

#python
dataset = [
    {'uuid': 'b7g2f5d8h4k9m3q1t6x8z0w5c', 'file_seq_num':0, 'file_name':'tw2x8j7z1b6m9q5p3c0v1t4r9.json'},
    {'uuid': 'b7g2f5d8h4k9m3q1t6x8z0w5c', 'file_seq_num':1, 'file_name':'p9c4t6f2k8m5w1h3v7j9x2d4b.json'},
    {'uuid': 'b7g2f5d8h4k9m3q1t6x8z0w5c', 'file_seq_num':2, 'file_name':'r3s7y9n1j8k4e2w6c0v5x7d8p.json'},
    {'uuid': 'b7g2f5d8h4k9m3q1t6x8z0w5c', 'file_seq_num':3, 'file_name':'q8k2h5n1z9b4m6p3r7c0v2x8j.json'},
    {'uuid': 'b7g2f5d8h4k9m3q1t6x8z0w5c', 'file_seq_num':4, 'file_name':'z0t2c5m9r3v1p6j4n8k7w2h9x.json'},
    {'uuid': 'b7g2f5d8h4k9m3q1t6x8z0w5c', 'file_seq_num':5, 'file_name':'x4v8c2n6j1m9k5p0r3h7w2t5z.json'},
    {'uuid': 'p9x2a6y7u3w0n4r8j5h1e7s4k', 'file_seq_num':0, 'file_name':'e5r9p1t4w8c3m7n2j0h6k5v9x.json'},
    {'uuid': 'p9x2a6y7u3w0n4r8j5h1e7s4k', 'file_seq_num':1, 'file_name':'h4z8v1p9m3k7c2w5n0x6q4t9r.json'},
    {'uuid': 'p9x2a6y7u3w0n4r8j5h1e7s4k', 'file_seq_num':2, 'file_name':'d8j2x5k7n4c9v6h3m1q8t5p0w.json'}
]

