
import os

import yaml

from ..greeter import greet

def test_greet():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures',
                           'samples.yaml')) as fixtures_file:
        fixtures = yaml.safe_load(fixtures_file)
        for fixture in fixtures:
            answer = fixture.pop('answer')
            assert greet(**fixture) == answer