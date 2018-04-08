# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^start/$', views.start, name='start'),

    url(r'^time_scatter/$', views.time_scatter, name='time_scatter'),
    url(r'^time_scatterHandle(.*)_(.*)_(.*)_(.*)_(.*)_(.*)_(.*)/$', views.time_scatterHandle, name='time_scatterHandle'),

    url(r'^level_scatter/$', views.level_scatter, name='level_scatter'),
    url(r'^level_scatterHandle(.*)_(.*)_(.*)_(.*)_(.*)_(.*)_(.*)/$', views.level_scatterHandle, name='level_scatterHandle'),

    url(r'^statistic/$', views.statistic, name='statistic'),
    url(r'^statisticHandle(.*)_(.*)_(.*)_(.*)_(.*)_(.*)_(.*)/$', views.statisticHandle, name='statisticHandle'),

    url(r'^diff_statistic/$', views.diff_statistic, name='diff_statistic'),
    url(r'^diff_statisticHandle(.*)_(.*)_(.*)_(.*)_(.*)_(.*)_(.*)/$', views.diff_statisticHandle, name='diff_statisticHandle'),

    url(r'^time_level/$', views.time_level, name='time_level'),
    url(r'^time_levelHandle(.*)_(.*)_(.*)_(.*)_(.*)_(.*)_(.*)/$', views.time_levelHandle, name='time_levelHandle'),


]

app_name = 'draw'