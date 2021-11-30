from api.dataset.models import DataSchema, Dataset


def verify_settings(model, p_key, settings):
    details = eval(model).get(p_key)
    for key, setting in settings.items():
        print(getattr(details, key), setting)
        setting = setting if setting else None
        assert getattr(details, key) == setting


def load_data():
    load_dataschema_data()
    load_dataset()


def load_dataschema_data():
    DataSchema.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    for i in range(50):
        name = "WorkOrder_v%d" % i
        data_schema = DataSchema(name)
        data = {
            "dataset": name,
            "status": "RETIRED",
            "description": "Schema for %s" % name,
            "creation_timestamp": "2017-04-24T11:38:41.164Z",
            "last_updated_timestamp": "2017-12-24T22:38:47.346Z",
        }
        for key in data:
            setattr(data_schema, key, data[key])
        data_schema.save()


def load_dataset():
    for i in range(50):
        data = {
            "name": "Forecast_v%d" % i,
            "description": "Providing a demand forecast",
            "status": "ACTIVE",
            "type": "TRANSACTIONAL",
            "frequency": "DAILY",
            "classification": "Orange",
            "owner": "Forecast team",
            "owner_contact": "forecast@",
            "service_arn": "arn:aws:s3:::org.ent-data-lake",
            "location_pointer": "my.org/Forecasting/Forecast_v1",
            "creation_timestamp": "2017-01-12T11:39:43.164Z",
            "derived_from": None,
            "replaced_by": None,
            "from_date": "2017-01-03",
            "to_date": None,
            "schema_name": "Forecast_schema_v1",
            "schema_location": None,
            "data_lineage": None,
            "compliance": None,
            "enforce_sla": None,
            "sla_cron": "0 6 * * *",
            "tags": [
                {"key": "org", "value": "CRM"},
                {"key": "cost", "value": "SupplyChain"},
            ],
            "retention": None,
            "encryption": None,
            "encryption_type": None,
            "encryption_kms_id": None,
            "cross_region_replication": None,
            "config_crr": None,
            "password": None,
            "s3_logging_enabled": None,
            "config_s3_logging": None,
            "requestor_pays_enabled": None,
        }
        name = "Forecast_v%d" % i
        dataset = Dataset(name)
        for key in data:
            setattr(dataset, key, data[key])
        dataset.save()
