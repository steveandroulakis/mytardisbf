import logging
import os

logger = logging.getLogger(__name__)


def get_meta(input_file_path, output_path, **kwargs):
    """ Extract specific metadata typically used in bio-image analysis. Also
    outputs a preview image to the output directory.

    Parameters
    ----------
    input_file_path: str
        Input file path
    output_path: str

    Returns
    -------
    meta: [dict]
        List of dicts containing with keys and values for specific metadata
    """
    meta = list()
    for i in range(2):
        smeta = dict()
        smeta['id'] = i
        smeta['name'] = "mytest"

        meta.append(smeta)     

    return meta
