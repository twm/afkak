# -*- coding: utf-8 -*-
# Copyright (C) 2015 Cyan, Inc.

from __future__ import absolute_import

from .client import KafkaClient
from .kafkacodec import (
    create_message, create_gzip_message, create_snappy_message
)
from .producer import Producer
from .partitioner import RoundRobinPartitioner, HashedPartitioner
from .consumer import Consumer
from .common import (OFFSET_EARLIEST, OFFSET_LATEST, OFFSET_COMMITTED,)

__title__ = 'afkak'
__version__ = '1.0.0'
__author__ = 'Robert Thille'
__license__ = 'Apache License 2.0'
__copyright__ = 'Copyright 2015, Cyan Inc. under Apache License, v2.0'

__all__ = [
    'KafkaClient', 'Producer', 'Consumer',
    'RoundRobinPartitioner', 'HashedPartitioner',
    'create_message', 'create_gzip_message',
    'create_snappy_message',
    'OFFSET_EARLIEST', 'OFFSET_LATEST', 'OFFSET_COMMITTED',
]
