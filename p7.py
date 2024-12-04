from cryptography.hazmat.primitives.asymmetric import rsa 

from cryptography.hazmat.primitives import hashes 

from cryptography.hazmat.primitives.asymmetric import padding 

from cryptography.hazmat.primitives import serialization 

def generate_key_pair(): 

    private_key = rsa.generate_private_key( 

        public_exponent=65537, 

        key_size=2048, 

    ) 

    

    public_key = private_key.public_key() 

    private_pem = private_key.private_bytes( 

        encoding=serialization.Encoding.PEM, 

        format=serialization.PrivateFormat.PKCS8, 

        encryption_algorithm=serialization.NoEncryption() 

    ) 

 

   

    public_pem = public_key.public_bytes( 

        encoding=serialization.Encoding.PEM, 

        format=serialization.PublicFormat.SubjectPublicKeyInfo 

    ) 

 

    return private_pem, public_pem 

private_key, public_key = generate_key_pair() 

print(f"Private Key: \n{private_key.decode()}") 

print(f"Public Key: \n{public_key.decode()}") 

 

Digitally Sign a Document 

def sign_document(document_content, private_key_pem): 

 

    private_key = serialization.load_pem_private_key(private_key_pem, password=None) 

     

    document_hash = hashes.Hash(hashes.SHA256()) 

    document_hash.update(document_content.encode())  # Use the document content to generate hash 

    digest = document_hash.finalize() 

 

    signature = private_key.sign( 

        digest, 

        padding.PKCS1v15(), 

        hashes.SHA256() 

    ) 

     

    return signature 

document = "This is a confidential document that requires a digital signature." 

 

 

signature = sign_document(document, private_key) 

print(f"Document Signature: \n{signature.hex()}") 

 

def verify_signature(document_content, signature, public_key_pem): 

     

    public_key = serialization.load_pem_public_key(public_key_pem) 

 

   

    document_hash = hashes.Hash(hashes.SHA256()) 

    document_hash.update(document_content.encode())  # Use the document content to generate hash 

    digest = document_hash.finalize() 

 

    try: 

         

        public_key.verify( 

            signature, 

            digest, 

            padding.PKCS1v15(), 

            hashes.SHA256() 

        ) 

        print("Document is authentic and signature is valid.") 

    except Exception as e: 

        print(f"Signature verification failed: {e}") 

 

print("\nVerifying the signature on the received document...\n") 

verify_signature(document, signature, public_key) 

 

Sending the Signed Document 

print("\nSending the signed document and signature...") 

 

print(f"Document: {document}") 

print(f"Signature: {signature.hex()}") 

 

print("\nVerification at the recipient's side...") 

verify_signature(document, signature, public_key) 

 