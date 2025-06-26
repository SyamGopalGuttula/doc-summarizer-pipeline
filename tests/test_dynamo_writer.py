import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from unittest.mock import MagicMock, patch
from dynamo_writer import write_to_dynamodb

@patch("boto3.resource")
def test_write_to_dynamodb(mock_boto_resource):
    mock_table = MagicMock()
    mock_boto_resource.return_value.Table.return_value = mock_table

    # Simulate successful response
    mock_table.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

    response = write_to_dynamodb("TestTable", "doc1.pdf", "This is a summary.")
    
    # Assertions
    mock_table.put_item.assert_called_once()
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
