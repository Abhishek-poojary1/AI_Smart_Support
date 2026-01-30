def calculate_confidence(docs_count: int, safe_refusal: bool) -> float:
    """
    Fast, explainable confidence scoring without extra LLM calls
    """

    # Safe refusal = good behavior
    if safe_refusal:
        return 0.7

    if docs_count >= 4:
        return 0.85
    if docs_count >= 2:
        return 0.7
    if docs_count == 1:
        return 0.55

    return 0.3
