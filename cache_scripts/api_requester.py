"""
   Descp: Functions to fetch from endpoint given queries.

   Created on: 10-jul-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui 
        <f.r.youssef@hotmail.com>
"""

import json
from graphqlclient import GraphQLClient
from typing import Dict, List


class ApiRequester:

    ELEMS_PER_CHUNK: int = 1000


    def __init__(self, endpoint: str) -> None:
        self.__client: GraphQLClient = GraphQLClient(endpoint)


    def request(self, query: str) -> Dict:
        """
        Requests data from endpoint.
        """
        result = self.__client.execute(query)
        result = json.loads(result)
        return result['data'] if 'data' in result else dict()


    def n_requests(self, query: str, skip_n: int, result_key: str) -> List[Dict]:
        """
        Requests all chunks from endpoint.

        Parameters:
            * query: json to request
            * skip_n: number of rows to skip
            * result_key: dict key to access the list
        """
        elements: List[Dict] = list()
        result = Dict
        
        # do-while structure
        condition: bool = True

        while condition:
            query_filled: str = query.format(self.ELEMS_PER_CHUNK, skip_n + len(elements))

            try:
                result = self.request(query=query_filled)
                result = result[result_key]
            except Exception:
                print('\nError: Not all elements was requested.\n')
                return elements

            elements.extend(result)

            # if return data (result) has less than ELEMS_PER_CHUNK means that it was the last chunk 
            condition = len(result) == self.ELEMS_PER_CHUNK

        return elements
