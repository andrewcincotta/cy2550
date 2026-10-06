# Andrew Cincotta - Project 2
## Part 1.1
"pbkdf2" tells OpenSSL to use PBKDF2 to derive the encryption key and IV from the passphrase and salt. It's needed because a passphrase is not itself a suitable encryption key. PBKDF2 derives stronger, fixed-length values from it.

## Part 1.2
The checksums differ because OpenSSL generates a fresh random salt for each encryption, which leads to a different IV and ciphertext, even with the same plaintext and passphrase. If repeated encryptions produced indentical ciphertexts, an observer could recognize when the same message was encrypted again, revealing information about repeated plaintexts.

## Part 1.3
1. ECB produces 3 distinct blocks; the most common repeats 24 times. CBC produces 37 distinct blocks; the most common repeats once.
2. ECB leaked the repeated-block pattern, revealing which records or sections were identical.
3. What encryption mode is used, and are IVs/nonces unique and authentication tags verified?

## Part 2.2
A SHA-256 hash is unkeyed, so an attacker who changes the file can calculate a matching new hash and send both. HMAC uses a secret key, so the colleague can verify the file’s authenticity and integrity. The attacker can modify the file and recompute an unkeyed hash, but without the HMAC key cannot create a valid tag for the modified file.

## Part 3
1. Email verification shows that someone who could access that email account clicked the link, demonstrating control of the address at that time. It does **not** prove the person’s real-world identity or that the public key belongs to them.
2. Independently ask the classmate for their full key fingerprint through a trusted, separate channel, such as in person, and compare all 40 hexadecimal characters with the downloaded key’s fingerprint. A network attacker cannot substitute a different key without changing its fingerprint, and cannot alter the fingerprint you obtained independently.

## Part 4.2
1. The public-key encrypted session-key packet contains a randomly generated symmetric session key, encrypted with the recipient’s RSA public key. The encrypted data packet contains the message encrypted with that session key.
2. RSA is inefficient and can only encrypt data smaller than its key size, with additional padding overhead. A symmetric cipher can efficiently encrypt messages of arbitrary practical length.
3. This is hybrid encryption.

## Part 4.3
Private key is used for signing. The signer's public key is used for verifying. The recipient's public key is used for encryption. The recipient's private key is used for decryption. Signing provides authenticity and integrity, it lets other verify who signed the file and whether it changed, that encryption alone does not.

## Part 5
Ed25519’s 256-bit key uses elliptic-curve cryptography, which achieves strong security with much shorter keys than RSA. Key sizes aren’t directly comparable across algorithms, so a smaller Ed25519 key isn’t necessarily weaker than a 4096-bit RSA key.

## Part 7.1
For 7.1, I used GPT 5.6-Sol, and copy-pasted the prompt from Canvas.

## Part 7.2
The function itself is secure. I don't think it has three real defects, and claiming otherwise would mean inventing problems. Here's why its secure:
It uses authenticated encryption, AES-GCM is an AEAD mode, so it provides confidentiality and integrity together. The key size is enforced, so the length check rejects anything that isn't 32 bytes and the code can't fall back to a weaker key. The nonce is handled correctly. This means it is 12 bytes, which is the size GCM is designed for. A fresh nonce comes from os.urandom, a cryptographically secure random generator, on every call. Lastly, it follows Kerckhoff's principle. Security rtests entirely on the key. Knowing the file format or the algorithm gives an attacker nothing. HOWEVER, the plaintext lingers in memory, and python can't avoid this, so maybe that is a defect??

## Part 7.3
I did not change anything because I defended why it is secure. Thus, I just ran the python file. I also copy-pasted the original into fixed_crypto.py.
