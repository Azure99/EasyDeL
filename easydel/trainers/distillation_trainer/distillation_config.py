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
from dataclasses import field

from eformer.pytree import auto_pytree

from easydel.utils import Registry
from easydel.utils.compiling_utils import hash_fn

from ..training_configurations import TrainingArguments


@Registry.register("trainer-arguments", "distillation")
@auto_pytree
class DistillationConfig(TrainingArguments):
    """Configuration class for knowledge distillation training.

    This configuration extends TrainingArguments with parameters specific to
    knowledge distillation, where a smaller student model learns to mimic
    a larger teacher model's behavior.

    Knowledge distillation uses temperature scaling to soften the probability
    distributions from both models, allowing the student to learn from the
    teacher's confidence across all classes rather than just hard labels.

    Attributes:
        trainer_prefix (str | None): Prefix for trainer logs and checkpoints.
            Default: "distillationtrainer"
        temperature (float): Temperature parameter for softening probability
            distributions. Higher values create softer distributions, revealing
            more information about the teacher's relative confidence across classes.
            Typical values range from 3.0 to 10.0. Default: 2.0
        alpha (float): Weight balancing distillation loss vs supervised loss.
            - alpha=1.0: Pure distillation (only learn from teacher)
            - alpha=0.0: Pure supervised learning (only learn from labels)
            - 0<alpha<1: Combination of both losses
            Default: 0.9 (90% distillation, 10% supervised)

    Example:
        >>> config = DistillationConfig(
        ...     temperature=5.0,
        ...     alpha=0.7,
        ...     learning_rate=1e-4,
        ...     num_train_epochs=10
        ... )

    Note:
        The distillation loss is computed as:
        Loss = alpha * KL(student/T, teacher/T) + (1-alpha) * CE(student, labels)
        where T is the temperature parameter.
    """

    trainer_prefix: str | None = field(
        default="distillationtrainer", metadata={"help": "Prefix used for trainer logs, checkpoints, and wandb runs."}
    )
    temperature: float = field(
        default=2.0,
        metadata={
            "help": "Temperature for softening probability distributions. Higher values "
            "create softer distributions, revealing more about teacher's confidence."
        },
    )
    alpha: float = field(
        default=0.9,
        metadata={
            "help": "Weight for distillation loss vs supervised loss. "
            "1.0 = pure distillation, 0.0 = pure supervised learning."
        },
    )
    __hash__ = hash_fn
