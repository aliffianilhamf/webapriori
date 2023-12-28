from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Transaksi

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

from datetime import datetime, timezone

from .preprocessing import Preprocessing,ExtraPreprocessing
#Create your views here.
def index(request):
    transaksi = Transaksi.objects.all()
    # Convert transactions to a list of lists
    transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transaksi]
    #transaction_list = list(transactions)
    df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
    df = Preprocessing(df)

        
    item_count = df.groupby(["order_no", "item_name"])["item_name"].count().reset_index(name = "Count")
    item_count_pivot = item_count.pivot_table(index = "order_no", columns="item_name", values='Count', aggfunc = "sum",).fillna(0)
    ukuran_dataset = item_count_pivot.shape
    jumlah_transaksi = item_count_pivot.shape[0]
    jumlah_item = item_count_pivot.shape[1]
    
    
    context = {
        'title' : "Dashboard",
        'transaksis' : transaksi,
        'ukuran_dataset': ukuran_dataset,
        'jumlah_transaksi' : jumlah_transaksi,
        'jumlah_item' : jumlah_item
    }
    
    return render(request, 'aprioriapp/dashboard.html', context)
   


#semua data
def all_data(request):
    transaksi = Transaksi.objects.all()
    transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transaksi]
    df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
    item_count = df.groupby(["order_no", "item_name"])["item_name"].size().reset_index(name = "Count")
    item_count_unique = item_count.drop_duplicates(subset=["order_no", "item_name"])
    item_count_pivot = item_count_unique.pivot_table(index = "order_no", columns="item_name", values='Count', aggfunc = "count",).fillna(0)
    ukuran_dataset = item_count_pivot.shape
    jumlah_transaksi = item_count_pivot.shape[0]
    jumlah_item = item_count_pivot.shape[1]
    
    #paginator
    paginator = Paginator(transaksi,50)
    page = request.GET.get('page')
    transaksi = paginator.get_page(page)
    
   
    context = {
        'title' : "Data Transaksi",
        'transaksis' : transaksi,
        'ukuran_dataset': ukuran_dataset,
        'jumlah_transaksi' : jumlah_transaksi,
        'jumlah_item' : jumlah_item
    }
    
    return render(request, 'aprioriapp/data_transaksi.html', context)
   
def proses_apriori(request):
    #sesudah dicari
    if request.method == "POST":
        request.session['fromdate'] = request.POST['fromdate']
        request.session['todate'] = request.POST['todate']
        request.session['support'] = request.POST['support']
        request.session['confidence'] = request.POST['confidence']
        if 'extraPreprocessing' in request.POST:
             request.session['extraPreprocessing'] = request.POST['extraPreprocessing']
        else:
            request.session['extraPreprocessing'] = 'off'
    
    if request.session.get('fromdate'):
        fromdate = request.session.get('fromdate')
        todate = request.session.get('todate')
        extraPreprocessing = request.session.get('extraPreprocessing')
        transactions=Transaksi.objects.filter(order_time__range=[fromdate,todate])
        # Convert transactions to a list of lists
        transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transactions]
        #transaction_list = list(transactions)
        df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
        df = Preprocessing(df)

        if(extraPreprocessing == 'on'):
            df = ExtraPreprocessing(df)
        
            
        item_count = df.groupby(["order_no", "item_name"])["item_name"].count().reset_index(name = "Count")
        item_count_pivot = item_count.pivot_table(index = "order_no", columns="item_name", values='Count', aggfunc = "sum",).fillna(0)
        item_count_pivot = item_count_pivot.astype("int32")
        ukuran_dataset = item_count_pivot.shape
        jumlah_transaksi = item_count_pivot.shape[0]
        jumlah_item = item_count_pivot.shape[1]
        
        
        #menampilkan 50 data awal
        paginator = Paginator(transactions,50)
        page = request.GET.get('page')
        transactions = paginator.get_page(page)
        context = {
            'title' : "Proses Apriori",
            'transaksis' : transactions,
            'ukuran_dataset': ukuran_dataset,
            'jumlah_transaksi' : jumlah_transaksi,
            'jumlah_item' : jumlah_item
        }
        
        return render(request, 'aprioriapp/proses_apriori.html', context)
    
    context = {
            'title' : "Proses Apriori",
        }
    return render(request, 'aprioriapp/proses_apriori.html',context)

#data hasil
def data_hasil(request):
    #sesudah dicari
    if request.session.get('fromdate'):
        fromdate = request.session.get('fromdate')
        todate = request.session.get('todate')
        support = request.session.get('support')
        confidence = request.session.get('confidence')
        extraPreprocessing = request.session.get('extraPreprocessing')
        
        transactions=Transaksi.objects.filter(order_time__range=[fromdate,todate])
        # Convert transactions to a list of lists
        transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transactions]
        #transaction_list = list(transactions)
        df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
        df = Preprocessing(df)

        if(extraPreprocessing == 'on'):
            df = ExtraPreprocessing(df)
        
            
        item_count = df.groupby(["order_no", "item_name"])["item_name"].count().reset_index(name = "Count")
        item_count_pivot = item_count.pivot_table(index = "order_no", columns="item_name", values='Count', aggfunc = "sum",).fillna(0)
        item_count_pivot = item_count_pivot.astype("int32")
        ukuran_dataset = item_count_pivot.shape
        jumlah_transaksi = item_count_pivot.shape[0]
        jumlah_item = item_count_pivot.shape[1]
        def encode(x):
            if x <= 0 :
                return 0
            elif x >=1 :
                return 1
        item_count_pivot = item_count_pivot.applymap(encode)
        

        # Apply Apriori algorithm to find frequent itemsets
        min_support = float(support)  # Adjust this threshold as needed
        frequent_itemsets = apriori(item_count_pivot, min_support=min_support, use_colnames=True)

        # Generate association rules
        metric = "lift"
        min_threshold = 1
        rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
        # Minimum confidence threshold
        min_confidence = float(confidence)
        filtered_rules = rules.query(f'confidence >= {min_confidence}')
        filtered_rules.sort_values('confidence', ascending=False, inplace=True)
        rules.sort_values('confidence', ascending=False, inplace=True)

        # Convert the rules DataFrame to a list of dictionaries for easy rendering in Django template
        filtered_rules_list = filtered_rules.to_dict(orient='records')
        rules_list = rules.to_dict(orient='records')
        context = {
            'title' : "Data Hasil",
            'transaksis' : transactions,
            'association_rules': rules_list,
            'filtered_rules_list':filtered_rules_list,
        }
        
        return render(request, 'aprioriapp/data_hasil.html', context)
    context = {
            'title' : "Data Hasil",
        }
    return render(request, 'aprioriapp/data_hasil.html',context)
def chart_data(request):
    
    transaksi = Transaksi.objects.all()
    
     #chart
    transaction_time = [[ transaction.order_time] for transaction in transaksi]
    datetime_objects = [dt for inner_list in transaction_time for dt in inner_list]
    transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transaksi]
    df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
    transaction_time_list = [dt.strftime('%m/%d/%Y %H:%M') for dt in datetime_objects]
    datetime_list = [  dt if isinstance(dt, datetime) else datetime.strptime(dt, '%m/%d/%Y %H:%M') 
                        for dt in transaction_time_list
                    ]
    
    item_counts = df['item_name'].value_counts().head(10)
    #10 transaksi 
    x = item_counts.index.tolist()
    y = item_counts.values.tolist()
    

    return JsonResponse({'labels': x, 'data': y})
def transaksi_tiap_bulan(request): 
    transaksi = Transaksi.objects.all()
    
     #chart
    transaction_time = [[ transaction.order_time] for transaction in transaksi]
    datetime_objects = [dt for inner_list in transaction_time for dt in inner_list]
    transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transaksi]
    df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
    transaction_time_list = [dt.strftime('%m/%d/%Y %H:%M') for dt in datetime_objects]
    datetime_list = [  dt if isinstance(dt, datetime) else datetime.strptime(dt, '%m/%d/%Y %H:%M') 
                        for dt in transaction_time_list
                    ]
    
    # Add a new column 'month' to the DataFrame
    df['month'] = [dt.month for dt in datetime_list]
    # Group by 'month' and count the number of orders in each month
    data_perbulan = df.groupby('month')['order_no'].count()
    data_perbulan = pd.concat([data_perbulan.iloc[4:], data_perbulan.iloc[:4]])
    x = ['January','February', 'March', 'April', 'May', 'June', 'july','August', 'September']
    y = data_perbulan.values.tolist()

    return JsonResponse({'labels': x, 'data': y})
def transaksi_per_hari(request): 
    transaksi = Transaksi.objects.all()
    
     #chart
    transaction_time = [[ transaction.order_time] for transaction in transaksi]
    datetime_objects = [dt for inner_list in transaction_time for dt in inner_list]
    transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transaksi]
    df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
    transaction_time_list = [dt.strftime('%m/%d/%Y %H:%M') for dt in datetime_objects]
    datetime_list = [  dt if isinstance(dt, datetime) else datetime.strptime(dt, '%m/%d/%Y %H:%M') 
                        for dt in transaction_time_list
                    ]
    
    # Add a new column 'day' to the DataFrame
    df['day'] = [dt.strftime('%A') for dt in datetime_list]
    # Group by 'day' and count the number of orders in each day
    data_perhari = df.groupby('day')['order_no'].count()
    data_perhari = pd.concat([data_perhari.iloc[4:], data_perhari.iloc[:4]])
    x = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    y = data_perhari.values.tolist()

    return JsonResponse({'labels': x, 'data': y})
def transaksi_per_jam(request): 
    transaksi = Transaksi.objects.all()
    
     #chart
    transaction_time = [[ transaction.order_time] for transaction in transaksi]
    datetime_objects = [dt for inner_list in transaction_time for dt in inner_list]
    transaction_list = [[transaction.order_no, transaction.item_name] for transaction in transaksi]
    df = pd.DataFrame(transaction_list, columns=["order_no", "item_name"])
    transaction_time_list = [dt.strftime('%m/%d/%Y %H:%M') for dt in datetime_objects]
    datetime_list = [  dt if isinstance(dt, datetime) else datetime.strptime(dt, '%m/%d/%Y %H:%M') 
                        for dt in transaction_time_list
                    ]
    
    # Add a new column 'hour' to the DataFrame
    df['hour'] = [dt.hour for dt in datetime_list]
    # Group by 'hour' and count the number of orders in each hour
    data_perjam = df.groupby('hour')['order_no'].count()
    x = data_perjam.index.tolist()
    y = data_perjam.values.tolist()

    return JsonResponse({'labels': x, 'data': y})