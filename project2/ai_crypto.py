from pathlib import Path
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    """Encrypt a file with AES-256-GCM; key must be exactly 32 bytes."""
    if len(key) != 32:
        raise ValueError("AES-256 requires a 32-byte key")

    plaintext = Path(input_path).read_bytes()
    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)

    # File format: 12-byte nonce followed by ciphertext and authentication tag.
    Path(output_path).write_bytes(nonce + ciphertext)
