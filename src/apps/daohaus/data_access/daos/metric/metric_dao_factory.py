"""
   Descp: This file is used as factory to create a DAO metric

   Created on: 5-oct-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui
        <f.r.youssef@hotmail.com>
"""
from typing import List

from src.apps.common.data_access.daos.metric.metric_dao \
    import MetricDao
import src.apps.daohaus.data_access.requesters.cache_requester as cache
from src.apps.daohaus.data_access.daos.metric.strategy.st_new_additions import StNewAdditions
from src.apps.daohaus.data_access.daos.metric.strategy.st_votes_type import StVotesType
from src.apps.daohaus.data_access.daos.metric.strategy.st_active_voters import StActiveVoters

NEW_MEMBERS = 0
VOTES_TYPE = 1
ACTIVE_VOTERS = 2
RAGE_QUITS = 3
NEW_PROPOSALS = 4


def get_dao(ids: List[str], metric: int) -> MetricDao:
    requester: cache.CacheRequester = None
    stg = None
    
    if metric == NEW_MEMBERS:
        stg = StNewAdditions(typ=StNewAdditions.MEMBERS)
        requester = cache.CacheRequester(srcs=[cache.MEMBERS])
    elif metric == VOTES_TYPE:
        stg = StVotesType()
        requester = cache.CacheRequester(srcs=[cache.VOTES])
    elif metric == ACTIVE_VOTERS:
        stg = StActiveVoters()
        requester = cache.CacheRequester(srcs=[cache.VOTES])
    elif metric == RAGE_QUITS:
        stg = StNewAdditions(typ=StNewAdditions.RAGE_QUITS)
        requester = cache.CacheRequester(srcs=[cache.RAGE_QUITS])
    elif metric == NEW_PROPOSALS:
        stg = StNewAdditions(typ=StNewAdditions.PROPOSALS)
        requester = cache.CacheRequester(srcs=[cache.PROPOSALS])

    return MetricDao(ids=ids, strategy=stg, requester=requester, address_key='molochAddress')
