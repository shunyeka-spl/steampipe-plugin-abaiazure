select name, id, type, region, resource_group, subscription_id
from abaiazure.abaiazure_app_configuration
where id = '{{ output.resource_id.value }}';
