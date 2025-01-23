import sys
import base64
import urllib.parse
from proto import migration_pb2


def decode_migration_text(migration_text):
    try:
        # Remove the prefix and decode URL encoding
        data = migration_text.replace('otpauth-migration://offline?data=', '')
        data = urllib.parse.unquote(data)  # Add this line to handle URL encoding

        # Decode base64
        decoded = base64.b64decode(data)

        # Parse the protobuf message
        payload = migration_pb2.MigrationPayload()
        payload.ParseFromString(decoded)

        # Extract and print details for each OTP
        for otp in payload.otp_parameters:
            print(f"\nName: {otp.name}")
            print(f"Secret: {base64.b32encode(otp.secret).decode('utf-8')}")
            print(f"Issuer: {otp.issuer}")
            print(f"Algorithm: {otp.algorithm}")
            print(f"Digits: {otp.digits}")
            print(f"Type: {'TOTP' if otp.type == 2 else 'HOTP'}")
            print("-" * 50)

    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 decode_auth.py <migration_text>")
        sys.exit(1)

    decode_migration_text(sys.argv[1])