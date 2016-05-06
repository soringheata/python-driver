# Copyright 2013-2016 DataStax, Inc.
#
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

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa

import six

from cassandra.query import BatchStatement, SimpleStatement


class BatchStatementTest(unittest.TestCase):
    # TODO: this suite could be expanded; for now just adding a test covering a PR

    def test_clear(self):
        keyspace = 'keyspace'
        routing_key = 'routing_key'
        custom_payload = {'key': six.b('value')}

        ss = SimpleStatement('whatever', keyspace=keyspace, routing_key=routing_key, custom_payload=custom_payload)

        batch = BatchStatement()
        batch.add(ss)

        self.assertTrue(batch._statements_and_parameters)
        self.assertEqual(batch.keyspace, keyspace)
        self.assertEqual(batch.routing_key, routing_key)
        self.assertEqual(batch.custom_payload, custom_payload)

        batch.clear()
        self.assertFalse(batch._statements_and_parameters)
        self.assertIsNone(batch.keyspace)
        self.assertIsNone(batch.routing_key)
        self.assertFalse(batch.custom_payload)

        batch.add(ss)

    def test_clear_empty(self):
        batch = BatchStatement()
        batch.clear()
        self.assertFalse(batch._statements_and_parameters)
        self.assertIsNone(batch.keyspace)
        self.assertIsNone(batch.routing_key)
        self.assertFalse(batch.custom_payload)

        batch.add('something')
