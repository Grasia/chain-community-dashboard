"""
   Descp: Strategy pattern to create votes-voters rate.

   Created on: 04-nov-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui
        <f.r.youssef@hotmail.com>
"""
import pandas as pd
from typing import List

from src.apps.common.data_access.daos.metric.imetric_strategy \
    import IMetricStrategy
from src.apps.common.business.transfers.stacked_serie import StackedSerie
from src.apps.common.business.transfers.serie import Serie 
import src.apps.common.data_access.pandas_utils as pd_utl
import src.apps.daohaus.data_access.daos.metric.strategy.st_votes_type \
    as vote_metric


class StVotesRate(IMetricStrategy):

    VOTES_FOR: int = 0
    VOTES_AGAINST: int = 1


    def __init__(self, m_type) -> None:
        self.__type = m_type


    def clean_df(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


    def process_data(self, df: pd.DataFrame) -> StackedSerie:
        if pd_utl.is_an_empty_df(df):
            return StackedSerie()
        
        votes: StackedSerie = vote_metric.StVotesType().process_data(df)

        rate: List[float] = self.__calculate_rate(m_votes=votes)

        metric: StackedSerie = StackedSerie(
            serie = Serie(x=votes.get_serie()), 
            y_stack = [rate])

        return metric


    def __calculate_rate(self, m_votes: StackedSerie) -> List[float]:
        rates: List[float] = []
        votes_for: List[int] = m_votes.get_i_stack(1)
        votes_against: List[int] = m_votes.get_i_stack(0)
        votes_type: List[int] = votes_against \
            if self.__type == self.VOTES_AGAINST else votes_for

        for i, _ in enumerate(votes_for):
            denominator: int = votes_for[i] + votes_against[i]
            rate: float = votes_type[i] / denominator if denominator else None
            rates.append(rate)

        return rates
