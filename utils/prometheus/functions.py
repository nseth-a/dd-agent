# (C) Datadog, Inc. 2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

from google.protobuf.internal.decoder import _DecodeVarint32  # pylint: disable=E0611,E0401

from . import metrics_pb2
import datadog_checks.utils.prometheus.functions
