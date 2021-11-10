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

    classification = UnicodeAttribute(null=True)
    compliance = UnicodeAttribute(null=True)
    config_crr = UnicodeAttribute(null=True)
    config_s3_logging = UnicodeAttribute(null=True)
    creation_timestamp = UnicodeAttribute(null=True)
    cross_region_replication = BooleanAttribute(null=True)
    data_lineage = UnicodeAttribute(null=True)
    derived_from = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=True)
    encryption = BooleanAttribute(null=True)
    encryption_kms_id = UnicodeAttribute(null=True)
    encryption_type = UnicodeAttribute(null=True)
    enforce_sla = BooleanAttribute(null=True)
    frequency = UnicodeAttribute(null=True)
    from_date = UnicodeAttribute(null=True)
    last_updated_timestamp = UnicodeAttribute(null=True)
    location_pointer = UnicodeAttribute(null=True)
    name = UnicodeAttribute(hash_key=True)
    owner = UnicodeAttribute(null=True)
    owner_contact = UnicodeAttribute(null=True)
    password = UnicodeAttribute(null=True)
    replaced_by = UnicodeAttribute(null=True)
    requestor_pays_enabled = BooleanAttribute(null=True)
    retention = NumberAttribute(null=True)
    s3_logging_enabled = BooleanAttribute(null=True)
    schema_location = UnicodeAttribute(null=True)
    schema_name = UnicodeAttribute(null=True)
    service_arn = UnicodeAttribute(null=True)
    sla_cron = UnicodeAttribute(null=True)
    status = UnicodeAttribute(null=True)
    tags = ListAttribute(default=[])
    to_date = UnicodeAttribute(null=True)
    type = UnicodeAttribute(null=True)
    version = NumberAttribute(null=True)


class DataSchema(Model, ModelIterator):
    class Meta:
        table_name = Config.DATASCHEMA_TABLE

    name = UnicodeAttribute(hash_key=True)
    compression = BooleanAttribute(default=False)
    dataset = UnicodeAttribute()
    derived_from = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=True)
    glue_database = UnicodeAttribute(null=True)
    glue_table = UnicodeAttribute(null=True)
    format = UnicodeAttribute(null=True)
    replaced_by = UnicodeAttribute(null=True)
    schema_content = JSONAttribute(null=True)
    schema_content_s3 = UnicodeAttribute(null=True)
    status = UnicodeAttribute()
    version = NumberAttribute(null=True)
    from_date = UnicodeAttribute(null=True)
    to_date = UnicodeAttribute(null=True)
    creation_timestamp = UnicodeAttribute(null=True)
    last_updated_timestamp = UnicodeAttribute(null=True)
