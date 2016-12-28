# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from async_query import main


def test_async_query(cloud_config, capsys):
    query = (
        'SELECT corpus FROM publicdata:samples.shakespeare '
        'GROUP BY corpus;')

    main(
        project_id=cloud_config.project,
        query_string=query,
        batch=False,
        num_retries=5,
        interval=1,
        use_legacy_sql=True)

    out, _ = capsys.readouterr()
    value = out.strip().split('\n').pop()

    assert json.loads(value) is not None


def test_async_query_standard_sql(cloud_config, capsys):
    query = 'SELECT [1, 2, 3] AS arr;'  # Only valid in standard SQL

    main(
        project_id=cloud_config.project,
        query_string=query,
        batch=False,
        num_retries=5,
        interval=1,
        use_legacy_sql=False)

    out, _ = capsys.readouterr()
    value = out.strip().split('\n').pop()

    assert json.loads(value) is not None
