"""
   Descp: A factory of dao stacked serie

   Created on: 13-mar-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui 
        <f.r.youssef@hotmail.com>
"""
from typing import List

from src.apps.daostack.data_access.graphql.dao_metric.dao_metric \
    import DaoStackedSerie
from src.api.graphql.daostack.api_manager import ApiRequester
import src.apps.daostack.data_access.graphql.dao_metric.strategy.\
    st_time_serie as st_s
import src.apps.daostack.data_access.graphql.dao_metric.strategy.\
    st_proposal_outcome as st_po
import src.apps.daostack.data_access.graphql.dao_metric.strategy.\
    st_different_voters_stakers as st_vs
from src.apps.daostack.data_access.graphql.dao_metric.strategy.\
    st_proposal_majority import StProposalMajority


NEW_USERS = 0
NEW_PROPOSALS = 1
PROPOSALS_BOOST_OUTCOME = 2
TOTAL_VOTES = 3
TOTAL_STAKES = 4
DIFFERENT_VOTERS = 5
DIFFERENT_STAKERS = 6
PROPOSAL_MAJORITY = 7
PROPOSALS_TOTAL_SUCCES_RATIO = 8
PROPOSALS_BOOST_SUCCES_RATIO = 9


def get_dao(ids: List[str], metric: int) -> DaoStackedSerie:# noqa: C901
    requester: ApiRequester = ApiRequester()

    stg = None
    if metric == NEW_USERS:
        stg = st_s.StTimeSerie(st_s.METRIC_TYPE_NEW_USERS)
    elif metric == NEW_PROPOSALS:
        stg = st_s.StTimeSerie(st_s.METRIC_TYPE_NEW_PROPOSAL)
    elif metric == TOTAL_VOTES:
        stg = st_s.StTimeSerie(st_s.METRIC_TYPE_TOTAL_VOTES)
    elif metric == TOTAL_STAKES:
        stg = st_s.StTimeSerie(st_s.METRIC_TYPE_TOTAL_STAKES)
    elif metric == PROPOSALS_BOOST_OUTCOME:
        stg = st_po.StProposalOutcome(st_po.METRIC_TYPE_BOOST_OUTCOME)
    elif metric == DIFFERENT_VOTERS:
        stg = st_vs.StDifferentVS(st_vs.METRIC_VOTERS)
    elif metric == DIFFERENT_STAKERS:
        stg = st_vs.StDifferentVS(st_vs.METRIC_STAKERS)
    elif metric == PROPOSAL_MAJORITY:
        stg = StProposalMajority()
    elif metric == PROPOSALS_TOTAL_SUCCES_RATIO:
        stg = st_po.StProposalOutcome(st_po.METRIC_TYPE_TOTAL_SUCCESS_RATIO)
    elif metric == PROPOSALS_BOOST_SUCCES_RATIO:
        stg = st_po.StProposalOutcome(st_po.METRIC_TYPE_BOOST_SUCCESS_RATIO)

    return DaoStackedSerie(ids=ids, strategy=stg, requester=requester)