from dataclasses import dataclass
from pathlib import Path
from extensions.configuration import set_defaults, read_configs_to_dataclass
from extensions.opentelemetry import configure_opentelemetry

BASE_DIR = Path(__file__).resolve().parent.parent



@dataclass
class Config:
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    
    host: str
    port: int
    
    enable_otel: bool

    

config = read_configs_to_dataclass(Config, path=BASE_DIR)


set_defaults(
    name='auth',
    namespace='fittracker',
    version='0.1.0'
)

configure_opentelemetry(
    enable_otel=config.enable_otel,
)