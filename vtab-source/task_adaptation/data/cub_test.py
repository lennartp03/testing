# coding=utf-8
# Copyright 2019 Google LLC.
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

"""Tests for cub.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from task_adaptation.data import cub
from task_adaptation.data import data_testing_lib
import tensorflow.compat.v1 as tf


class CUB2011DataTest(data_testing_lib.BaseTfdsDataTest):
  """See base class for usage and test descriptions."""

  def setUp(self):
    self.dataset = cub.CUB2011Data()
    super(CUB2011DataTest, self).setUp(
        data_wrapper=self.dataset,
        num_classes=200,
        expected_num_samples=dict(
            train=5395,
            val=599,
            trainval=5994,
            test=5794,
        ),
        required_tensors_shapes={
            "image": (None, None, 3),
            "label": (),
        })


if __name__ == "__main__":
  tf.test.main()
