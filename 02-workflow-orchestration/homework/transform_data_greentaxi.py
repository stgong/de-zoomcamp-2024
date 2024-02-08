from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import inflection

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform_df(df: DataFrame, *args, **kwargs) -> DataFrame:

    # Rename columns in Camel Case to Snake Case,
    df.columns = [inflection.underscore(col) for col in df.columns]

    # Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    df_new = df[(df['passenger_count']>0) & (df['trip_distance']>0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    df_new['lpep_pickup_date'] = df_new['lpep_pickup_datetime'].dt.date

    print(df_new.shape)
    

    return df_new


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
