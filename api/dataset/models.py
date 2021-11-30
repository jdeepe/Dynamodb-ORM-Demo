from pynamodb.attributes import (
    BooleanAttribute,
    JSONAttribute,
    ListAttribute,
    NumberAttribute,
    UnicodeAttribute,
)
from pynamodb.models import Model

from api.utils import ModelIterator
from settings import Config


class Dataset(Model, ModelIterator):
    class Meta:
        table_name = Config.DATASET_TABLE

    name = UnicodeAttribute(hash_key=True)
    classification = UnicodeAttribute(null=True)
    compliance = UnicodeAttribute(null=True)
    config_crr = UnicodeAttribute(null=True)
    config_s3_logging = UnicodeAttribute(null=True)
    creation_timestamp = UnicodeAttribute(null=True)
    encryption = BooleanAttribute(null=True)


class DataSchema(Model, ModelIterator):
    class Meta:
        table_name = Config.DATASCHEMA_TABLE

    name = UnicodeAttribute(hash_key=True)
    status = BooleanAttribute(default=False)
    dataset = UnicodeAttribute()
    version = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=True)
    last_updated_timestamp = UnicodeAttribute(null=True)
