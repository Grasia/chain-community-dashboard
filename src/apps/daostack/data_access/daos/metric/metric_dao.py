"""
   Descp: This is a dao (data access object) of metrics.
    It's used as interface to transform data from the datawarehouse
    and transfers like serie, stackedSerie, NStackedSerie.  

   Created on: 17-jul-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui 
        <f.r.youssef@hotmail.com>
"""

from typing import List
import pandas as pd

from src.apps.daostack.data_access.daos.metric.strategy.\
    strategy_metric_interface import IMetricStrategy
from src.apps.daostack.data_access.requesters.cache_requester import CacheRequester


class MetricDao():
    def __init__(self, ids: List[str], strategy: IMetricStrategy,
     requester: CacheRequester):
        self.__ids = ids
        self.__st = strategy
        self.__requester = requester


    def get_metric(self):
        df: pd.DataFrame = self.__requester.request()
        
        # get only data from daos in ids
        df = df.loc[df['dao'].isin(self.__ids)]

        return self.__st.process_data(df)
