import { useState } from "react";
import { predictChurn } from "../services/api";

const fieldStyle = {
    width: "100%",
    padding: "12px 14px",
    fontSize: "15px",
    border: "1px solid rgba(0, 0, 0, 0.1)",
    borderRadius: "10px",
    background: "#f5f5f7",
    color: "#1d1d1f",
    outline: "none",
    boxSizing: "border-box",
    fontFamily: "inherit",
    transition: "border-color 0.2s ease, background 0.2s ease",
};

const labelStyle = {
    display: "block",
    fontSize: "13px",
    fontWeight: 600,
    color: "#6e6e73",
    marginBottom: "6px",
};

function CustomerForm({ onPrediction }) {
    const [formData, setFormData] = useState({
        gender: "Male",
        tenure: 12,
        MonthlyCharges: 65,
        TotalCharges: 780,
    });
    const [loading, setLoading] = useState(false);
    const [focused, setFocused] = useState(null);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        const customer = {
            SeniorCitizen: 0,
            Partner: "No",
            Dependents: "No",
            PhoneService: "Yes",
            MultipleLines: "No",
            InternetService: "Fiber optic",
            OnlineSecurity: "No",
            OnlineBackup: "Yes",
            DeviceProtection: "No",
            TechSupport: "No",
            StreamingTV: "Yes",
            StreamingMovies: "Yes",
            Contract: "Month-to-month",
            PaperlessBilling: "Yes",
            PaymentMethod: "Electronic check",
            ...formData,
        };

        try {
            const result = await predictChurn(customer);
            onPrediction(result);
        } finally {
            setLoading(false);
        }
    };

    const getFieldStyle = (name) => ({
        ...fieldStyle,
        borderColor: focused === name ? "#1d1d1f" : "rgba(0, 0, 0, 0.1)",
        background: focused === name ? "#ffffff" : "#f5f5f7",
    });

    return (
        <form
            onSubmit={handleSubmit}
            style={{
                maxWidth: "420px",
                padding: "28px",
                background: "#ffffff",
                borderRadius: "18px",
                border: "1px solid rgba(0, 0, 0, 0.06)",
                boxShadow: "0 2px 20px rgba(0, 0, 0, 0.04)",
                fontFamily:
                    "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', sans-serif",
            }}
        >
            <h2
                style={{
                    margin: "0 0 24px 0",
                    fontSize: "20px",
                    fontWeight: 700,
                    letterSpacing: "-0.02em",
                    color: "#1d1d1f",
                }}
            >
                Customer Details
            </h2>

            <div style={{ marginBottom: "18px" }}>
                <label style={labelStyle}>Gender</label>
                <input
                    name="gender"
                    value={formData.gender}
                    onChange={handleChange}
                    onFocus={() => setFocused("gender")}
                    onBlur={() => setFocused(null)}
                    style={getFieldStyle("gender")}
                />
            </div>

            <div style={{ marginBottom: "18px" }}>
                <label style={labelStyle}>Tenure (months)</label>
                <input
                    name="tenure"
                    type="number"
                    value={formData.tenure}
                    onChange={handleChange}
                    onFocus={() => setFocused("tenure")}
                    onBlur={() => setFocused(null)}
                    style={getFieldStyle("tenure")}
                />
            </div>

            <div style={{ marginBottom: "18px" }}>
                <label style={labelStyle}>Monthly Charges</label>
                <input
                    name="MonthlyCharges"
                    type="number"
                    value={formData.MonthlyCharges}
                    onChange={handleChange}
                    onFocus={() => setFocused("MonthlyCharges")}
                    onBlur={() => setFocused(null)}
                    style={getFieldStyle("MonthlyCharges")}
                />
            </div>

            <div style={{ marginBottom: "26px" }}>
                <label style={labelStyle}>Total Charges</label>
                <input
                    name="TotalCharges"
                    type="number"
                    value={formData.TotalCharges}
                    onChange={handleChange}
                    onFocus={() => setFocused("TotalCharges")}
                    onBlur={() => setFocused(null)}
                    style={getFieldStyle("TotalCharges")}
                />
            </div>

            <button
                type="submit"
                disabled={loading}
                style={{
                    width: "100%",
                    padding: "14px",
                    fontSize: "16px",
                    fontWeight: 600,
                    color: "#ffffff",
                    background: loading ? "#a1a1a6" : "#0071e3",
                    border: "none",
                    borderRadius: "10px",
                    cursor: loading ? "default" : "pointer",
                    transition: "background 0.2s ease",
                    fontFamily: "inherit",
                }}
            >
                {loading ? "Predicting…" : "Predict"}
            </button>
        </form>
    );
}

export default CustomerForm;