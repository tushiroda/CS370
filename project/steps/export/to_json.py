from pathlib import Path

from typing_extensions import Annotated
from clearml import PipelineDecorator

from llm_engineering.infrastructure.files_io import JsonFileManager


@PipelineDecorator.component()
def to_json(
    data: Annotated[dict, "serialized_artifact"],
    to_file: Annotated[Path, "to_file"],
) -> Annotated[Path, "exported_file_path"]:
    absolute_file_path = JsonFileManager.write(
        filename=to_file,
        data=data,
    )

    return absolute_file_path
