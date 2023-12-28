from django.urls import path, include
from . import views 

urlpatterns = [ 
    path("", views.index, name="index"),
    path("data_transaksi/", views.all_data, name="data_transaksi"),
    path("proses_apriori/", views.proses_apriori, name="proses_apriori"),
    path("data_hasil/", views.data_hasil, name="data_hasil"),
    path('chart_data/', views.chart_data, name='chart_data'),
    path("transaksi_tiap_bulan/", views.transaksi_tiap_bulan, name="transaksi_tiap_bulan"),
    path("transaksi_per_hari/", views.transaksi_per_hari, name="transaksi_per_hari"),
    path("transaksi_per_jam/", views.transaksi_per_jam, name="transaksi_per_jam"),
]