function PredictionCard({ result }) {
    if (!result) return null;

    const isChurn = result.result?.toLowerCase().includes("yes") ||
                     result.result?.toLowerCase().includes("churn");

    return (
        <div
            style={{
                marginTop: "24px",
                padding: "28px",
                borderRadius: "18px",
                background: "#ffffff",
                border: "1px solid rgba(0, 0, 0, 0.06)",
                boxShadow: "0 2px 20px rgba(0, 0, 0, 0.04)",
                fontFamily:
                    "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', sans-serif",
                maxWidth: "420px",
            }}
        >
            <p
                style={{
                    margin: "0 0 8px 0",
                    fontSize: "13px",
                    fontWeight: 600,
                    color: "#86868b",
                    textTransform: "uppercase",
                    letterSpacing: "0.06em",
                }}
            >
                Prediction Result
            </p>

            <h2
                style={{
                    margin: "0 0 20px 0",
                    fontSize: "28px",
                    fontWeight: 700,
                    letterSpacing: "-0.02em",
                    color: isChurn ? "#ff3b30" : "#1d1d1f",
                }}
            >
                {result.result}
            </h2>

            <div
                style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",
                    padding: "14px 16px",
                    background: "#f5f5f7",
                    borderRadius: "12px",
                }}
            >
                <span style={{ fontSize: "14px", color: "#6e6e73", fontWeight: 500 }}>
                    Probability
                </span>
                <span
                    style={{
                        fontSize: "17px",
                        fontWeight: 700,
                        color: "#1d1d1f",
                        letterSpacing: "-0.01em",
                    }}
                >
                    {(result.probability * 100).toFixed(2)}%
                </span>
            </div>
        </div>
    );
}

export default PredictionCard;