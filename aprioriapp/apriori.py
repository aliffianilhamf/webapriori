import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import association_rules, apriori

from .models import Transaksi

# load dataset

data = Transaksi.objects.all()
data['order_time'] = pd.to_datetime(data['order_time'], format="%d-%m-%Y %H:%M")

data['month'] = data['order_time'].dt.month
data['day'] = data['order_time'].dt.weekday

data['month'].replace([i for i in range (1, 12 + 1)], ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "september", "Oktober", "November", "desember"], inplace=True)
data['day'].replace([i for i in range (6+1)], ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"], inplace=True)

# ambli data
def get_data(period_day = '', weekday_weekend = '', month = '', day = ''):
    ds = data.copy()
    filtered = [
        (ds['period_day'].str.contains(period_day))&
        (ds['weekday_weekend'].str.contains(weekday_weekend))&
        (ds['month'].str.contains(month.title()))&
        (ds['day'].str.contains(day.title))
    ]
    
    return filtered if filtered.shape[0] else "NO RESULT!" 
 
#encoding
def encode(x):
    if x <= 0 :
        return 0
    elif x >=1 :
        return 1
    
#
if type(data) != type ("No Result"):
    item_count = data.groupby(["order_no", "item_name"])["item_name"].count().reset_index(name = "Count")
    item_count_pivot = item_count.pivot_table(index = "order_no", columns="item_name", values='Count', aggfunc = "sum",).fillna(0)
    item_count_pivot = item_count_pivot.applymap(encode)
    
    support = 0.01
    frequent_item = apriori(item_count_pivot,min_support=support, use_colnames = True)
    
    metric = "lift"
    min_threshold = 1
    
    rules = association_rules(frequent_item, metric=metric, min_threshold=min_threshold)[["antecedents","consequents","support","confidence", "lift"]]
    
    rules.sort_values('confidence', ascending=False, inplace=True)
    
def parse_list(x):
    x = list(x)
    if len(x) == 1 :
        return x[0]
    elif len(x) > 1 :
        return ", ".join(x)
    
def return_item_data(item_antecedents):
    data = rules[["antecedents", "consequents"]].copy()
    
    data["antecedents"] = data["antecedents"].apply(parse_list)
    data["consequents"] = data["consequents"].apply(parse_list)
    
    return list(data.loc[data["antecedents"] == item_antecedents].iloc[0, :])

def tampil(item_name):
    if type(data) != type("No result!"):
        print(f"Jika Customer membeli **{item_name}** Maka Membeli**{return_item_data(item_name)}**")
    