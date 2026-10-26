# Copyright 2026, Pulumi Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from pulumi.provider.experimental.provider import CreateRequest


@pytest.mark.parametrize(
    "urn,expected_type,expected_name",
    [
        (
            "urn:pulumi:dev::proj::pkg:index:Thing::name",
            "pkg:index:Thing",
            "name",
        ),
        (
            "urn:pulumi:dev::proj::pkg:index:Thing::a::b",
            "pkg:index:Thing",
            "a::b",
        ),
        (
            "urn:pulumi:dev::proj::pkg:index:Parent$pkg:index:Thing::a::b::c",
            "pkg:index:Parent$pkg:index:Thing",
            "a::b::c",
        ),
    ],
)
def test_request_type_and_name(urn: str, expected_type: str, expected_name: str):
    request = CreateRequest(urn=urn, properties={}, timeout=0, preview=False)
    assert request.type == expected_type
    assert request.name == expected_name
