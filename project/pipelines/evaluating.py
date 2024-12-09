from clearml import PipelineDecorator

from steps import evaluating as evaluating_steps


@PipelineDecorator.component()
def evaluating(
    is_dummy: bool = False,
) -> None:
    evaluating_steps.evaluate(
        is_dummy=is_dummy,
    )
