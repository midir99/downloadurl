import logging
import shutil

import requests

REQUEST_TIMEOUT = 30


def _save_file(response: requests.Response, content_type: str, filename: str) -> str:
    """The return value is the final filename used to save the file."""
    ext = content_type.split("/")[1]
    final_filename = f"{filename}.{ext}"
    with open(final_filename, "wb") as file:
        shutil.copyfileobj(response.raw, file)
    return final_filename


def _save_text_file(response: requests.Response, filename: str) -> str:
    """The return value is the final filename used to save the file."""
    final_filename = f"{filename}.html"
    with open(final_filename, "wt", encoding="utf-8") as file:
        file.write(response.text)
    return final_filename


def downloadurl(url: str, filename: str) -> str:
    """
    Please don't include the extension in the filename, it will be appended
    automatically, we will generate it from the Content-Type response header.
    This function supports the following Content-Type response headers:
    - application/pdf
    - image/jpeg
    - image/png
    - text/html; charset=utf-8
    Returns the final filename used to save the file.
    """
    try:
        res = requests.get(url, stream=True, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.SSLError:
        logging.warning("retrieving %s without SSL cert verification", url)
        res = requests.get(url, stream=True, verify=False, timeout=REQUEST_TIMEOUT)
    res.raise_for_status()
    content_type = res.headers.get("Content-Type", "").lower().strip()
    if content_type in ["application/pdf", "image/jpeg", "image/png"]:
        final_filename = _save_file(res, content_type, filename)
    elif content_type in ["text/html; charset=utf-8", "text/html;charset=utf-8"]:
        final_filename = _save_text_file(res, filename)
    else:
        raise ValueError(f"Content-Type {content_type} is not supported")
    return final_filename
