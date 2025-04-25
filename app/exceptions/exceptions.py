from fastapi import HTTPException

not_found_exception = HTTPException(status_code=404, detail=f"No expected result was found.")
not_found_exception_doc = {
    404: {
        "content": {
            "application/json": {
                "example": {
                    "detail": "No expected result was found."
                }
            }
        },
    },
}
