import unittest
from unittest.mock import Mock, patch
# from src.operators.custom_operators import CustomOperator
from src.operators.xcom_push_operator import XComPushOperator

# class TestCustomOperator(unittest.TestCase):

#     def setUp(self):
#         self.operator = CustomOperator(task_id='test_task')

#     def test_execute(self):
#         result = self.operator.execute()
#         self.assertIsNotNone(result)  # Replace with actual expected result

class TestXComPushOperator(unittest.TestCase):

    def setUp(self):
        self.operator = XComPushOperator(
            task_id='test_xcom_push',
            xcom_values={'key1': 'value1', 'key2': 'value2'}
        )

    def test_execute(self):
        # Create a mock task instance
        mock_ti = Mock()
        mock_ti.xcom_push = Mock()

        # Create mock context with task instance
        mock_context = {
            'ti': mock_ti,
            'task': self.operator,
            'dag': Mock(),
            'dag_run': Mock(),
            'task_instance': mock_ti,
            'execution_date': None,
            'logical_date': None,
        }

        # Execute the operator
        result = self.operator.execute(context=mock_context)

        # Assert the results
        self.assertEqual(result, {'key1': 'value1', 'key2': 'value2'})
        
        # Verify xcom_push was called for each value
        expected_calls = [
            unittest.mock.call(key='key1', value='value1'),
            unittest.mock.call(key='key2', value='value2')
        ]
        mock_ti.xcom_push.assert_has_calls(expected_calls, any_order=True)
        self.assertEqual(mock_ti.xcom_push.call_count, 2)

if __name__ == '__main__':
    unittest.main()