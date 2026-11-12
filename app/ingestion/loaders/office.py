import logfire
from unstructured.partition.auto import partition

def parse_office(file_path:str):
    """
    Parses Office documents (.docx, .pptx) using the Unstructured library.
    Unlike PDFs, these formats are structured and lightweight, so they are processed locally.
    """
    with logfire.span("📄 Office Document Parsing", filename=file_path):
        try:
            # Unstructured automatically detects if it's docx or pptx
            elements = partition(file_path)
            full_text = "\n".join([str(el) for el in elements])

            if not full_text.strip():
                logfire.warning(f"⚠️ unstructured returned empty text for {file_path}.")
            else: 
                logfire.info(f"✅ Successfully parsed {len(file_path)} characters")
        except Exception as e:
            logfire.error(f"❌ Office Document Parse Failed: {e}")