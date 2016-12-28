# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Integration tests for Dataproc samples.

Creates a Dataproc cluster, uploads a pyspark file to Google Cloud Storage,
submits a job to Dataproc that runs the pyspark file, then downloads
the output logs from Cloud Storage and verifies the expected output."""

from gcp.testing.flaky import flaky

import create_cluster_and_submit_job

CLUSTER_NAME = 'testcluster2'
ZONE = 'us-central1-b'


@flaky
def test_e2e(cloud_config):
    output = create_cluster_and_submit_job.main(
        cloud_config.project, ZONE, CLUSTER_NAME, cloud_config.storage_bucket)
    assert b"['Hello,', 'dog', 'elephant', 'panther', 'world!']" in output
