#part1
import pandas as pd

customer_master = pd.read_csv('customer_master.csv')
print(customer_master.head())

item_master = pd.read_csv('item_master.csv')
print(item_master.head())

transaction_1 = pd.read_csv('transaction_1.csv')
print(transaction_1.head())

transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
print(transaction_detail_1.head())

#part2
transaction_2 = pd.read_csv('transaction_2.csv')
transaction = pd.concat([transaction_1, transaction_2], ignore_index = True)
print(transaction.head())

print(len(transaction_1))
print(len(transaction_2))
print(len(transaction))

transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail=pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
print(transaction_detail.head())

#part3
join_data = pd.merge(transaction_detail, transaction[['transaction_id','payment_date','customer_id']], on='transaction_id', how='left')
print(join_data.head())

print(len(transaction_detail))
print(len(transaction))
print(len(join_data))

#part4
join_data = pd.merge(join_data, customer_master, on='customer_id', how='left')
join_data = pd.merge(join_data, item_master, on='item_id', how='left')
print(join_data.head())

#part5
join_data['price'] = join_data['quantity']*join_data['item_price']
print(join_data[['price', 'quantity','item_price']].head())

#part6
print(join_data['price'].sum())
print(transaction['price'].sum())

print(join_data['price'].sum() == transaction['price'].sum())

#part7
print(join_data.isnull().sum())
print(join_data.describe())

#part8
print(join_data['payment_date'].min())
print(join_data['payment_date'].max())

print(join_data.dtypes)

join_data['payment_date']=pd.to_datetime(join_data['payment_date'])
join_data['payment_month']=join_data['payment_date'].dt.strftime('%Y%m')
print(join_data[['payment_date', 'payment_month']].head())

print(join_data.groupby('payment_month')[['price']].sum())

#part9 
