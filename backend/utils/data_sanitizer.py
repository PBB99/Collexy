class DataSanitizer:
    @staticmethod
    def sanitize_payload(payload: dict) -> dict:
        """
        Transforma valores vacíos ('') o None en None para que
        puedan ser tratados como NULL en la base de datos.
        """
        if not payload:
            return {}
        return {k: (v if v not in ("", None) else None) for k, v in payload.items()}
