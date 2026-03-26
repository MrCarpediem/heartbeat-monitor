class LLMService:
    def summarize(self, urgent, info):
        lines = []

        lines.append(" URGENT:")
        if urgent:
            for u in urgent:
                lines.append(f"- {u['message']}")
        else:
            lines.append("No urgent updates.")

        lines.append("\n INFO:")
        if info:
            for i in info:
                lines.append(f"- {i['message']}")
        else:
            lines.append("No informational updates.")

        return "\n".join(lines)