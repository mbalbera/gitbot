from functools import wraps
from lineage_tracker import emit_lineage
import traceback

def lineage_step(job_name, system="default_system", environment="dev", step_name="unnamed_step", operation=None, inputs=None, outputs=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                emit_lineage(
                    job_name=job_name,
                    system=system,
                    environment=environment,
                    step_name=step_name,
                    operation=operation,
                    status="success",
                    inputs=inputs,
                    outputs=outputs
                )
                return result
            except Exception as e:
                error_log = traceback.format_exc()
                emit_lineage(
                    job_name=job_name,
                    system=system,
                    environment=environment,
                    step_name=step_name,
                    operation=operation,
                    status="failed",
                    error=error_log,
                    inputs=inputs,
                    outputs=outputs
                )
                raise
        return wrapper
    return decorator
