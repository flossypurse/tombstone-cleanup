from kafka import KafkaAdminClient

BOOTSTRAP_SERVERS = ["localhost:19092"]
SECURITY_PROTOCOL = "SASL_PLAINTEXT"
SASL_MECHANISM = "SCRAM-SHA-256"
SASL_PLAIN_USERNAME = "superuser"
SASL_PLAIN_PASSWORD = "secretpassword"

admin = KafkaAdminClient(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    security_protocol=SECURITY_PROTOCOL,
    sasl_mechanism=SASL_MECHANISM,
    sasl_plain_username=SASL_PLAIN_USERNAME,
    sasl_plain_password=SASL_PLAIN_PASSWORD,
)