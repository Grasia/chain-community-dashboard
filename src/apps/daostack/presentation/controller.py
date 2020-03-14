"""
   Descp: It's used to manage the dashboard events.

   Created on: 20-feb-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui 
        <f.r.youssef@hotmail.com>
"""

from typing import List, Dict
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from src.app import app
import src.apps.daostack.presentation.layout as ly
from src.apps.daostack.resources.strings import TEXT
from src.apps.daostack.business.transfers.stacked_serie import StackedSerie
from src.apps.daostack.business.app_service import get_service


def init():
    pass


def __get_data_from_metric(metric: StackedSerie) -> List:
    i_stack: int = 0
    return [
        ly.generate_bar_chart(
            x = metric.get_serie(), 
            y = metric.get_i_stack(i_stack)),
        TEXT['graph_amount'].format(metric.get_last_serie_elem(), 
            metric.get_last_value(i_stack)),
        TEXT['graph_subtitle'].format(metric.get_diff_last_values(i_stack))
    ]


@app.callback(
    [Output('new-users-graph', 'figure'),
    Output('new-users-amount', 'children'),
    Output('new-users-subtitle', 'children')],
    [Input('org-dropdown', 'value')]
)
def update_new_user_graph(org_id):
    if not org_id:
        raise PreventUpdate
    
    return __get_data_from_metric(get_service().get_metric_new_users(org_id))


@app.callback(
    [Output('new-proposal-graph', 'figure'),
    Output('new-proposal-amount', 'children'),
    Output('new-proposal-subtitle', 'children')],
    [Input('org-dropdown', 'value')]
)
def update_proposal_graph(org_id):
    if not org_id:
        raise PreventUpdate

    return __get_data_from_metric(get_service().get_metric_new_proposals(org_id))


@app.callback(
    Output('proposals-type-graph', 'figure'),
    [Input('org-dropdown', 'value')]
)
def update_proposals_type_graph(org_id):
    if not org_id:
        raise PreventUpdate

    attrs: Dict = get_service().get_metric_type_proposals(org_id)
    return ly.generate_4stacked_bar_chart(
            x=attrs['metric'].get_serie(), 
            y=attrs['metric'].get_n_stacks(4),
            text=attrs['text'],
            color=attrs['color']
        )