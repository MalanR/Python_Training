import pytest
import asyncio
from process_api import ProcessAPI
from measures_module import Measures
from triggers_module import Triggers
from main import data_structure

api = ProcessAPI()


@pytest.mark.asyncio
async def test_add_module():
    api.add_module("measure", Measures)
    api.add_module("triggers", Triggers)
    assert 'measure' in api.modules
    assert 'triggers' in api.modules


@pytest.mark.asyncio
async def test_add_module_fail():
    with pytest.raises(TypeError):
        api.add_module('measures')
        api.add_module('triggers')


@pytest.mark.asyncio
async def test_add_module_fail2():
    with pytest.raises(TypeError):
        api.add_module(Measures)
        api.add_module(Triggers)


@pytest.mark.asyncio
async def test_call():
    api.call("measure", "create", {"api": api, "data_structure": data_structure})

    measurements = data_structure['measurement']
    for measure in measurements:
        for trigger in measure['triggers']:
            assert trigger['measure_code'] == measure['code']


@pytest.mark.asyncio
async def test_call_fail():
    with pytest.raises(TypeError):
        api.call("triggers", {"api": api, "data_structure": data_structure})

        measurements = data_structure['measurement']
        for measure in measurements:
            for trigger in measure['triggers']:
                assert trigger['measure_code'] == measure['code']
