from app import create_app
from waitress import serve
import sys

if len(sys.argv) > 1:
    instance_name = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
else:
    instance_name = 'default'
    port = 5000

app = create_app(instance_name=instance_name, port=port)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=port)
