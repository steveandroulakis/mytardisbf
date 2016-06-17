from mytardisbf import metadata, tasks
from django.conf import settings
from tardis.tardis_portal.models import Schema, DatafileParameterSet


class MetadataFilter(object):
    """MyTardis filter for extracting metadata from micrscopy image
    formats using the Bioformats library.

    Attributes
    ----------
    name: str
        Short name for schema
    schema: str
        Name of the schema to load the EXIF data into.
    """
    def __init__(self, name, schema):
        self.name = name
        self.schema = "http://tardis.edu.au/schemas/robtest/1"

    def __call__(self, sender, **kwargs):
        """Post save call back to invoke this filter.

        Parameters
        ----------
        sender: Model
            class of the model
        instance: model Instance
            Instance of model being saved.
        created: boolean
            Specifies whether a new record is being created.
        """
        instance = kwargs.get('instance')
        
        # use instance to extract metadata here

        # this splits by extension
        #input_fname, ext = os.path.splitext(os.path.basename(instance))
        
        # eg. process_file(instance)

        # write result to database  
        ps = DatafileParameterSet(schema=self.schema, datafile=instance)
        ps.save()    

        dfp = DatafileParameter(parameterset=ps, name='samplesperpixel')
        dfp.string_value = "rob test"

        dfp.save()


def make_filter(name, schema):
    return MetadataFilter(name, schema)

make_filter.__doc__ = MetadataFilter.__doc__
