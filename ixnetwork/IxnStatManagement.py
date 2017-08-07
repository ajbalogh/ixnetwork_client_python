from __future__ import print_function
# from IxnHttp import IxnHttp
import json


class IxnStatManagement(object):
    """A high level class that simplifies the process of getting statistic results

        Example:
        stat_mgmt = IxnStatManagement(ixnhttp)
        stat_mgmt.get_views()
        port_statistics = stat_mgmt.get_view_page('Port Statistics')
        stat_mgmt.print_view_page(port_statistics)
    """

    def __init__(self, ixnhttp):
        self._ixnhttp = ixnhttp

    def get_views(self):
        """Get a list of all statistic view captions.
        A view caption corresponds to the name on the statistic view tab
        """
        self._ixnhttp.root.query.clear()
        query_result = self._ixnhttp.root.query \
            .node('statistics') \
            .node('view', properties=['caption']) \
            .go()
        view_names = []
        for view in query_result.statistics.view:
            view_names.append(view.attributes.caption.value)
        return view_names

    def get_view_page(self, view_caption):
        self._ixnhttp.root.query.clear()
        query_result = self._ixnhttp.root.query \
            .node('statistics') \
            .node('view', properties=['caption', 'enabled'], where=[{'property': 'caption', 'regex': view_caption}]) \
            .node('page', properties=['isReady']) \
            .go()
        if len(query_result.statistics.view) == 1 and query_result.statistics.view[0].page.attributes.isReady.value is True:
            query_result = query_result.statistics.view[0].query \
                .node('page', properties=['columnCaptions', 'pageValues']) \
                .go()
            page_result = []
            page_header = []
            for caption in query_result.page.attributes.columnCaptions.value:
                page_header.append(caption)
            page_result.append(page_header)            
            for row in query_result.page.attributes.pageValues.value:
                page_result.append(row[0])
            return page_result
        else:
            raise Exception('statistics view %s is not ready on the server' % view_caption)
    
    def _fill_cell(self, cell, length=15):
        if len(cell) <= 15:
            cell = '%s%s' % (cell, ' ' * (15 - len(cell)))
        else:
            cell = cell[0: 15]
        return cell

    def print_view_page(self, view_page, column_captions=None):
        """Pretty print a statistic view page returned by get_view_page."""
        indexes = []
        for index in range(len(view_page[0])):
            if column_captions is None:
                indexes.append(index)
            elif view_page[0][index] in column_captions:
                indexes.append(index)
        for index in indexes:
            print(self._fill_cell(view_page[0][index]), end='')
        print()
        for row in view_page[1:]:
            for index in indexes:
                print(self._fill_cell(row[index]), end='')
            print()
