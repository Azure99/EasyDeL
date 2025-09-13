# Copyright 2025 The EasyDeL Author @erfanzar (Erfan Zare Chavoshi).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Default configuration values for ELM.

This module defines the default configuration values that are applied to all
ELM configurations when values are not explicitly specified.
"""

from __future__ import annotations

import pathlib

from .types import ELMConfig

DEFAULTS: ELMConfig = {
    "loader": {"dtype": "bf16", "param_dtype": "bf16", "verbose": True},
    "sharding": {
        "axis_dims": (1, 1, 1, -1, 1),
        "axis_names": ("dp", "fsdp", "ep", "tp", "sp"),
        "shard_attention_computation": True,
        "auto_shard_model": True,
    },
    "quantization": {"block_size": 128, "quantize_tensors": False},
    "base_config": {"values": {"hardware_abstraction": True, "use_pallas_group_matmul": False}},
    "esurge": {
        "min_input_pad": 16,
        "max_num_seqs": 32,
        "hbm_utilization": 0.80,
        "page_size": 128,
        "enable_prefix_caching": True,
        "verbose": False,
    },
    "vsurge": {
        "bytecode_decode": True,
        "interleaved_mode": False,
        "max_concurrent_decodes": 8,
        "max_concurrent_prefill": 1,
        "verbose": False,
        "seed": 448,
    },
    "mixture": {
        "cache_dir": f"{pathlib.Path.home()}/.cache/easydel",
        "streaming": True,
        "text_target_field": "text",
        "image_target_field": "image",
        "batch_size": 1,
        "shuffle_buffer_size": 1000,
        "seed": 42,
        "use_fast_loader": True,
        "num_workers": 4,
        "prefetch_size": 10,
        "enable_caching": True,
    },
}
