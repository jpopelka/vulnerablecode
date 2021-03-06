#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/vulnerablecode/
# The VulnerableCode software is licensed under the Apache License version 2.0.
# Data generated with VulnerableCode require an acknowledgment.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with VulnerableCode or any VulnerableCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with VulnerableCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  VulnerableCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  VulnerableCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/vulnerablecode/ for support and download.

from rest_framework import serializers

from vulnerabilities.models import Package
from vulnerabilities.models import PackageReference
from vulnerabilities.models import Vulnerability
from vulnerabilities.models import VulnerabilityReference


class PackageReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageReference
        fields = [
            'repository',
            'platform',
            'name',
            'version',
        ]


class VulnerabilityReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VulnerabilityReference
        fields = [
            'source',
            'reference_id',
            'url',
        ]


class VulnerabilitySerializer(serializers.ModelSerializer):
    references = VulnerabilityReferenceSerializer(source='vulnerabilityreference_set', many=True)

    class Meta:
        model = Vulnerability
        fields = [
            'summary',
            'cvss',
            'references',
        ]


class PackageSerializer(serializers.ModelSerializer):
    vulnerabilities = VulnerabilitySerializer(many=True)
    references = PackageReferenceSerializer(source='packagereference_set', many=True)

    class Meta:
        model = Package
        fields = [
            'name',
            'version',
            'platform',
            'vulnerabilities',
            'references',
        ]
