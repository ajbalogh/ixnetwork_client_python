"""Encapsulates file transfer
"""
import json
import os


class IxnFileManagement(object):
    """File management """
    
    def __init__(self, ixnhttp):
        self._ixnhttp = ixnhttp
    
    def create(self, remote_filename):
        """Create an empty file on the server """
        url = '/files?filename=%s' % remote_filename
        return self._add_href(self._ixnhttp.post(url, file_content='').files[0])

    def delete(self, remote_filename):
        """Delete a file on the server """
        url = '/files?filename=%s' % remote_filename
        return self._ixnhttp.delete(url)
    
    def upload(self, local_filename):
        """Upload file to the server """
        filename = self._get_filename(local_filename)
        url = '/files?filename=%s' % filename
        with open(local_filename, 'rb') as fid:
            return self._add_href(self._ixnhttp.post(url, fid=fid).files[0])

    def download(self, remote_filename, local_filename):
        """Download a file from the server """
        url = '/files?filename=%s' % remote_filename
        with open(local_filename, 'wb') as fid:
            self._ixnhttp.get(url, fid=fid)

    def files(self, match=None):
        """Get a list of files currently on the server """
        files = []
        file_list = self._ixnhttp.get('/files').files
        for file in file_list:
            self._add_href(file)
        for file in file_list:
            if match is not None:
                if match in file.name:
                    files.append(file)
            else:
                    files.append(file)
        return files

    def _get_filename(self, filename):
        return os.path.basename(os.path.normpath(filename))

    def _add_href(self, file_object):
        file_object.href = '/api/v1/sessions/%s/ixnetwork/files/%s' % (self._ixnhttp.current_session.id, file_object.name)
        return file_object


