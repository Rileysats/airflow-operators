from airflow.models import BaseOperator
from airflow.utils.context import Context
from typing import Any, Dict

class XComPushOperator(BaseOperator):
    """
    Operator that pushes multiple XCom values in a single task.
    
    :param xcom_values: Dictionary of key-value pairs to push as XCom
    :type xcom_values: Dict[str, Any]
    """
    template_fields = ('xcom_values',)  # Enable Jinja templating for xcom_values

    def __init__(
            self, 
            xcom_values: Dict[str, Any],
            *args, 
            **kwargs
        ):
        super().__init__(*args, **kwargs)
        self.xcom_values = xcom_values

    def execute(self, context: Context) -> Any:
        for key, value in self.xcom_values.items():
            context['ti'].xcom_push(key=key, value=value)
        self.log.info(f'Pushed XCom values: {self.xcom_values}')
        return self.xcom_values 